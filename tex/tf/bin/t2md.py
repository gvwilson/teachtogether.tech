#!/usr/bin/env python

import sys
from TexSoup import TexSoup
from TexSoup.data import TexNode as Node
from TexSoup.utils import TokenWithPosition as Token


_w = sys.stdout.write


class Skip(object):

    def __init__(self):
        self.count = 0

    def inc(self, by):
        self.count += by

    def dec(self, by):
        self.count -= by

    def get(self):
        return self.count


SKIP = Skip()
    

def unknown(node, depth):
    print('!!' * depth, node.name)
    sys.exit(1)


def crossref(label):
    flavor, body = label.split(':')
    slug = body.split('-')[0]
    return f'{slug}.html#{label}'


#----------------------------------------


def _appref(node, depth):
    xref = crossref(node.args[0])
    _w(f'[Appendix FIXME]({xref})')
    SKIP.inc(1)
    return None


def _aside(node, depth):
    _w(f'<aside>\n')
    _w(f'#### ')
    dispatch(node.args[0])
    _w(f'\n')
    return f'</aside>\n\n'


def _chaplbl(node, depth):
    _w(f'# ')
    dispatch(node.args[0])
    _w(f' {{#{node.args[1]}}}\n')
    SKIP.inc(2)
    return None


def _chapref(node, depth):
    xref = crossref(node.args[0])
    _w(f'[Chapter FIXME]({xref})')
    SKIP.inc(1)
    return None


def _cite(node, depth):
    keys = [x.strip() for x in node.args[0].split(',')]
    cites = '[' + ','.join([f'[{k}](bib.html#{k})' for k in keys]) + ']'
    _w(cites)
    SKIP.inc(1)
    return None


def _description(node, depth):
    _w(f'<dl>\n')
    return f'</dl>\n'


def _dollar(node, depth):
    _w(f'{"==" * depth} dollar')
    return None


def _emph(node, depth):
    _w(f'*')
    dispatch(node.args[0])
    _w(f'*')
    SKIP.inc(1)
    return None


def _enumerate(node, depth):
    _w(f'<ol>\n')
    return f'</ol>\n'


def _gref(node, depth):
    _w(f'[')
    dispatch(node.args[1])
    _w(f'](gloss.html#{node.args[1]})')
    SKIP.inc(2)
    return None


def _hreffoot(node, depth):
    _w(f'[')
    dispatch(node.args[1])
    _w(f']({node.args[0]})')
    SKIP.inc(2)
    return None


def _item(node, depth):
    if len(node.args) == 0:
        _w(f'<li>')
    else:
        _w(f'<dt>')
        dispatch(node.args[0])
        _w(f'</dt>')
        SKIP.inc(1)
    return None


def _itemize(node, depth):
    _w(f'<ul>\n')
    return f'</ul>\n'


def _seclbl(node, depth):
    _w(f'## ')
    dispatch(node.args[0])
    _w(f' {{#{node.args[1]}}}\n')
    SKIP.inc(2)
    return None


def _secref(node, depth):
    xref = crossref(node.args[0])
    _w(f'[Section FIXME]({xref})')
    SKIP.inc(1)
    return None


def _subsection_star(node, depth):
    _w(f'### ')
    dispatch(node.args[0])
    _w(f'\n')
    SKIP.inc(1)
    return None


def _url(node, depth):
    _w(f'[{node.args[0]}]({node.args[0]})')
    SKIP.inc(1)
    return None


HANDLERS = {
    'appref' : _appref,
    'aside' : _aside,
    'chaplbl' : _chaplbl,
    'chapref' : _chapref,
    'cite' : _cite,
    'description' : _description,
    '$' : _dollar,
    'emph' : _emph,
    'enumerate' : _enumerate,
    'gref' : _gref,
    'hreffoot' : _hreffoot,
    'item' : _item,
    'itemize' : _itemize,
    'seclbl' : _seclbl,
    'secref' : _secref,
    'subsection*' : _subsection_star,
    'url' : _url
}


def recurse(node, depth=0):
    for child in node.contents:
        dispatch(child, depth+1)


def dispatch(node, depth=0):
    if type(node) == Node:
        handler = HANDLERS.get(node.name, unknown)
        after = handler(node, depth)
        recurse(node, depth)
        if after:
            _w(after)
    elif type(node) == Token:
        if SKIP.get() > 0:
            SKIP.dec(1)
        else:
            _w(node)
    elif type(node) == str:
        _w(node)
    else:
        print('Unknown node type', type(node), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    soup = TexSoup(open(sys.argv[1], 'r').read())
    recurse(soup)
