
amt=float(input("enter sale amount:"))
          
if(amt>0):
    if amt<=1000:
             discount=0
    elif amt<=2000:
             discount=amt*0.1
    elif amt<=3000:
             discount=amt*0.2
    elif amt<=5000:
             discount=amt*0.25
    print("discount :",discount)
else:
    print("invalid")
