#!/usr/bin/env python

import sys


def main():
    for line in sys.stdin:
        line = line\
            .replace('input{pdf-settings}', 'input{html-settings}')\
            .replace('%%- ', '')
        sys.stdout.write(line)


if __name__ == '__main__':
    main()

