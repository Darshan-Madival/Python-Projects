a=20#global variable
def function1():
    z=10#enclosing variable it is a non local variable
    print(z)
    def function2():
        a=5#local variable
        print(a)
    function2() 
    print(z)#print,def,etc are built in variables which is already exits in python  
      
function1()
        