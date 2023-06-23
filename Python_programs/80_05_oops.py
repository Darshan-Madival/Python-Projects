class Trian:
    def __init__(self,name,price,seats):
        self.name=name
        self.price=price
        self.seats=seats
    def status(self):
        print(f"*******The Train Name {self.name} The Price is {self.price} and seats Avialable are {self.price}*******")
    
    def bookticket(self):
        if(self.seats>0):
            print(f"Your seat is booked!! and your seat  number is {self.seats}")
            self.seats=self.seats-1
        else:
            print(f"Sorry!! kindly try for next trian The number of seats Avilable are {self.seats}")
    def bookticket(self):
        if(self.seats>0):
            print(f"Your seat is booked!! and your seat  number is {self.seats}")
            self.seats=self.seats-1
        else:
            print(f"Sorry!! kindly try for next trian The number of seats Avilable are {self.seats}")
    
    def cancel(self):
        a=int(input("if you want cancel your seats Please enter 1\n"))
        if(a==1):
            b=int(input("Please type your Seat number"))
            self.seats=b
        elif(a==2):
            pass
    
    def bookticket(self):
        if(self.seats>0):
            print(f"Your seat is booked!! and your seat  number is {self.seats}")
            self.seats=self.seats-1
        else:
            print(f"Sorry!! kindly try for next trian The number of seats Avilable are {self.seats}")        #if(self.seats==b):
            
            
    
sirsi=Trian("Sirsi Express",100,2)

sirsi.status()
sirsi.bookticket()
sirsi.bookticket()
sirsi.cancel()
sirsi.bookticket()