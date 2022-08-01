import sys

if sys.argv == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith("py"):
    sys.exit("Not a python file")

try:

    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")


i = 0

not_a_line = 0




while i < (len(lines)):
    if lines[int(i)].startswith(('\n', '\t')):
        not_a_line = not_a_line + 1

    i = i + 1
i = 0
while i < (len(lines)):
    if "#" in lines[int(i)]:
        not_a_line = not_a_line + 1

    i = i + 1





loc = len(lines) - not_a_line
print(loc)