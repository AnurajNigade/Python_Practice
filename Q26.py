## Intersection of two array

def intersec(arr1,arr2):
    ans=[]
    for i in arr1:
        for j in arr2:
            if i==j:
                ans.append(i)
    print(ans)

arr1=[5,6,9,2,3,9,8,2,33,7,11,33,12]
arr2=[11,33,9,2,1,8,22,99,66,7]

intersec(arr1,arr2)