# chech string is palindrome or not

def palin(string):

    reverse=""

    for i in string:
        reverse=i+reverse
    
    if reverse==string:
        print("Given String is palindrome")
    else :
        print("String is not palindrome")

str=input("Enter string : ")
palin(str)
    