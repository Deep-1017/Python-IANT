import os

# f = open("file1.txt", "r")
# # print(f.readlines())
# print(f.read(10))
# f.close()

# with open("file1.txt") as f:
#     print(f.read())

with open("file1.txt", "a") as f:
  f.write("\nNow the file has some more content!")


if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
  print("The file does not exist")
  
# print(os)