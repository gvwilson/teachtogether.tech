#!/usr/bin/env python

import sys
import re


def appref(m):
    return '[APPENDIX][{}]'.format(m.group(1))
appref.pattern = re.compile(r'@@appendix@@(.+?)@@')


def chapref(m):
    return '[CHAPTER][{}]'.format(m.group(1))
chapref.pattern = re.compile(r'@@chapter@@(.+?)@@')


def figref(m):
    return '[FIGURE][{}]'.format(m.group(1))
figref.pattern = re.compile(r'@@figure@@(.+?)@@')


def secref(m):
    return '[SECTION][{}]'.format(m.group(1))
secref.pattern = re.compile(r'@@section@@(.+?)@@')


FUNCS = [appref, chapref, figref, secref]


def main():
    data = sys.stdin.read()
    for func in FUNCS:
        data = func.pattern.sub(func, data)
    sys.stdout.write(data)


if __name__ == '__main__':
    main()
