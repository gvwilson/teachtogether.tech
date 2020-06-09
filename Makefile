.PHONY : all check clean commands everything html once pages pdf settings spell words

# Commands
PANDOC=pandoc \
  --standalone \
  --css=assets/bootstrap.min.css \
  --css=assets/tango.css \
  --css=assets/book.css \
  --toc \
  --toc-depth=2 \
  --csl=chicago.csl

# Files
TEX=$(wildcard en/*.tex)
SRC=${TEX} $(wildcard en/*.bib) $(wildcard *.cls) $(wildcard *.csl)
HTML=docs/index.html
FIGURES_SRC=$(wildcard figures/*)
FIGURES_DST=$(patsubst %,docs/%,${FIGURES_SRC})
ASSETS_SRC=$(wildcard assets/*)
ASSETS_DST=$(patsubst %,docs/%,${ASSETS_SRC})

# Controls
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## html : generate HTML from LaTeX source.
html : ${HTML} ${FIGURES_DST} ${ASSETS_DST} docs/CNAME

# Generate HTML.
${HTML} : ${SRC} template.html bin/pre-pandoc.py bin/post-pandoc.py
	@mkdir -p docs
	bin/pre-pandoc.py < en/book.tex > temp.tex
	${PANDOC} --template=template.html --bibliography=book.bib --output=- temp.tex \
	| bin/post-pandoc.py \
	> ${HTML}
	rm temp.tex

# Copy figures.
docs/figures/% : figures/%
	@mkdir -p docs/figures
	@cp $< $@

# Copy assets.
docs/assets/% : assets/%
	@mkdir -p docs/assets
	@cp $< $@

# Copy CNAME file.
docs/CNAME : ./CNAME
	@mkdir -p docs
	@cp $< $@

## check : check internal consistency.
check : spell
	@python bin/check.py -b book.bib -f figures ${TEX}

## clean : clean up junk files.
clean :
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
	@find . -name .DS_Store -prune -exec rm -r "{}" \;

## settings : show settings.
settings :
	@echo TEX ${TEX}
	@echo SRC ${SRC}
	@echo HTML ${HTML}
	@echo FIGURES_SRC ${FIGURES_SRC}
	@echo FIGURES_DST ${FIGURES_DST}
