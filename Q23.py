
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

sum_prime=0
num1=int(input("Enter range : " ))
for i in range(num1):
    if is_prime(i):
        print(i)
        sum_prime+=i
print("Sum is : ",sum_prime)


