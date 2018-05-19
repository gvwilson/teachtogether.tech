#!/usr/bin/env python

'''Pre-processing for LaTeX-to-HTML conversion.'''

import sys
import re


CrossRef = {}
crossRefPat = re.compile(r'\\newlabel{((s|f):[^}]+)}.+{(.+)}{}}$')
def readCrossRef(filename):
    with open(filename, 'r') as reader:
        for line in reader:
            m = crossRefPat.search(line)
            if not m:
                continue
            label = m.group(1)
            filename = m.group(1).split(':')[1].split('-')[0] + '.html'
            number = m.group(3).split('.', 1)[1]
            CrossRef[label] = (filename, number)


def macroHandler(line):
    if r'\renewcommand{\href}' in line:
        return True


calloutPat = re.compile(r'\\begin{callout}{(.+)}')
def calloutHandler(line):
    '''Pandoc won't handle an environment with an argument, so \callout has to be replaced.'''

    if r'\newenvironment{callout}' in line:
        return True

    if r'\begin{callout}' in line:
        m = calloutPat.search(line)
        line = r'\begin{quote}\textbf{' + m.group(1) + '}'
        print(line)
        return True

    if r'\end{callout}' in line:
        print(r'\end{quote}')
        return True

    return False


objectivesPat = re.compile(r'\\begin{objectives}')
def objectivesHandler(line):
    '''Pandoc won't insert title of the "objectives" callout, so we have to.'''

    if r'\newenvironment{objectives}' in line:
        return True

    if r'\begin{objectives}' in line:
        m = objectivesPat.search(line)
        line = r'\begin{quote}\noindent\textbf{After reading this chapter, you will be able to{\ldots}}\begin{itemize}'
        print(line)
        return True

    if r'\end{objectives}' in line:
        print(r'\end{itemize}\end{quote}')
        return True

    return False


def citeSub(match):
    # Have to wrap the '[' and ']' in '$' because otherwise the output
    # might contain '\item [Cite1234] says...'.
    cites = match.group(1).split(',')
    cites = [r'\href{./bib.html#' + c + '}{' + c + '}' for c in cites]
    cites = '$[$' + ','.join(cites) + '$]$'
    return cites
citeSub.pattern = re.compile(r'\\cite{([^}]+)}')


def apprefSub(match):
    label = match.group(1)
    filename, number = CrossRef[label]
    return r'\href{./' + filename + '}{Appendix~' + number + '}'
apprefSub.pattern = re.compile(r'\\appref{(s:[^}]+)}')


def chaprefSub(match):
    label = match.group(1)
    filename, number = CrossRef[label]
    return r'\href{./' + filename + '}{Chapter~' + number + '}'
chaprefSub.pattern = re.compile(r'\\chapref{(s:[^}]+)}')


def chaptitleSub(match):
    text = match.group(1)
    label = match.group(2)
    filename, number = CrossRef[label]
    return r'\chapter{' + number + ') ' + text + r'}\label{' + label + '}'
chaptitleSub.pattern = re.compile(r'\\chapter{(.+?)}\\label{(.+?)}')


def secrefSub(match):
    label = match.group(1)
    filename, number = CrossRef[label]
    return r'\href{./' + filename + '#' + label + '}{Section~' + number + '}'
secrefSub.pattern = re.compile(r'\\secref{(s:[^}]+)}')


def sectitleSub(match):
    level = match.group(1)
    text = match.group(2)
    label = match.group(3)
    filename, number = CrossRef[label]
    return '\\' + level + '{' + number + ') ' + text + r'}\label{' + label + '}'
sectitleSub.pattern = re.compile(r'\\(.*?section){(.+?)}\\label{(.+?)}')


def figrefSub(match):
    label = match.group(1)
    filename, number = CrossRef[label]
    return r'\href{./' + filename + '#' + label + '}{Figure~' + number + '}'
figrefSub.pattern = re.compile(r'\\figref{(f:[^}]+)}')


def fignumberSub(match):
    caption = match.group(1)
    label = match.group(2)
    filename, number = CrossRef[label]
    return r'\caption{Figure ' + number + ': ' + caption + '}\n' + r'\label{' + label + '}'
fignumberSub.pattern = re.compile(r'\\caption{(.+?)}\s*\\label{(.+?)}', re.DOTALL)


def glossrefSub(match):
    label = match.group(1)
    text = match.group(2)
    return r'\href{./gloss.html#' + label + r'}{\textbf{' + text.replace('\n', ' ') + '}}'
glossrefSub.pattern = re.compile(r'\\glossref{([^}]+)}{([^}]+)}', re.DOTALL)


def glossdefSub(match):
    label = match.group(1)
    text = match.group(2)
    return r'\item[' + text.replace('\n', ' ') + r':]\label{' + label + r'}'
glossdefSub.pattern = re.compile(r'\\glossdef{([^}]+)}{([^}]+)}', re.DOTALL)


PatSubs = (citeSub, figrefSub, fignumberSub,
           chaptitleSub, apprefSub, chaprefSub, sectitleSub, secrefSub,
           glossrefSub, glossdefSub)


def main():
    readCrossRef(sys.argv[1])
    doc = sys.stdin.read()

    # Convert macro usages.
    for func in PatSubs:
        doc = func.pattern.sub(func, doc)

    for line in doc.split('\n'):

        # Filter some macro definitions.
        if macroHandler(line):
            continue

        # Callouts and objectives need special handling.
        if calloutHandler(line):
            continue
        if objectivesHandler(line):
            continue

        # Display.
        sys.stdout.write(line)
        sys.stdout.write('\n')


if __name__ == '__main__':
    main()
