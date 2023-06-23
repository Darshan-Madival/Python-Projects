from functools import reduce

sum=lambda a,b:a+b

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

val=reduce(sum,l)
print(val)