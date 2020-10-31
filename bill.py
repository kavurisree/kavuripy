unit=int(input("Enter the unit consumed: "))
def Bill(unit):         
    if((unit>=1)and(unit<=50)):
        print(unit*3);
    
    elif((unit>50)and(unit<=100)):
        print((50*3)+(unit-50)*6)
    
    elif((unit>100)and(unit<=150)):
        print((50*3)+((100-50)*6)+(unit-100)*9)
    
    elif(unit>200):          
        print((50*3)+((100-50)*6)+((150-100)*9)+(unit-150)*12)
    else:
            print("No usage ");
      
Bill(unit)             
