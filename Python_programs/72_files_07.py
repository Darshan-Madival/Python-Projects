words=['donkey','monkey','pandu','poude']
with open("darshan.txt")as f:
    content=f.read()

for word in words:
    content = content.replace(word,'$%$#@&')

with open('darshan.txt','w')as f:
    f.write(content)