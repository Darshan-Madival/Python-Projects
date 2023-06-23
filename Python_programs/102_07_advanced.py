from pickle import TRUE


def greater_than_5(num):
    if num>5:
        return TRUE
    else:
        return False
    
darshan=lambda k :k>5
k=[1,2,3,4,5,6,78]    
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(list(filter(greater_than_5,l)))    
print(list(filter(darshan,k)))    