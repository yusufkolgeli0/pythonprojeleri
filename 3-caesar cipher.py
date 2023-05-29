alp= "abcdefghijklmnopqrstuvwqyz"
msg= "kara"
new_msg= ""
plus=3
for char in msg:
    new_msg=new_msg+alp[alp.index(char)+plus]
    print(new_msg)


