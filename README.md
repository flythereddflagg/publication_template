# PUBLICATION TEMPLATE
A streamlined way to write documents in markdown and produce professional documents using Pandoc and LaTeX.

## Required Software

This template is designed for Windows users but may be adapted for Linux and Macintosh users. The software used is cross-platform and open source where possible. To use, you will need the following:

- [JabRef](https://www.jabref.org/) to make managing your bibliography easier (recommended but not required)
- The PowerShell script `./src/install_software.ps1` 
  - This will automatically install the rest of the needed software.
  - Just right-click on the script, select 'Run with PowerShell' and answer 'a' to the permission questions.
  - The following software tools will be installed for the user:
    - [scoop](https://scoop.sh/): to install the below software and manage updates
    - [Typora](https://typora.io/): to write in markdown with a WYSIWYG interface
    - [Pandoc](https://pandoc.org/): (required) to convert from markdown to tex
    - [Python](https://www.python.org/): (required) to automate Pandoc conversion and make adjustments as needed. To fix references for figures and tables, the following Python packages are needed:
      - [pandoc-xnos](https://github.com/tomduck/pandoc-xnos) (with dependencies)
    - [LaTeX](https://miktex.org/): (required) to convert from tex to pdf. I use MiKTeX for this project.
    - [Sumatrapdf](https://www.sumatrapdfreader.org/free-pdf-reader.html): (required) to display the pdf dynamically
    - [make](http://gnuwin32.sourceforge.net/packages/make.htm): (required) to automate all of this.

## How to use

- Once all the software is installed, you should have a PowerShell window open in the base directory. Files should be organized as follows:

  -  Markdown files should be saved in `./content/` and should be have filenames beginning with 2-digit numbers beginning with 10 (e.g. `10-introduction.md`, `11-lit-review.md`, `20-results-and-discussion.md` etc.). These two-digit numbers are intended to correspond to different sections of the document. Markdown files without the number >= 10 prefix will not be included. Usage examples are in `./content/10-Sample-Text.md`.
  - Feedback, edits and any old versions you want to keep can go in `./edits/`.
  - Pictures, tables and other external media should be in `./media/`.
  - Your bibliography file `bibliography.bib`, PDF copies of referenced literature and any related materials can be stored in `./references/`.

- The other folders are for convenience in working with the document:

  - `./src/` contains the relevant code files to make the system work. Generally you will not do anything in that folder so just leave it alone.
  - `./tex/` contains the generated LaTeX files and allows you to make tweaks to the generated LaTeX as you go.

- Then just run: `PS C:\Users\...> make`

  And the document should compile and display as a PDF using Sumatra PDF. There are different options for `make` including:

  - `make clean`: reset your document and delete all files generated by `make`
  - `make nobib`: same as make but skips the generation of the bibliography
  - `make md`: generate the `.tex` files but do nothing else
  - `make pdf`: compile the generated `.tex` files to pdf
  - `make bib `: generate and add a bibliography to the compiled pdf
  - `make display`: display the compiled pdf

- If you are ready to make a final draft with fine-grain adjustments to your publication, copy all the LaTeX source files into `./final_draft/`. This allows you to use the Makefile in that folder to adjust then compile the LaTeX files directly in the folder.


Good luck! Input and contributions welcome!

