#!/usr/bin/env python

import sys
import re


GLOSS_DEF = re.compile(r'\\gitem{(.+?)}{.+?}', re.DOTALL + re.MULTILINE)
GLOSS_USE = re.compile(r'\\gref{(.+?)}{.+?}', re.DOTALL + re.MULTILINE)


def main(filenames):
    files = [(f, open(f, 'r').read()) for f in filenames]
    gloss(files)


def gloss(files):
    defined = find_all(GLOSS_DEF, files)
    used = find_all(GLOSS_USE, files)
    report('Glossary', 'missing', used - defined)
    report('Glossary', 'unused', defined - used)


def find_all(pattern, files):
    result = set()
    [result.update(pattern.findall(text)) for (name, text) in files]
    return result


def report(major, minor, values):
    if values:
        print(f'{major} {minor}')
        for v in sorted(values):
            print(f'  {v}')


if __name__ == '__main__':
    main(sys.argv[1:])
