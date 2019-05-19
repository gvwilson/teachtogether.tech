#!/usr/bin/env python

from TexSoup import TexSoup
from TexSoup.data import TexNode as Node
from TexSoup.utils import TokenWithPosition as Token


def _UNKNOWN(node, depth):
    print('--' * depth, node.name)


def _appref(node, depth):
    print(f'{"==" * depth} appref {node.args[0]}')


def _aside(node, depth):
    print(f'{"==" * depth} aside {node.args[0]}')


def _chaplbl(node, depth):
    print(f'{"==" * depth} chaplbl {node.args[0]} {node.args[1]}')


def _cite(node, depth):
    print(f'{"==" * depth} cite {node.args[0]}')


def _gref(node, depth):
    print(f'{"==" * depth} gref {node.args[0]} {node.args[1]}')


def _hreffoot(node, depth):
    print(f'{"==" * depth} hreffoot {node.args[0]} {node.args[1]}')


def _seclbl(node, depth):
    print(f'{"==" * depth} seclbl {node.args[0]} {node.args[1]}')


def _secref(node, depth):
    print(f'{"==" * depth} secref {node.args[0]}')


def _url(node, depth):
    print(f'{"==" * depth} url {node.args[0]}')


HANDLERS = {
    'appref' : _appref,
    'aside' : _aside,
    'chaplbl' : _chaplbl,
    'cite' : _cite,
    'gref' : _gref,
    'hreffoot' : _hreffoot,
    'seclbl' : _seclbl,
    'secref' : _secref,
    'url' : _url
}


def process(node, depth=0):
    if type(node) == Token:
        print('TOKEN """{}"""'.format(node))
    elif type(node) == Node:
        print('NODE')
        handler = HANDLERS.get(node.name, _UNKNOWN)
        handler(node, depth)
        for child in node.contents:
            process(child, depth+1)


if __name__ == '__main__':
    soup = TexSoup(open('intro.tex', 'r').read())
    process(soup)

