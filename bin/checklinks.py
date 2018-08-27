#!/usr/bin/env python

import sys
import re

from texpost import readLinks

LINK_PAT = re.compile(r'\[([^\]]+?)\]\[([^\]]+?)\]', re.DOTALL)


def main(linksPath, filenames):
    links = readLinks(linksPath)
    links = {k:False for k in links}
    for f in filenames:
        with open(f, 'r') as reader:
            doc = reader.read()
            for m in LINK_PAT.finditer(doc):
                alias = m.group(2)
                if alias not in links:
                    print('{}: [{}][{}]'.format(f, m.group(1), alias))
                else:
                    links[alias] = True
    unused = [k for k in links if not links[k]]
    if unused:
        unused.sort()
        print('unused:')
        for k in unused:
            print('    {}'.format(k))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])

