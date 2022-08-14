bal = 5000
pin=1234
class ATM:
    global bal
    def pinnumber(self):
        if p==pin:
            return True
        else:
            print("WRONG PIN NUMBER")
    def checkbalance(self):
        print("Your balance is " +str(bal))
    def cashwithdraw(self):
        c=int(input("ENTER THE CASH YOU WANT TO WITHDRAW: "))
        global bal
        if c<bal:
            bal=bal-c
            print("YOU SUCESSFULLY WITHDRAN THE CASH")
            print(f"YOUR AVAILABLE BALANCE IS {bal}")
        else:
            print(f"SORRY! YOU DON'T HAVE {c} CASH IN YOUR ACCOUNT")
    def casdeposit(self):
        d=int(input("ENTER THE CASH YOU WANT TO DEPOSIT: "))
        global bal
        bal=bal+d
        print(f"YOUR AVAILABLE BALANCE IS {bal}")



if __name__ == '__main__':
 print("**********WELCOME TO THE ATM OF DARSHAN MADIVAL**********")
 p = int(input("PLEASE ENTER YOUR ATM PIN: "))
 while(True):
  atm = ATM()
  if(atm.pinnumber()==True):
   print("*****PLEASE SELECT THE ATM SERVICE*****")
   print('''1.CHECK BALANCE\n2.CASH WITHDRAW\n3.CASH DEPOSIT\n4.QUIT''')
   a=int(input("ENTER THE YOUR CHOICE: "))
   if a==1:
    atm.checkbalance()
   if a==2:
       atm.cashwithdraw()
   if a==3:
       atm.casdeposit()
   if a==4:
       print("THANK YOU FOR USING OUR ATM SERVICES! HAVE A GREAT DAY")
       exit()
