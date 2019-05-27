#!/usr/bin/env python

import sys
import re


FIGURE_PAT = re.compile(r'<embed src="figures/(.+?)\.pdf"')


def main():
    for line in sys.stdin:
        line = FIGURE_PAT.sub(r'<img src="figures/\1.svg"', line)
        sys.stdout.write(line)


if __name__ == '__main__':
    main()
