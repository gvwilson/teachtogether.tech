#!/usr/bin/env python

import sys
import os
import re
import getopt


def main(args):
    bib_filename, fig_dir, tex_filenames = parse_args(args)
    tex_files = [(f, open(f, 'r').read()) for f in tex_filenames]
    check_gloss(tex_files)
    check_figs(fig_dir, tex_files)
    bib_keys = check_bib_keys(bib_filename)
    check_bib_cites(bib_keys, tex_files)


def parse_args(args):
    bib_filename = None
    fig_dir = None
    options, tex_filenames = getopt.getopt(args, 'b:f:')
    for (opt, arg) in options:
        if opt == '-b':
            bib_filename = arg
        elif opt == '-f':
            fig_dir = arg
        else:
            fail(f'Unknown option "{opt}"')
    fail('Bibliography filename not given (use -b)', not bib_filename)
    fail('Figure director not given (use -f)', not fig_dir)
    return bib_filename, fig_dir, tex_filenames


def check_gloss(files):
    GLOSS_DEF = re.compile(r'\\gitem{(.+?)}', re.DOTALL + re.MULTILINE)
    GLOSS_USE = re.compile(r'\\gref[^}]*?{(.+?)}', re.DOTALL + re.MULTILINE)
    defined = find_all(GLOSS_DEF, files)
    used = find_all(GLOSS_USE, files)
    report('Glossary', 'missing', used - defined)
    report('Glossary', 'unused', defined - used)


def check_figs(fig_dir, files):
    FIG_USE = re.compile(r'\\(figimg|figpdf|figpdfhere)\{(.+?)\}\{.+?\}\{.+?\}')
    used = {os.path.basename(path) for (macro, path) in find_all(FIG_USE, files)}
    exists = set(os.listdir(fig_dir))
    report('Figures', 'missing', used - exists)
    used_stems = {os.path.splitext(f)[0] for f in used}
    exists_stems = {os.path.splitext(f)[0] for f in exists}
    report('Figures', 'unused', exists_stems - used_stems)


def check_bib_keys(bib_filename):
    BIB_KEY = re.compile(r'^@[a-z]+?{(\w+?),$', re.DOTALL + re.MULTILINE)
    KEY_PAT = re.compile(r'[A-Z][A-Za-z]{1,3}[0-9]{4}')
    text = open(bib_filename, 'r').read()
    keys = set(BIB_KEY.findall(text))
    mismatch = [k for k in keys if not KEY_PAT.match(k)]
    report('Bibliography', 'bad keys', mismatch)
    return keys


def check_bib_cites(bib_keys, files):
    CITE_PAT = re.compile(r'\\cite{(.+?)}')
    raw_cites = [c.split(',') for c in find_all(CITE_PAT, files)]
    all_cites = {item for sublist in raw_cites for item in sublist}
    report('Bibliography', 'missing', all_cites - bib_keys)
    report('Bibliography', 'unused', bib_keys - all_cites)


def find_all(pattern, files):
    result = set()
    [result.update(pattern.findall(text)) for (name, text) in files]
    return result


def report(major, minor, values):
    if values:
        print(f'{major} {minor}')
        for v in sorted(values):
            print(f'  {v}')


def fail(msg, failure=True):
    if failure:
        print(msg, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
