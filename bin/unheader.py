#!/usr/bin/env python

import sys


doc = sys.stdin.read()
doc = doc.split('---\n', 2)[2]
sys.stdout.write(doc)
