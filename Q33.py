# def sub_set(arr,sum,res):
#     if sum == 0:
#         return True
#     if sum<0 or len(arr)==0 :
#         return False
#     if len(arr) > 0:
#         res.append(arr[0])
#         select = sub_set(arr[1:],sum-arr[0],res)
#         res.pop()
#         reject = sub_set(arr[1:],sum,res)
#         return select or reject
    
# arr = [3,4,5,2]
# sum=3
# res=[]
# print(sub_set(arr,sum,res))

# def sub_set(arr, target_sum, res):
#     if target_sum == 0:
#         return True
#     if target_sum < 0 or len(arr) == 0:
#         return False

#     # Include the first element in the subset
#     res.append(arr[0])
#     select = sub_set(arr[1:], target_sum - arr[0], res)

#     # Backtrack: Remove the last element to undo the inclusion
#     res.pop()

#     # Exclude the first element from the subset
#     reject = sub_set(arr[1:], target_sum, res)

#     return select or reject

# arr = [3, 4, 5, 2]
# target_sum = 2
# res = []
# print(sub_set(arr, target_sum, res))

# def sub_set(arr,sum,res):
#     if sum == 0:
#         return True
#     if sum<0 or len(arr)==0 :
#         return False
#     if len(arr) > 0:
#         res.append(arr[0])
#         select = sub_set(arr[1:],sum-arr[0],res)
#         res.pop()
#         reject = sub_set(arr[1:],sum,res)
#         return select or reject
    
# arr = [3,4,5,2]
# sum=7
# res=[]
# print(sub_set(arr,sum,res))

# def sub_set(arr,sum,res):
#     if sum == 0:
#         return True
#     if sum<0 :
#         return False
#     if len(arr)==0 and sum!=0:
#         return False
#     if len(arr) > 0:
#         res.append(arr[0])
#         select = sub_set(arr,sum-arr[0],res)
#         res.pop(0)
#         reject = sub_set(arr,sum,res)
#         return select or reject
    
# arr = [3,4,5,2]
# sum=7
# res=[]
# print(sub_set(arr,sum,res))

def sub_set(arr,sum,res):
    if sum == 0:
        return True
    if sum<0:
        return False
    if len(arr)==0 and sum!=0:
        return False
    if len(arr) > 0:
        a=arr.pop(0)
        res.append(a)
        select = sub_set(arr,sum-a,res)
        reject = sub_set(arr,sum,res)
        return select or reject
    
arr = [3,4,5,2]
sum=7
res=[]
print(sub_set(arr,sum,res))