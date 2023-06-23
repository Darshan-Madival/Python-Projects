def divisible_by_5(num):
    if num%5==0:
        return True
    else:
        return False
    
l=[5,12,10,15,16,23]
print(list(filter(divisible_by_5,l)))
    