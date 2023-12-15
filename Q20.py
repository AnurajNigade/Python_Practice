## armstrong number
def length(digit):
    length=0
    while digit>0:
        digit=digit//10
        length+=1
    return length

def armstrong(digit):
    temp=digit
    len1=length(digit)
    # print(len1)
    sum1=0
    while temp>0:
        last=temp%10
        print(last)
        temp=temp//10
        sum1+=(last**len1)
    
    print(digit)
    print(sum1)
    if digit==sum1:
        print("Yes armstrong")
    else:
        print("NOT armstrong")

armstrong(153)

