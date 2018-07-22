# Tools.
JEKYLL=jekyll
LATEX=pdflatex
BIBTEX=bibtex
PANDOC=pandoc
PANDOC_FLAGS=--from=gfm --to=latex
REPO=http://github.com/gvwilson/teachtogether.tech

# Settings.
CHAPTERS_MD=$(filter-out _chapters_en/bib.md,$(wildcard _chapters_en/*.md))
CHAPTERS_TEX=$(patsubst _chapters_en/%.md,tex_en/inc/%.tex,${CHAPTERS_MD})

# Controls
.PHONY : commands serve site bib crossref clean
all : commands

## commands   : show all commands.
commands :
	@grep -h -E '^##' Makefile | sed -e 's/## //g'

## serve      : run a local server.
serve :
	${JEKYLL} serve -I

## site       : build files but do not run a server.
site :
	${JEKYLL} build

## pdf        : build PDF version of book.
pdf : tex_en/t3.pdf

## tex        : generate LaTeX for book, but don't compile to PDF.
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

## bib        : rebuild Markdown bibliography from BibTeX source.
bib : _chapters_en/bib.md

_chapters_en/bib.md : files/t3.bib bin/bib2md.py
	bin/bib2md.py < $< > $@

## crossref   : rebuild cross-reference file.
crossref : files/crossref.js

files/crossref.js : bin/crossref.py _config.yml ${CHAPTERS_MD}
	bin/crossref.py < _config.yml > files/crossref.js

## ----------------------------------------

## authors    : list all authors.
authors :
	@bin/authors.py files/t3.bib

## missing    : list all missing bibliography entries.
missing :
	@bin/checkcites.py --missing files/t3.bib ${CHAPTERS_TEX}

## publishers : list all publishers.
publishers :
	@bin/fields.py files/t3.bib publisher

## unused     : list all unused bibliography entries.
unused :
	@bin/checkcites.py --unused files/t3.bib ${CHAPTERS_TEX}

## years      : CSV histogram of publication years.
years :
	@bin/years.py files/t3.bib

## ----------------------------------------

## exercises  : count exercises per chapter.
exercises :
	@bin/exercises.py tex_en/t3.tex

## issues     : create single-page view of all GitHub issues.
issues :
	@bin/issues.py ${REPO} | ${PANDOC} -o issues.html -

## labels     : make sure all labels conform to standards.
labels :
	@bin/checklabels.py ${CHAPTERS_TEX}

## pages      : count pages per chapter.
pages : tex_en/t3.toc
	@bin/pages.py < tex_en/t3.toc

## spelling   : check spelling.
spelling :
	@grep bibnote files/t3.bib \
	| cat - ${CHAPTERS_MD} \
	| aspell --mode=tex list \
	| sort \
	| uniq \
	| comm -2 -3 - words.txt

## words      : count words per chapter.
words :
	@wc -w ${CHAPTERS_MD} | sort -n -r

## ----------------------------------------

## nonascii   : look for non-ASCII characters.
nonascii :
	@bin/nonascii.py ${CHAPTERS_MD}

## clean      : clean up junk files.
clean :
	@rm -rf _site tex_en/t3.bib tex_en/inc */*.aux */*.bbl */*.blg */*.log */*.out */*.toc
	@find . -name .DS_Store -exec rm {} \;
	@find . -name '*~' -exec rm {} \;

## settings   : show macro values.
settings :
	@echo 'JEKYLL = ' ${JEKYLL}
	@echo 'LATEX = ' ${LATEX}
	@echo 'BIBTEX = ' ${BIBTEX}
	@echo 'PANDOC = ' ${PANDOC}
	@echo 'PANDOC_FLAGS = ' ${PANDOC_FLAGS}
	@echo 'REPO = ' ${REPO}
	@echo 'CHAPTERS_MD = ' ${CHAPTERS_MD}
	@echo 'CHAPTERS_TEX = ' ${CHAPTERS_TEX}
