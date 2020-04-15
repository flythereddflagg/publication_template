# PUBLICATION TEMPLATE
(Intended for windows users) To use this you will need the following:

- [JabRef](https://www.jabref.org/) to make managing your bibliography easier

- The PowerShell script `./src/install_software.ps1` 
  - This will automatically install the rest of the needed software.
  - Just right-click on the script, select 'Run with PowerShell' and answer 'a' to the permission questions.
  - The following software tools will be installed for the user:
    - [scoop](https://scoop.sh/) (to install the below software and manage updates)
    - typora (to write in markdown with a WYSIWYG interface)
    - pandoc (to convert from markdown and tex)
    - python (to automate pandoc conversion and make adjustments as needed)
    - latex (to convert from tex to pdf)
    - sumatrapdf (to display the pdf dynamically)
    - make (to automate all of this)

### How to use:

Once all the software is installed, you should have a PowerShell window open in the base directory. Markdown files should be saved in your "content" folder and should be ordered beginning with 2-digit numbers beginning with 10 (e.g. `10-introduction.md`, `11-lit-review.md`, `20-results-and-discussion.md` etc.). Markdown files without the number >= 10 prefix will not be included. Pictures, tables and other external media should be in the "media" folder. Then just run:

```powershell
PS C:\Users\<username>\Documents\publication_template> make
```

And the document should compile and display as a PDF using Sumatra PDF.

Use `make clean` to reset your document if desired.

Good luck! Input and contributions welcome!

