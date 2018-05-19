#!/usr/bin/env python

'''Bibliography post-processing.'''

import sys
import re
import bibtexparser


def keySub(match):
    key = match.group(1)
    entry = ENTRIES[key]
    label = None

    if 'link' in entry:
        label = entry['link']
    elif ('howpublished' in entry) and entry['howpublished'].startswith('http'):
        label = entry['howpublished']

    if label is None:
        label = key
    else:
        label = '<a href="{}">{}</a>'.format(label, key)

    return '<p id="' + key + '">[<strong>' + label + '</strong>]'

keySub.pattern = re.compile(r'^<p>\[([^]]+)\]')


def main(bibfile):
    global ENTRIES
    with open(bibfile, 'r') as reader:
        text = reader.read()
    ENTRIES = bibtexparser.loads(text).entries
    ENTRIES = {e['ID'] : e for e in ENTRIES}
    for line in sys.stdin:
        line = keySub.pattern.sub(keySub, line)
        sys.stdout.write(line)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: bbl2html-post /path/to/bibfile')
        sys.exit(1)
    main(sys.argv[1])
