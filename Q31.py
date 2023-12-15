## String is palindrome

def palindrome(string):
    temp=list(string)
    temp.reverse()
    ans=''.join(temp)
    if ans == string:
        print(ans,"is palindrome ")
    else:    
        print(string,"is not palindrome ")

def palindrome1(string):
    str1=""
    for i in string:
        str1=i + str1
    if str1 == string:
        print(str1,"is palindrome ")
    else:    
        print(string,"is not palindrome ")


palindrome(input("Enter string : " ))
palindrome1(input("Enter string : " ))