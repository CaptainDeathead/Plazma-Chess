import sys

string = ""

for i in range(int(sys.argv[1])):
    string += "1"

print(int(string, 2))