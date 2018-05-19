#!/usr/bin/env python

'''Post-processing for LaTeX-to-HTML conversion.'''


import sys
import re


def glossrefSub(match):
    link = match.group(1)
    return '<a class="glossref" href="{}">'.format(link)
glossrefSub.pattern = re.compile(r'<a href="(\./gloss.html#[^"]+)">')


def glossdefTermSub(match):
    text = match.group(1)
    return '<dt>{}:</dt>'.format(text)
glossdefTermSub.pattern = re.compile(r'<dt>([^:]+):</dt>')


def glossdefDefSub(match):
    label = match.group(1)
    return '<dd id="{}"><p>'.format(label)
glossdefDefSub.pattern = re.compile(r'<dd><p><span id="([^"]+)" label="[^"]+">\[[^+]+\]</span> ')


def alignSub(match):
    alignment = match.group(1)
    return '<td style="text-align: {}">'.format(alignment)
alignSub.pattern = re.compile(r'<td align="([^"]+)">')


def listparSub(match):
    return '<li>{}'.format(match.group(1))
listparSub.pattern = re.compile(r'^<li><p>(.+)</p>')


def figembedSub(match):
    stem = match.group(1)
    return '<img src="./fig/{}.svg" />'.format(stem)
figembedSub.pattern = re.compile(r'<embed\s*src=".+/(.+?)\.pdf"\s*/>')


def figcaptionSub(match):
    caption = match.group(1)
    label = match.group(2)
    return '<figcaption id="{}">{}</figcaption>'.format(label, caption)
figcaptionSub.pattern = re.compile(r'<figcaption>(.+?)<span label="(.+?)"></span></figcaption>')


PATTERNS = (glossrefSub, glossdefTermSub, glossdefDefSub,
            alignSub, listparSub,
            figembedSub, figcaptionSub)

STRINGS = (('<img src="../docs/fig/', '<img src="./fig/'),
           ('"unnumbered unnumbered"', '"unnumbered"'),
           ('<span class="math inline">[</span>', '['),
           ('<span class="math inline">]</span>', ']'))


def hrefSub(match):
    return 'href="{}"'.format(match.group(2))
hrefSub.pattern = re.compile(r'href="(\./)?[a-z]+\.html(#[^"]+)"')


def copyFile(filename):
    with open(filename, 'r') as reader:
        copying = False
        for line in reader:
            if 'h1' in line:
                copying = True
                line = line.replace('h1', 'h2')
            if copying:
                sys.stdout.write(line)


def main(bibFile=None, glossFile=None):
    for line in sys.stdin:
        for func in PATTERNS:
            line = func.pattern.sub(func, line)
        for (src, dst) in STRINGS:
            line = line.replace(src, dst)
        if bibFile:
            line = hrefSub.pattern.sub(hrefSub, line)
        sys.stdout.write(line)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        sys.stderr.write('Usage: ltx2html-post [bibFile glossFile]\n')
        sys.exit(1)
