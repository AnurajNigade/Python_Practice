def second_large(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    
    print("Second largest number from array is : ",arr[1])

def sec_large2(arr):
    max_no=arr[0]
    sec_large=arr[1]
    for i in range(2,len(arr)):
        if arr[i]>sec_large and arr[i]<max_no:
            sec_large=arr[i]
        elif arr[i]>max_no :
            max_no=arr[i]
            sec_large=max_no

    print("Second large is :",sec_large) 

def sec_large3(arr):
    sorted(arr,reverse=True)
    print(arr[1])         

arr=[20,21,5,6,9,77,85,97,63,11,22,33,66]
second_large(arr)
sec_large2(arr)
sec_large3(arr)