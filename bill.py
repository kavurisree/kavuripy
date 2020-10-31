unit=int(input("Enter the unit consumed: "))
def Bill_Calc1(unit):          #function definition
    if((unit>=1)and(unit<=50)):#between 1 - 50 units
        print(unit*3);
    
    elif((unit>50)and(unit<=100)):#between 50 - 100 units
    
        print((50*3)+(unit-50)*6)
    
    elif((unit>100)and(unit<=150)):#between 100 -  150 units
        print((50*3)+((100-50)*6)+(unit-100)*9)
    
    elif(unit>200):           #above 200 units
        print((50*3)+((100-50)*6)+((150-100)*9)+(unit-150)*12)
    else:
            print("No usage ");
        #amount=0;
Bill_Calc1(unit)             
