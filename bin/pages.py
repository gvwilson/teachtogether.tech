#!/usr/bin/env python

import sys
import re

PAGES_PAT = re.compile(r'^ \[(\d+)', re.MULTILINE)

INTERESTING_PAT = re.compile(r'\{chapter\}|References|Index')
CHAPTER_PAT = re.compile(r'\{chapter\}\{\\numberline\s*\{\\bfseries\s*(.+?)~(.+?)\}(.+?)\}\{(.+?)\}')
OTHER_PAT = re.compile(r'\{\\bfseries\s+(References|Index)\}\{(\d+)\}')

def main(log, toc):
    num_pages = read_log(log)
    chapters = read_chapters(toc, num_pages)
    for (kind, label, title, start, num) in chapters:
        print(f'{kind:<8} {label:>2} {start:>3} ({num:>3}) {title}')


def read_log(log):
    with open(log, 'r') as reader:
        text = reader.read()
    all_pages = PAGES_PAT.findall(text)
    return int(all_pages[-1])


def _extract_chapters(line):
    match = CHAPTER_PAT.search(line)
    if match:
        return [match.group(1), match.group(2), match.group(3), int(match.group(4))]
    match = OTHER_PAT.search(line)
    return ['Other', '', match.group(1), int(match.group(2))]

def read_chapters(toc, num_pages):
    with open(toc, 'r') as reader:
        all_lines = [line for line in reader.readlines() if INTERESTING_PAT.search(line)]
    matched = [_extract_chapters(line) for line in all_lines]

    for i in range(1, len(matched)):
        matched[i-1].append(matched[i][3] - matched[i-1][3])
    matched[-1].append(num_pages - matched[-1][3])

    return matched


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: pages book.log book.toc', file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
