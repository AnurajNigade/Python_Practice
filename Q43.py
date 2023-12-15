import re

def valid_palindrome(str):
    cl_str=re.sub(r'[^\w*\s*]','',str)

    if cl_str == cl_str[::-1]:
        print("Yes Palindrome")
    else : 
        print("No Palindrome")
    print(cl_str)
str = input("Enter String : ")
valid_palindrome(str)

# str=['d','f','g','f']
# ans="".join(str)
# print(ans)



