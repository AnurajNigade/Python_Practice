#Reverse string without inbuilt function

def reversed_str(string):
    reversed=""
    word=""

    for char in string:
        if char == " ":
            reversed=word + " " +reversed
            word=""
        else :
            word+=char
    reversed=word + " "+reversed
    return reversed

str=input("Enter sentence you want to reverse :")
print(reversed_str(str))
