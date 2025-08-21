def line():
    print("\n".ljust(60, ".") + "\n")

with open("demofile.txt") as f:
    print(f.read())
    print(f.readline()) 
    # f.readline() não vai funcionar porque ele
    # já leu todo o arquivo

line()

with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

line()

with open("demofile.txt") as f:
    for ln in f:
        print(ln)

line();

append_demo_file="demofile-append.txt"
with open(append_demo_file, "a") as f:
    for i in range(0,10):
        f.writelines("Now the file has more content!\n")

with open(append_demo_file) as f:
    print(f.read())

line()

import os

if os.path.exists(append_demo_file):
    os.remove(append_demo_file)
    print(append_demo_file + " was removed.")
else:
    print("The file does not exist")