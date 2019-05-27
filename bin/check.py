#!/usr/bin/env python

import sys
import re
import getopt


def main(args):
    bib_filename, tex_filenames = parse_args(args)
    if bib_filename:
        check_bib(bib_filename)
    check_gloss(tex_filenames)


def parse_args(args):
    bib_filename = None
    options, tex_filenames = getopt.getopt(args, 'b:')
    for (opt, arg) in options:
        if opt == '-b':
            bib_filename = arg
        else:
            fail(f'Unknown option "{opt}"')
    return bib_filename, tex_filenames


def check_bib(bib_filename):
    BIB_KEY = re.compile(r'^@[a-z]+?{(\w+?),$', re.DOTALL + re.MULTILINE)
    KEY_PAT = re.compile(r'[A-Z][A-Za-z]{1,3}[0-9]{4}')
    text = open(bib_filename, 'r').read()
    keys = BIB_KEY.findall(text)
    mismatch = [k for k in keys if not KEY_PAT.match(k)]
    report('Bibliography', 'bad keys', mismatch)


def check_gloss(tex_filenames):
    GLOSS_DEF = re.compile(r'\\gitem{(.+?)}{.+?}', re.DOTALL + re.MULTILINE)
    GLOSS_USE = re.compile(r'\\gref{(.+?)}{.+?}', re.DOTALL + re.MULTILINE)
    files = [(f, open(f, 'r').read()) for f in tex_filenames]
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


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
