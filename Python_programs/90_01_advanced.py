from logging import exception

while (True):
    a = input("enter the number\n")
    try:
        a = int(a)
        if a >= 18:
            print("your age is greater then 18")
            break
        else:
            print("Not eligible")

    except Exception as e:
        print(f"The error occured{e}")