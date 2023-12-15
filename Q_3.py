# Write a Python program that takes two lists of integers as input and returns a new list containing only the common elements of both lists.

l1 = []
l2 = []
n = int(input("Enter size of list 1: "))
for i in range(1,n+1):
    a = int(input("Enter list element : "))
    l1.append(a)
m = int(input("Enter size of list 2: "))
for i in range(1,m+1):
    a = int(input("Enter list element : "))
    l2.append(a)

l3 =[]
for i in l1 :
    for b in l2 :
        if i==b:
            l3.append(i)

print(l3)
