import subprocess

with open("list.txt", "r") as f:
    lines = f.readlines()

def main():
    for line in lines:
        line = line.split()
        subprocess.run(["python3", "main.py", line[0], line[1], ' '.join(line[2:])])

if __name__ == "__main__":
    main()