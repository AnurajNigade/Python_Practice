# no of occurences of a character in a string

def No_occ(string,ch):
    count=0
    for i in string:
        if i == ch:
            count+=1
    
    print(ch,"occurs",count)

str1=input("Enter string  : " )
ch=input("Enter character you want to search : ")
No_occ(str1,ch)