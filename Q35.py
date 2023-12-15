def check_long_consecutive_sub(arr,n):
    if n==1: return 1

    count=ans=0
    arr1=[]
    for i in range(n):
        if i not in arr1:
            arr1.append(arr[i])
    arr1.sort()
    for i in range(len(arr1)):
        if arr1[i]==arr1[i-1]+1:
            count+=1
        else: 
            count=1
        ans=max(count,ans)
    return ans

arr = [1, 2, 2, 3, 4, 6,66,5]
n = len(arr)
 
print("Length of the Longest contiguous subsequence is",
      check_long_consecutive_sub(arr, n))


## For Repeating elements
# def check_long_consecutive_sub(arr,n):
#     if n==1: return 1

#     count=ans=0
#     arr.sort()
    
#     for i in range(len(arr)-1):
#         if arr[i+1]-arr[i]==1:
#             count+=1
#         elif arr[i+1]-arr[i]==0: 
#             continue
#         else:
#             count=1
#         ans=max(count,ans)
#     return ans

# arr = [1, 2, 2, 3, 4, 6,6,6,6,66,5]
# n = len(arr)
 
# print("Length of the Longest contiguous subsequence is",
#       check_long_consecutive_sub(arr, n))

