## Reverse of array

def rev_arr(arr):
    print(arr[::-1])

def rev_arr1(arr):
    rev=[]
    for i in arr:
        rev.insert(0,i)
    print(rev)

arr=[54,6,962,658,89,3,46,69,23,74]
rev_arr(arr)
rev_arr1(arr)
