content= True
i=1
with open('darshan.txt')as f:
    while content:
      content=f.readline().lower()
      if 'python' in content:
          print("line",i)
          print(content)

      else:
          i+=1