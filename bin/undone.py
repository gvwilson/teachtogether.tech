#!/usr/bin/env python

import sys
import bibtexparser

filename = sys.argv[1]
text = open(filename).read()
bib = bibtexparser.loads(text).entries
noteless = [b for b in bib if ('note' not in b)]
print('{} ({:.1f}%)'.format(len(noteless), 100.0 * len(noteless) / len(bib)))
print('\n'.join([b['ID'] for b in noteless]))
