# coverletter

This project requires LaTeX. You can install it here: https://www.latex-project.org/get/

After that's installed, run
```
pip install -r requirements.txt
```
to install the requirements.

Right now I have cover letters for machine learning and data science jobs. If you want to use this, CHANGE THE .TEX FILES TO USE YOUR OWN CONTENT.
This is nowhere near production level, so the cover letters I currently use are still in the .tex files

## Running

To test this, try adding lines to list.txt in the form
```
ml CompanyName software engineer intern
```
You must have a template file whose name exactly matches the first word; in this case, it's ml.tex.

Then, run the command
```
python3 automator.py
```

This will generate a PDF in the new folder cover_letters/CompanyName_software_engineer_intern, with the company name and job title included in the cover letter.
PDFs will also be generated for each line in list.txt.
Note that PDF generation does not work unless you have LaTeX installed.

You can also add additional flags, like "-startup", and "-finance", depending on what type of company you're applying to. This changes the last line of the cover letter so you can _really_ suck up to each company. These flag categories, along with the associated last lines they have, can be found in last_lines.json. You can edit the text they produce there, too.

## Editing files

For each cover letter, automator.py generates a .tex file, a PDF file, and some log files. If you want to make extra adjustments to the cover letter that you created using the command
```
ml CompanyName software engineering intern
```
navigate to the folder cover_letters/CompanyName_software_engineer_intern, where you'll find a file main.tex. Make your edits there. Then, from the root directory, run the command
```
./edit.sh CompanyName_software_engineer_intern
```
to save your changes and add them to the PDF.
