print("begin")
try:
    print(10/2)
    print(10/ten)
except ZeroDivisonError as msg:
    print(msg)
finally:
    print("end")
