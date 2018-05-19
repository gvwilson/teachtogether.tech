#!/usr/bin/env python

import sys
import bibtexparser

filename = sys.argv[1]
text = open(filename).read()
bib = bibtexparser.loads(text).entries
titles = [b['title'] for b in bib if 'title' in b]
titles = [(len(t), t) for t in titles]
titles.sort()
for (_, t) in titles:
    print(t)
