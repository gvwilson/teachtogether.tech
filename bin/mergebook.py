#!/usr/bin/env python

import sys
import os
import re
import yaml


def main(configPath, crossrefPath, rootDir):
    slugs, markerStart, markerEnd = readConfig(configPath)
    before, body, after = getBody(os.path.join(rootDir, 'index.html'), markerStart, markerEnd)
    print(before)
    print(body)
    slugPaths = [(s, os.path.join(rootDir, s, 'index.html')) for s in slugs]
    for (slug, path) in slugPaths:
        _, body, _ = getBody(path, markerStart, markerEnd)
        body = body.replace('<h1', '<h1 id="s:{}"'.format(slug))
        print(body)
    print(after)


def readConfig(configPath):
    with open(configPath, 'r') as reader:
        config = yaml.load(reader)
    slugs = [p.strip('/') for p in config['toc']['lessons'] + config['toc']['extras']]
    markerStart = config['marker']['start']
    markerEnd = config['marker']['end']
    return slugs, markerStart, markerEnd


def getBody(path, markerStart, markerEnd):
    with open(path, 'r') as reader:
        text = reader.read()
        start = text.find(markerStart) + len(markerStart)
        end = text.find(markerEnd, start)
        return text[:start], text[start:end], text[end:]


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.stderr.write('Usage: mergebook /path/to/config /path/to/crossref /path/to/site\n')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
