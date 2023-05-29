import re

pattern = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

value=input("please enter your email adress: ")

if re.search(pattern,value):
    print(f"{value} is valid")
else:
    print(f"{value} is invalid")

