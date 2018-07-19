#!/usr/bin/env python

import sys
import re


def appref(m):
    return '[APPENDIX][{}]'.format(m.group(1))
appref.pattern = re.compile(r'@@appendix@@(.+?)@@')


def chapref(m):
    return '[CHAPTER][{}]'.format(m.group(1))
chapref.pattern = re.compile(r'@@chapter@@(.+?)@@')


def cite(m):
    return '[{}]'.format(','.join(['[{}](../bib/#{})'.format(c, c) for c in m.group(1).split(',')]))
cite.pattern = re.compile(r'@@cite@@(.+?)@@')


def exercise(m):
    return '### {}\n**({}/{})**'.format(m.group(1), m.group(2), m.group(3))
exercise.pattern = re.compile(r'@@exercise@@(.+?)@@(.+?)@@(.+?)@@')


def figref(m):
    return '[FIGURE][{}]'.format(m.group(1))
figref.pattern = re.compile(r'@@figure@@(.+?)@@')


def glossdef(m):
    return '**' + m.group(2) + '**{:#' + m.group(1) + '}:'
glossdef.pattern = re.compile(r'@@glossdef@@(.+?)@@(.+?)@@')


def glossref(m):
    return '**[{}](../gloss/#{})**'.format(m.group(2), m.group(1))
glossref.pattern = re.compile(r'@@glossref@@(.+?)@@(.+?)@@')


def secref(m):
    return '[SECTION][{}]'.format(m.group(1))
secref.pattern = re.compile(r'@@section@@(.+?)@@')


FUNCS = [appref, chapref, cite, exercise, figref, glossdef, glossref, secref]


def main():
    data = sys.stdin.read()
    for func in FUNCS:
        data = func.pattern.sub(func, data)
    sys.stdout.write(data)


if __name__ == '__main__':
    main()
