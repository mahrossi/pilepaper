.PHONY: all
all: text.pdf 
%.pdf: %.tex %.bbl
	while (pdflatex $< ; \
	grep -q "Rerun to get cross" $*.log ) do true ; \
	done
%.bbl: %.tex biblio.bib
	pdflatex $<
	bibtex $*

