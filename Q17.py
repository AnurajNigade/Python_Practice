## Sum of digit in number

def Sum(num):
    sum1=0
    while num>0:
        last=num%10
        sum1+=last
        num=num//10
    print(sum1)

Sum(1234)    
