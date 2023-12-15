# Write a Python function that takes a list of integers as input and 
# returns a new list where each element is the sum of the previous two elements in the original list.

l1 = []
n = int(input("Enter size of list greater than 2: "))
for i in range(1,n+1):
    a = int(input("Enter list element : "))
    l1.append(a)


sum_list = [l1[0], l1[1]]  
for i in range(2, len(l1)):
    next_sum = l1[i - 1] + l1[i - 2]
    sum_list.append(next_sum)

print(sum_list)