# Write a Python function that takes a list of integers as input and returns the maximum number in the list.

# ls = []

# n = int(input("Enter size of list : "))
# for i in range(1,n+1):
#     a = int(input("Enter list element : "))
#     ls.append(a)
# ls.sort()

# print("Max element from list is : ",ls[-1] )

ls = []

n = int(input("Enter size of list : "))
for i in range(1,n+1):
    a = int(input("Enter list element : "))
    ls.append(a)
max_no =ls[0]
for i in ls(1,n+1):
    if max_no > i :
        max_no =i

print(max_no) 