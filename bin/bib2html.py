#!/usr/bin/env python

'''
Convert a BibTeX file to HTML.  This only handles the subset
of BibTeX used in this book's bibliography.
'''

import sys
import bibtexparser


def _c(text):
    '''
    Clean up LaTeXisms in strings.
    '''
    return text.replace('{', '').replace('}', '')


def _authors(entry):
    '''
    Format the author names in an entry.
    '''
    if 'author' in entry:
        names = entry['author']
        suffix = ''
    elif 'editor' in entry:
        names = entry['editor']
        suffix = ' (eds.)'
    names = names.split(' and ')
    if len(names) == 0:
        raise Exception('NO AUTHOR')
    elif len(names) == 1:
        return _c(f'{names[0]}{suffix}')
    elif len(names) == 2:
        return _c(f'{names[0]} and {names[1]}{suffix}')
    else:
        return _c(f'{", ".join(names[:-1])}, and {names[-1]}{suffix}')


def _booktitle(entry):
    '''
    Format the book title in an entry.
    '''
    if 'link' in entry:
        return _c(f'<em><a href="{entry["link"]}">{entry["booktitle"]}</a></em>')
    else:
        return _c(f'<em>{entry["booktitle"]}</em>')


def _details(entry):
    '''
    Format publication details: year plus optional month, volume, number.
    '''
    result = entry['year']
    if 'month' in entry:
        result = f'{entry["month"]} {result}'
    if 'volume' in entry:
        if 'number' in entry:
            extra = f'{_c(entry["volume"])}({entry["number"]})'
        else:
            extra = _c(entry['volume'])
        result = f'{extra}, {result}'
    return result


def _doi(entry):
    '''
    Format a DOI in an entry.
    '''
    if 'doi' not in entry:
        return ''
    return f'doi:{entry["doi"]}'


def _howpublished(entry):
    '''
    Format the 'howpublished' of a miscellaneous entry (possibly as a link).
    '''
    how = entry['howpublished']
    if how.startswith('\\url{'):
        how = how.replace('\\url{', '')[:-1]
    if how.startswith('http'):
        how = f'<a href="{how}">{how}</a>'
    return _c(how)

    
def _isbn(entry):
    '''
    Format an ISBN in an entry.
    '''
    if 'isbn' not in entry:
        return ''
    return entry['isbn']


def _journal(entry):
    '''
    Format a journal title.
    '''
    return _c(f'<em>{entry["journal"]}</em>')

    
def _key(entry):
    '''
    Format the citation key, including a linkable ID.
    '''
    return f'<dt id="ref-{entry["ID"]}">{entry["ID"]}</dt>'


def _note(entry):
    '''
    Format an entry's bibliographic note.
    '''
    return _c(f'<em>{entry["note"]}</em>')


def _papertitle(entry):
    '''
    Format the title of a paper.
    '''
    if 'url' in entry:
        return _c(f'"<a href="{entry["url"]}">{entry["title"]}</a>"')
    else:
        return _c(f'"{entry["title"]}"')

    
def _publisher(entry):
    '''
    Format the publisher in an entry.
    '''
    return _c(entry['publisher'])


def _title(entry):
    '''
    Format the book title in an entry.
    '''
    if 'link' in entry:
        return _c(f'<em><a href="{entry["link"]}">{entry["title"]}</a></em>')
    else:
        return _c(f'<em>{entry["title"]}</em>')


def output(text):
    '''
    Display text with simple LaTeXisms removed.
    '''
    text = text.replace(r'\&', '&').replace(r'\ ', ' ')
    sys.stdout.write(text)


# Handlers for various entry types.
# Each element is either a function (always called) or a (prefix, function) pair.
# In the latter case, the prefix is only displayed if the function returns something.
HANDLERS = {
    'article' : [
        _key, '<dd>',
        _authors, ':', ' ',
        _papertitle, '.', ' ',
        _journal, (', ', _details), (', ', _doi), '.', ' ',
        _note,
        '</dd>'
    ],
    'book' : [
        _key, '<dd>',
        _authors, ': ', ' ',
        _title, '.', ' ',
        _publisher, (', ', _details), (', ', _isbn), '.', ' ',
        _note,
        '</dd>'
    ],
    'incollection' : [
        _key, '<dd>',
        _authors, ':', ' ',
        _papertitle, '.', ' ',
        'In ', _booktitle, ',', ' ',
        _publisher, (', ', _details), (', ', _doi), '.', ' ',
        _note,
        '</dd>'
    ],
    'inproceedings' : [
        _key, '<dd>',
        _authors, ':', ' ',
        _papertitle, '.', ' ',
        'In ', _booktitle, (', ', _details), (', ', _doi), '.', ' ',
        _note,
        '</dd>'
    ],
    'misc' : [
        _key, '<dd>',
        _authors, ':', ' ',
        _papertitle, '.', ' ',
        _howpublished, (', ', _details), (', ', _doi), '.', ' ',
        _note,
        '</dd>'
    ]
}

def main():
    '''
    Main driver: read bibliography from stdin, format and print the entries to stdout.
    '''
    source = bibtexparser.loads(sys.stdin.read()).entries
    try:
        print('<dl class="bibliography">')
        for entry in source:
            for h in HANDLERS[entry['ENTRYTYPE']]:
                if type(h) is tuple:
                    prefix, func = h
                    text = func(entry)
                    if text:
                        output(prefix + text)
                elif callable(h):
                    output(h(entry))
                else:
                    output(h)
            output('\n\n')
        print('</dl>')
    except Exception as e:
        sys.stderr.write('\nERROR {}:: {}\n'.format(str(e), str(entry)))


# Command-line launch.
if __name__ == '__main__':
    main()
