# this is the Makefile for your final draft

# CC specifies the Latex compiler BIB specifies the 
# bibliography compiler
CC = pdflatex
BIB = biblatex

# these specify the names of the .tex source files
MAIN = main
PART = part

SRC = ./$(MAIN)

# this is the default function
# it runs each function name in order seen below
all: tex_to_pdf clean-meta display

# runs the commands to convert the markdown content
# into latex source code

# takes the latex source code and compiles it into a pdf file
tex_to_pdf:
	$(CC) $(SRC).tex
	$(BIB) $(MAIN)
	$(CC) $(SRC).tex
	$(CC) $(SRC).tex

# dynamically updates the pdf file using Sumatra pdf
display:
	..\src\display_pdf.bat $(MAIN)

# deletes all the meta data used in compiling the latex source code
# except the log file (in case you need to debug)
clean-meta:
	del *.dvi
	del *.aux
	del *.bbl
	del *.blg
	del *.brf
	del *.out
	del *.toc

# cleans all files related to the document including the
# generated .tex files
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
