import os

file = "data.txt"

# create and write
f = open(file,"w")
f.write("Hello Python\n")
f.write("File Handling Example\n")
f.close()

# append
f = open(file,"a")
f.write("New Line Added\n")
f.close()

# read full file
f = open(file,"r")
print("Read Full File:")
print(f.read())
f.close()

# readline
f = open(file,"r")
print("First Line:",f.readline())
f.close()

# readlines
f = open(file,"r")
print("All Lines:",f.readlines())
f.close()

# copy file
with open(file,"r") as f1, open("copy.txt","w") as f2:
    f2.write(f1.read())

print("File Copied")

# check file exists
if os.path.exists(file):
    print("File Exists")

# delete copy file
os.remove("copy.txt")
print("Copy File Deleted")