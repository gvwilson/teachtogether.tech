#!/usr/bin/env python

'''Convert bibliography to LaTeX so that Pandoc can convert to HTML.'''

import sys
import re


keyPat = re.compile(r'\\bibitem.+{([^}]+)}')
def keySub(match):
    key = match.group(1)
    return r'[' + key + ']'


def main():
    print(r'\chapter{Bibliography}\label{s:bib}')
    print(r'\newcommand{\bibnote}[1]{\emph{#1}}')
    with open(sys.argv[1], 'r') as reader:
        for line in reader:
            if r'\newcommand' in line:
                continue
            if r'\begin{thebibliography}' in line:
                continue
            if r'\end{thebibliography}' in line:
                continue
            line = line.replace(r'\newblock ', '')
            line = keyPat.sub(keySub, line)
            sys.stdout.write(line)

    
if __name__ == '__main__':
    main()
