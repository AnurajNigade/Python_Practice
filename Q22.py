#  string contains only digit

def check_digit(str1):
    flag=True
    for i in str1:
        if i.isalpha():
            flag=False
    
    if flag==True:
        print("Given string only contains digit")
    else:
        print("Given string not contains all digit")

def check_digit1(str1):
    if str1.isdigit():
        print("Given string only contains digit")
    else:
        print("Given string does not contain all digits")


check_digit1("122335")
check_digit("a122335")
