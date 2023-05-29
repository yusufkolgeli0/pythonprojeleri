

word=input("please enter a word: ")
v=["a","e","i","o","u","A","E","I","O","U"]

vowel=0
consonant=0

for i in word :
    if i in v :
        vowel+=1
    else:
        consonant+=1
print(f"the numbers of vowels are {vowel}")
print(f"the numbers of consonants are {consonant}")