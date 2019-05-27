#!/usr/bin/env python

import sys
import re


FIGURE_PAT = re.compile(r'<embed src="figures/(.+?)\.pdf"')
BIB_REF_PAT = re.compile(r'<span\s+class="citation"\s+data-cites="(.+?)">.+?</span>')
BIB_ENTRY_PAT = re.compile(r'<div\s+id="ref-(.+?)">\n<p>', re.MULTILINE)


def main():
    text = sys.stdin.read()
    text = FIGURE_PAT.sub(r'<img src="figures/\1.svg"', text)
    text = BIB_REF_PAT.sub(replace_ref, text)
    text = BIB_ENTRY_PAT.sub(replace_entry, text)
    sys.stdout.write(text)


def replace_ref(refs):
    return '[' + ','.join(f'<a class="cite" href="#ref-{r}">{r}</a>' for r in refs.group(1).split()) + ']'


def replace_entry(entry):
    entry = entry.group(1)
    return f'<div id="ref-{entry}">\n<p><strong>[{entry}]</strong> '


if __name__ == '__main__':
    main()
