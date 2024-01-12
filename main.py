import sys
import os
import json
import subprocess

RUN_ERROR_MESSAGE = 'python main.py [ml | ds | se] companyname "position"'

with open("last_lines.json", "r") as json_file:
    last_lines = json.load(json_file)

def main():
    if len(sys.argv) < 3:
        print('Invalid number of arguments - ' + RUN_ERROR_MESSAGE)
        sys.exit(1)

    pos_type = sys.argv[1]
    company_name = sys.argv[2].replace("_", " ")
    position_0 = ' '.join(sys.argv[3:])

    #Clean up position name
    position = position_0
    for position_type in last_lines:
        position = position.replace(position_type, "")

    #Select appropriate LaTeX document for type of job
    if pos_type in ['ml', 'ds', 'se']:
        filepath = pos_type+".tex"
    else:
        print("Invalid run type - " + RUN_ERROR_MESSAGE)

    #Read basic template .tex document
    with open(filepath, "r") as f:
        content = f.read()

    #Fill in company and position names on template
    content = content.replace("{\companyname}{}", "{\companyname}{"+company_name+"}")
    content = content.replace("{\position}{}", "{\position}{" + position + " " + "}")

    #Use default ending at first
    last_line = last_lines["-default"]
    
    #Reselect last line based on type of company
    for position_type in last_lines:
        if position_type in position_0:
            last_line = last_lines[position_type]
            break

    content = content.replace("[last_line]", last_line)

    if "-usa" in position_0:
        content = content.replace("% \\newline \\newline \small \\textit", "\\newline \\newline \small \\textit")

    position = '_'.join(position.split())

    #Make a folder containing both .tex and .pdf documents for the cover letter
    new_path = f'cover_letters/{sys.argv[2]}_{position}'
    os.makedirs(name=new_path)

    path_to_main = f"{new_path}/main.tex"
    
    #Add text content to .tex document
    with open(path_to_main, "w") as f:
        f.write(content)

    #Generate pdf
    subprocess.run(["pdflatex", f"-jobname={sys.argv[2]}_{position}_cover_letter", f"-output-directory={new_path}", path_to_main])

if __name__ == "__main__":
    main()