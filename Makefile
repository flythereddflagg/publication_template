CC = pdflatex
BIB = bibtex

MAIN = main
PART = part

SRC = ./tex/$(MAIN)


all: md_to_tex tex_to_pdf clean-meta display

md_to_tex:
	python convert_to_tex.py

tex_to_pdf:
	$(CC) $(SRC).tex
	$(BIB) $(MAIN)
	$(CC) $(SRC).tex
	$(CC) $(SRC).tex

display:
	display_pdf.bat $(MAIN)

clean-meta:
	del *.dvi
	del *.aux
	del *.bbl
	del *.blg
	del *.brf
	del *.out
	del *.toc

clean:
	del *.pdf
	del *.log
	del *.dvi
	del *.aux
	del *.bbl
	del *.blg
	del *.brf
	del *.out
	del *.toc
	del .\tex\section*