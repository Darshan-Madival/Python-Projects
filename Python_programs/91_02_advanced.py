from logging import exception


i=input("enter the number\n")
try:
    i=int(i)
    if(i>20):
        print("Good")
except Exception as e:
    print(f"The error occured {e}")
 
finally:
    print("Jai hind")     
        