slst=['rahul','nick','max','abhishek','tom']

# print(slst)
for i in range (len(slst)-1):
    for j in range(0,len(slst)-i-1):
        if len(slst[j])>len(slst[(j+1)]):
            slst[j], slst[j + 1] = slst[j + 1], slst[j]

print(slst)                           
ans=[]
for i in slst:
    j=''.join(sorted(i))
    ans.append(j)
print(ans)

# anssort=sorted(ans.items(),key=lambda x:x[1])
# print(anssort)