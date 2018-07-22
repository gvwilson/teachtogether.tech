# Tools.
JEKYLL=jekyll
LATEX=pdflatex
BIBTEX=bibtex
PANDOC=pandoc
PANDOC_FLAGS=--from=gfm --to=latex

# Settings.
CHAPTERS_MD=$(filter-out _chapters_en/bib.md,$(wildcard _chapters_en/*.md))
CHAPTERS_TEX=$(patsubst _chapters_en/%.md,tex_en/inc/%.tex,${CHAPTERS_MD})

# Controls
.PHONY : commands serve site bib crossref clean
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' Makefile | sed -e 's/## //g'

## serve    : run a local server.
serve :
	${JEKYLL} serve -I

## site     : build files but do not run a server.
site :
	${JEKYLL} build

## pdf      : build PDF version of book.
pdf : tex_en/t3.pdf

## tex      : generate LaTeX for book, but don't compile to PDF.
tex : ${CHAPTERS_TEX}

tex_en/t3.pdf : ${CHAPTERS_TEX} tex_en/t3.bib
	@cd tex_en \
	&& ${LATEX} t3 \
	&& ${BIBTEX} t3 \
	&& ${LATEX} t3 \
	&& ${LATEX} t3 \
	&& ${LATEX} t3

tex_en/inc/%.tex : _chapters_en/%.md bin/texpre.py bin/texpost.py _includes/links.md
	mkdir -p tex_en/inc && \
	cat $< \
	| bin/texpre.py \
	| ${PANDOC} ${PANDOC_FLAGS} -o - \
	| bin/texpost.py _includes/links.md \
	> $@

tex_en/t3.bib : files/t3.bib
	cp $< $@

## bib      : rebuild Markdown bibliography from BibTeX source.
bib : _chapters_en/bib.md

_chapters_en/bib.md : files/t3.bib bin/bib2md.py
	bin/bib2md.py < $< > $@

## crossref : rebuild cross-reference file.
crossref : files/crossref.js

files/crossref.js : bin/crossref.py _config.yml ${CHAPTERS_MD}
	bin/crossref.py < _config.yml > files/crossref.js

## clean    : clean up junk files.
clean :
	@rm -rf _site tex_en/t3.bib tex_en/inc */*.aux */*.bbl */*.blg */*.log */*.out */*.toc
	@find . -name .DS_Store -exec rm {} \;
	@find . -name '*~' -exec rm {} \;
