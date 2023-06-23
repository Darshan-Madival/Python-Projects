import os
oldname="sample.txt"
newname="darshu.txt"
with open(oldname,'r')as f:
    content=f.read()
with open(newname,'w')as f:
    f.write(content)

os.remove(oldname)