# Write a Python program that takes a list of integers as input and 
# returns a new list containing only the even numbers in the original list.

l1 = []
n = int(input("Enter size of list 1: "))
for i in range(1,n+1):
    a = int(input("Enter list element : "))
    l1.append(a)

ans =[]
for i in l1:
    if i%2==0:
        ans.append(i)

print(ans)