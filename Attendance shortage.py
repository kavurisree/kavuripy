class AttendanceShortageException(Exception):
 def __init__(self,arg):
  self.msg=arg
class IncomeException(Exception):
 def __init__(self,arg):
  self.msg=arg
class GPAException(Exception):
 def __init__(self,arg):
  self.msg=arg
Attendance=int(input("Enter Attendance:"))
if Attendance>50:
 raise AttendanceShortageException("ok fine")
elif Attendance<18:
 raise AttendanceShortageException("not allowed")
else:
 print("you are promoted")
 Income=int(input("Enter Income:"))
if Income>500000:
 raise IncomeException("ok fine")
elif Income<180000:
 raise IncomeException("not allowed")
else:
 print("you are promoted")
GPA=int(input("Enter Attendance:"))
if GPA>8:
 raise GPAException("ok fine")
elif GPA<6:
 raise GPAException("not allowed")
else:
 print("you are promoted")                                                
