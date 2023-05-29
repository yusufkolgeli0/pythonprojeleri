array=["serrap","serpil","sevda"]
first_word = array[0]
pref = ""
exit = False
for a in array:
    if len(a)<len(first_word):
        first_word=a
    
print(first_word)
for each_word  in array:
    if exit == True:
        break
    for index in range(0, len(first_word)):
        if first_word != each_word:
            if first_word[index] == each_word[index]:
                pref = pref + first_word[index]
            else:
                exit = True
                break

print(pref)        
    # print(first_word,each_word)




# for a in x:
#     if not x[0]==y[0]:
#         print("ıts not common prefix")
#     elif x[2]==y[2] and x[2]==z[2] and x[1]==y[1] and x[1]==z[1] and x[3]==y[3] and x[3]==z[3]:
#         print(x[0]+x[1])
#     elif x[2]==y[2] and x[2]==z[2] and x[1]==y[1] and x[1]==z[1]:
#         print(x[0]+x[1]+x[2])
#     elif  x[1]==y[1] and x[1]==z[1]:
#         print(x[0]+x[1])
#     else:
#         print(x[0])
    