aranan=26
liste=[1,3,5,7,9,11,13,15,17,18,26,27,31,38,46,78]
medyan=len[liste]//2
def binary(dizi,aranan):



if len[liste]==1:
    if aranan == liste[0]:
        return liste[0]
    else :
        return False
else:
    if aranan==liste[medyan]:
        return  liste[medyan]
    if aranan<liste[medyan]:
        return binary(liste[0:medyan].aranan)
    if aranan>liste[medyan]:
        return binary(liste[medyan:len(liste)].aranan)
    
print(binary(liste,26))