PYTHON ?= python
LATEXMK ?= latexmk
.PHONY: all figures pdf clean
all: figures pdf
figures:
	cd figures && $(PYTHON) gen.py
pdf:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex
clean:
	$(LATEXMK) -c main.tex || true
	rm -f main.bbl main.run.xml
