f = open("ex2.txt", "r")
print(f.read())
f.close()

with open("ex2.txt", "r") as f:
    print(f.read())
