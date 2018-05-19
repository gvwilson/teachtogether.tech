#!/usr/bin/env python

import sys
import os
import bibtexparser


def main(dirpath, bibfile):
    text = open(bibfile).read()
    entries = bibtexparser.loads(text).entries
    entries = [b for b in entries if ('local' in b) and (b['ENTRYTYPE'] not in {'book'})]
    expected = set([b['local'] for b in entries])
    files = set([f for f in os.listdir(dirpath) if f.endswith('.pdf')])
    report('Missing', expected - files)
    report('Extra', files - expected)


def report(title, items):
    if items:
        print(title)
        for i in sorted(items):
            print('  {}'.format(i))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: bibfiles /path/to/files /path/to/bibliography')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
