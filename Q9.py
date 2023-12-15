import math
n=int(input("enter position of prime number"))
def isprime(n1):
    if n1<2:
        return False
    for i in range(2,int(n1**0.5)+1):
        if n1%i ==0:
            return False
    return True
countr=0
i = 2  # Start with the first prime number (2)
while countr < n:
    if isprime(i):
        countr += 1
        if countr == n:
            print(f"The {n}th prime number is {i}")
            break
    i += 1
print(i)
# for i in range(1,100000):
#     if(isprime(i)):
#         countr+=1
#         if countr==n:
#             print(i)            
#             break

# print((10**0.5))
# print(math.sqrt(10))
        
