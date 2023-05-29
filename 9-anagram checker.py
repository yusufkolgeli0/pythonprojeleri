str1=input("please enter first string: ")
str2=input("please enter second string: ")

if len(str1) != len(str2):
    print("this is not anagram")

else:
    if sorted(str1)==sorted(str2):
        print("this is anagram")
    else:
        print("this is not anagram")


