 
def addTwoNum(x,y):
    ans=x
    for i in range(1,y):
        ans+=x
    print(ans)

x,y=map(int ,input().split())
addTwoNum(x,y)

# haystack = "hello"
# needle = "loa"

# index = haystack.find(needle)

# if index != -1:
#     print(f"The first occurrence of '{needle}' in '{haystack}' is at index {index}.")
# else:
#     print(f"'{needle}' not found in '{haystack}'.")
