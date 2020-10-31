#Student report card
print('Student report card')
stud_name=input('Please enter Name :')
stud_age=int(input('Pleae enter Roll no :'))
english_marks=int(input('Please enter English marks :'))
maths_marks=int(input('Please enter Maths marks :'))
science_marks=int(input('Please enter Science marks :'))
social_marks=int(input('Please enter social marks :'))
Telugu_marks=int(input('Please enter Telugu marks :'))
hindi_marks=int(input('Please enter hindi marks :'))
total = maths_marks + science_marks + english_marks+ social_marks+ Telugu_marks+hindi_marks
print('total',total)
stud_percentage = (total/600 * 100)
print('stud_percentage',stud_percentage)
avg=(total/600)
print('avg',avg)

#Student grade classification
if(stud_percentage>=80): 
  print('A')
elif stud_percentage >=60 and  stud_percentage< 79:
  print('B')
elif (stud_percentage>50 and stud_percentage<59):
  print('C')
elif (stud_percentage>40 and stud_percentage<49):
  print('D')
elif (stud_percentage<40):
  print('promoted')
else:
  print('Fail')
print('=======================================')
