# Build the flagship preprint.
#   make figures   regenerate all plots (matplotlib -> figures/out/*.pdf,*.png)
#   make pdf       compile main.tex -> main.pdf (latexmk)
#   make all       figures then pdf
#   make clean     remove LaTeX aux files (keeps main.pdf and figures/out)

PYTHON ?= python
LATEXMK ?= latexmk

.PHONY: all figures pdf clean veryclean

all: figures pdf

figures:
	cd figures && $(PYTHON) gen_figures.py

pdf:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	$(LATEXMK) -c main.tex || true
	rm -f main.bbl main.run.xml

veryclean: clean
	$(LATEXMK) -C main.tex || true
	rm -f figures/out/*.pdf figures/out/*.png
