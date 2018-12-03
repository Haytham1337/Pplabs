import random
lines = open('file1.txt').read().splitlines()
myline =random.choice(lines)
print(myline)