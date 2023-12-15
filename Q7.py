slist=[2,4,5,6,6,6,6,2,5,8,]
ans={}

for i in slist:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=1
print(ans)

sort=sorted(ans.items(),key=lambda x:x[1])
print(sort)


