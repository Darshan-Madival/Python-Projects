def remove_and_split(string,word):
       
       newstr= string.replace(word,"")
       return newstr.strip()



this="     i am darshan      "
n=remove_and_split(this,"darshan")
print(n)