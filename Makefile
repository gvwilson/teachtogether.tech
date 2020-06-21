.PHONY : all check clean commands everything html once pages pdf settings spell words

# Files
TEX=$(wildcard en/*.tex)
SRC=${TEX} $(wildcard en/*.bib) $(wildcard *.cls) $(wildcard *.csl)
HTML=docs/index.html
FIGURES_SRC=$(wildcard figures/*)
FIGURES_DST=$(patsubst %,docs/%,${FIGURES_SRC})
STATIC_SRC=$(wildcard static/*)
STATIC_DST=$(patsubst %,docs/%,${STATIC_SRC})

# Controls
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## html : generate HTML from LaTeX source.
html : ${HTML} ${FIGURES_DST} ${STATIC_DST} docs/CNAME

# Generate HTML.
${HTML} : ${SRC} template.html bin/pre-pandoc.py bin/post-pandoc.py
	@make -C en -f html.mk html

# Copy figures.
docs/figures/% : figures/%
	@mkdir -p docs/figures
	@cp $< $@

# Copy static.
docs/static/% : static/%
	@mkdir -p docs/static
	@cp $< $@

# Copy CNAME file.
docs/CNAME : ./CNAME
	@mkdir -p docs
	@cp $< $@

## clean : clean up junk files.
clean :
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
	@find . -name .DS_Store -prune -exec rm -r "{}" \;
	@make -C en clean
	@make -C es clean
	@make -C kr clean

## settings : show settings.
settings :
	@echo TEX ${TEX}
	@echo SRC ${SRC}
	@echo HTML ${HTML}
	@echo FIGURES_SRC ${FIGURES_SRC}
	@echo FIGURES_DST ${FIGURES_DST}
