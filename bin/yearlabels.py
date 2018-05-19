#!/usr/bin/env python

import sys
import string
import bibtexparser

def mismatch(year, ident):
    if ident[-1] in string.ascii_lowercase:
        ident = ident[:-1]
    return not ident.endswith(year)

filename = sys.argv[1]
text = open(filename).read()
for (year, ident) in [(b['year'], b['ID']) for b in bibtexparser.loads(text).entries if mismatch(b['year'], b['ID'])]:
    print(year, ident)
