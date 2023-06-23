# def factorial(n):
    
#     product=1
#     for i in range(1,n+1):
#         product=product*i
#     return product
        
# print(factorial(5))

#recursion

# def recurse(n):
#     if(n==0 or n==1):
#         return 1
#     return n*recurse(n-1)
# print(recurse(5)) 

def sumlist(numlist):
    if  len(numlist)==1:
        return numlist[0]
    return numlist[0]+sumlist(numlist[1:])

print(sumlist([1,2,3,4,5]))
 
# def listsum(numList):
#     if len(numList) == 1:
#        return numList[0]
   
#     return numList[0] + listsum(numList[1:])
    
    
# print(listsum([1,3,5,7,9]))


    
     