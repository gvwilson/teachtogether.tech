#!/usr/bin/env python

import sys
import os


IGNORES = ['CNAME', '_config.yml', 'favicon.ico', 'index.html', '.jekyll-metadata']
SUFFIXES = ['epub', 'html', 'mobi', 'pdf']


def main(stem, actual_dir, expected_files):
    ignores = IGNORES + [stem + '.' + s for s in SUFFIXES]
    actual = [os.path.join(actual_dir, f) for f in os.listdir(actual_dir) if f not in ignores]
    actual = set([f for f in actual if os.path.isfile(f)])
    expected = set(expected_files)
    report('Missing', expected - actual)
    report('Extra', actual - expected)


def report(title, filenames):
    if filenames:
        print(title)
        for f in sorted(filenames):
            print('  {}'.format(f))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: mismatch stem output_dir expected_files...')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
