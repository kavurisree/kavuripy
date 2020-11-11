
class LimitException(Exception):
 def __init__(self,arg):
  self.msg=arg
class InvalidminimumException(Exception):
 def __init__(self,arg):
  self.msg=arg
class InsufficientFundException(Exception):
 def __init__(self,arg):
  self.msg=arg
amount=int(input("Enter amount:"))
if amount>10000:
 raise LimitException("ok fine")
elif amount<100:
 raise InvalidminimumException("not allowed")
elif amount<50:
 raise InsufficientFundException("Insufficient")
else:
 print("you receive the receipt")
 
