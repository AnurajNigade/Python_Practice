def sum_digit_string(str):
    sum=0
    for i in str:
        if i.isdigit():
            sum+=int(i)
    
    print(sum)

str=input("Enter string : ")
sum_digit_string(str)

