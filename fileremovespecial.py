f1 = open("file1.txt", "r")
f2 = open("file2.txt", "w")
for line in f1.readlines():
    for c in line:
        if c.isalnum() or c == " " or c == "\t" or c == "\n" or c == "":
            f2.write(c)
f1.close()
f2.close()