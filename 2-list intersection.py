
L1=[1,2,3,4,5,6]
L2=[3,5,7,9,1]

intersection=[]

for i in L1:
    if i in L2:
        intersection.append(i)

print("your intersection list is", intersection)