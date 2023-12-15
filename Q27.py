## Strong number

def factorial(num):
    if num<2:
        return num
    else:
        return num * factorial(num-1)

def strong_number(no):
    sum1=0
    temp=no
    while temp>0:
        last=temp%10
        sum1+=factorial(last)
        temp=temp//10
    
    if no==sum1:
        # print("Yes Strong number ")
        print(no)
    # else :
    #     print("Not strong number")
for i in range(1,10000):
    strong_number(i)
