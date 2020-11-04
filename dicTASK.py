def menu():
 print("1.enter the task")
 print("2.date")
 print("3.exit")
 while True:
    try:
     select=int(input("enter your choice:"))
     if select==1:
            task()
            break
     elif select==2:
            date()
            break
     elif select==3:
            break
     else:
            print("invalid")

             menu()
