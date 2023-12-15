## Perfect number or not

def perfect_no(num):
    temp=num
    sum1=0
    
    for i in range(1,temp):
        if temp%i==0:
            sum1+=i
            print(i)
    
    if sum1==num:
        print("perfect number !!")
    else : 
        print("not perfect number !")

perfect_no(28)
