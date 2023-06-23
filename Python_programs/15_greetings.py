letter='''Dear <|Name|>,
congrajulations you are selected
Have a great future ahead
<|Date|>'''


name=input("Enter your name:")
date=input("Enter Date:")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)
