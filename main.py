import sys
import os
import subprocess

RUN_ERROR_MESSAGE = 'python main.py [ml | ds | se] companyname "position"'

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
        pass #Work on this later
    else:
        print("Invalid run type - " + RUN_ERROR_MESSAGE)

    with open(filepath, "r") as f:
        content = f.read()

    content = content.replace("{\companyname}{}", "{\companyname}{"+company_name+"}")
    content = content.replace("{\position}{}", "{\position}{" + position + " " + "}")

    position = '_'.join(position.split())

    new_path = f'cover_letters/{company_name}_{position}'
    os.makedirs(name=new_path)

    path_to_main = f"{new_path}/main.tex"
    
    with open(path_to_main, "w") as f:
        f.write(content)

    subprocess.run(["pdflatex", f"-jobname={company_name}_{position}_cover_letter", f"-output-directory={new_path}", path_to_main])
    # subprocess.run(["mv", "main.aux", new_path+"/main.aux"])
    # subprocess.run(["mv", "main.log", new_path+"/main.log"])
    # subprocess.run(["mv", "main.out", new_path+"/main.out"])

if __name__ == "__main__":
    main()