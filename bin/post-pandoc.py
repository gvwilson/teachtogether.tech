#!/usr/bin/env python

import sys
import re


FIGURE_PAT = re.compile(r'<embed src="figures/(.+?)\.pdf"')
BIB_REF_PAT = re.compile(r'<span\s+class="citation"\s+data-cites="(.+?)">.+?</span>')
BIB_ENTRY_PAT = re.compile(r'<div\s+id="ref-(.+?)">\n<p>', re.MULTILINE)

EMPTY_ROW_EVEN = '''<tr class="even">
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
'''

EMPTY_ROW_ODD = '''<tr class="odd">
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
'''

def main():
    text = sys.stdin.read()\
        .replace('<table>', '<table class="table table-striped">')\
        .replace(EMPTY_ROW_EVEN, '')\
        .replace(EMPTY_ROW_ODD, '')
    text = FIGURE_PAT.sub(r'<img src="figures/\1.svg"', text)
    text = BIB_REF_PAT.sub(replace_ref, text)
    text = BIB_ENTRY_PAT.sub(replace_entry, text)
    text = fix_footnotes(text)
    sys.stdout.write(text)


def replace_ref(refs):
    return '[' + ','.join(f'<a class="cite" href="#ref-{r}">{r}</a>' for r in refs.group(1).split()) + ']'


def replace_entry(entry):
    entry = entry.group(1)
    return f'<div id="ref-{entry}">\n<p><strong>[{entry}]</strong> '


def fix_footnotes(text):
    FOOTNOTE_REF = re.compile(r'<a\s+href="#fn(\d+?)"\s+class="footnote-ref"\s+id="fnref\d+?"\s+role="doc-noteref"><sup>\d+</sup></a>')
    FOOTNOTE_DEF = re.compile(r'<li\s+id="fn(\d+?)"\s+role="doc-endnote">(.+?)</li>')
    BACKREF = re.compile('<a\s+href="#fnref(\d+?)"\s+class="footnote-back"\s+role="doc-backlink">')

    actual = {original:(i+1) for (i, original) in list(enumerate(FOOTNOTE_REF.findall(text)))}

    def replace_ref(match):
        key = match.group(1)
        return f'<a href="#fn{actual[key]}" class="footnote-ref" id="fnref{actual[key]}" role="doc-noteref"><sup>{actual[key]}</sup></a>'

    def replace_def(match):
        key, body = match.group(1), match.group(2)
        result = ''
        if key in actual:
            result = f'<li id="fn{actual[key]}" role="doc-endnote">{body}</li>'
        return result

    def replace_backref(match):
        key = match.group(1)
        return f'<a href="#fnref{actual[key]}" class="footnote-back" role="doc-backlink">'
            
    text = FOOTNOTE_REF.sub(replace_ref, text)
    text = FOOTNOTE_DEF.sub(replace_def, text)
    text = BACKREF.sub(replace_backref, text)

    return text

if __name__ == '__main__':
    main()
