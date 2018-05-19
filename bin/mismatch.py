#!/usr/bin/env python

import sys
import os


IGNORES = {'CNAME', '_config.yml', 'favicon.ico', 'index.html'}


def main(actual_dir, expected_files):
    actual = [os.path.join(actual_dir, f) for f in os.listdir(actual_dir) if f not in IGNORES]
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
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: dangling output_dir expected_files...')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2:])
