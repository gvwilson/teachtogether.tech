#!/usr/bin/env python

import sys
import re

PAGES_PAT = re.compile(r'^ \[(\d+)', re.MULTILINE)
CHAPTER_PAT = re.compile(r'\{chapter\}\{\\numberline\s*\{\\bfseries\s*(.+?)~(.+?)\}(.+?)\}\{(.+?)\}')

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


def read_chapters(toc, num_pages):
    with open(toc, 'r') as reader:
        matches = [CHAPTER_PAT.search(line) for line in reader]

    chapters = [[m.group(1), m.group(2), m.group(3), int(m.group(4))] for m in matches if m]

    for i in range(1, len(chapters)):
        chapters[i-1].append(chapters[i][3] - chapters[i-1][3])
    chapters[-1].append(num_pages - chapters[-1][3])

    return chapters


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: pages book.log book.toc', file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
