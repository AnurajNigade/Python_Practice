# anagrams string

def anagram(str1,str2):
    lstr1=list(str1)
    for i in range(len(lstr1)):
        for j in range(len(lstr1)-i-1):
            if lstr1[j]>lstr1[j+1]:
                lstr1[j],lstr1[j+1]=lstr1[j+1],lstr1[j]

    new_str1=""            
    for x in lstr1:
        new_str1+=" "+x
    print(new_str1)
    lstr2=list(str2)
    for i in range(len(lstr2)):
        for j in range(len(lstr2)-i-1):
            if lstr2[j]>lstr2[j+1]:
                lstr2[j],lstr2[j+1]=lstr2[j+1],lstr2[j]
    
    new_str2=""
    for x in lstr2:
        new_str2+=" "+x
    print(new_str2)
    print(str(lstr2))
    if lstr1 == lstr2:
        print("given string is anagram")
    else:
        print("String is not anagram")

str1=input("Enter first string : ")
str2=input("Enter second string : ")

anagram(str1,str2)