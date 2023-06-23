def game():
    return 680


score=game()

with open("hiscore.txt", "r") as f:
    hiscore = f.read()

if str(hiscore)=='':
    with open('hiscore.txt','w')as f:
        f.write(str(score))

elif str(score)>hiscore:
    with open('hiscore.txt','w')as f:
        f.write(str(score))