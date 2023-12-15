import math

def square(x):
    if x<0:
        x=-x
    ans=0
    for i in range(x):
        ans += x
    
    return ans

n=int(input("Enter the number :"))
print(square(n))

# arr=list(map(int,input().split()))
# print(arr)