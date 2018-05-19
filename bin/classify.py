#!/usr/bin/env python

import sys
import bibtexparser
from collections import Counter

filename = sys.argv[1]
text = open(filename).read()
bib = bibtexparser.loads(text).entries
counts = Counter([b['ENTRYTYPE'] for b in bib])
print('{:4} total'.format(len(bib)))
for k in sorted(counts.keys()):
    print('{:4} {}'.format(counts[k], k))
