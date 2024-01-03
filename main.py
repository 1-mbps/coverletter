import sys
import os
from pdflatex import PDFLaTeX as pdfl

RUN_ERROR_MESSAGE = 'python main.py [ml | se] companyname "position"'

def main():
    if len(sys.argv) < 3:
        print('Invalid number of arguments - ' + RUN_ERROR_MESSAGE)
        sys.exit(1)
    pos_type = sys.argv[1]
    company_name = sys.argv[2]
    position = ' '.join(sys.argv[3:])
    if pos_type == 'ml':
        filepath = "main.tex"
    elif pos_type == 'se':
        pass #Work on this late
    else:
        print("Invalid run type - " + RUN_ERROR_MESSAGE)

    with open(filepath, "r") as f:
        content = f.read()

    content = content.replace("{\companyname}{}", "{\companyname}{"+company_name+"}")
    content = content.replace("{\position}{}", "{\position}{" + position + " " + "}")

    new_path = f'cover_letters/{company_name} {position}'
    os.makedirs(name=new_path)
    
    with open(f"{new_path}/main.tex", "w") as f:
        f.write(content)

    file = pdfl.from_binarystring(content, 'main')
    pdf, log, cp = file.create_pdf()

if __name__ == "__main__":
    main()