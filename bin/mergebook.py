#!/usr/bin/env python

import sys
import os
import re


HEADER = '''---
layout: chapter
title: "{title}"
---
<h1>{title}</h1>'''

IGNORES = {'settings', 'macros', 'frontmatter'}

HEADINGS = (('h3', 'h4'), ('h2', 'h3'), ('h1', 'h2'))


def main(title, bookFile, outputDir):
    order = readOrder(bookFile)
    print(HEADER.format(title=title))
    for stem in order:
        process(os.path.join(outputDir, stem + '.html'))


def readOrder(bookFile):
    with open(bookFile, 'r') as reader:
        data = reader.read()
    pat = re.compile(r'\\(input|bibliography){([^}]+)}')
    result = [m[1] for m in pat.findall(data) if m[1] not in IGNORES]
    return result


def process(filename):
    with open(filename, 'r') as reader:
        data = reader.read()
    data = data[data.index('<h1'):]
    data = fixInternal.pattern.sub(fixInternal, data)
    for (src, dst) in HEADINGS:
        data = data.replace(src, dst)
    print(data)


def fixInternal(match):
    stem = match.group(1)
    anchor = match.group(2)
    if anchor:
        target = anchor
    else:
        target = 's:{}'.format(stem)
    return 'href="{}"'.format(target)
fixInternal.pattern = re.compile(r'href="\./(.+?)\.html((#[^"]+)?)"')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.stderr.write('Usage: mergebook title /path/to/book.tex /path/to/output_directory')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
