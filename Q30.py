n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    ch=input()
    if ch=='pop':
        s.pop()
    elif ch=='remove':
        x=int(input())
        s.remove(x)
    elif ch=='discard':
        x=int(input())
        s.discard(x)

print(sum(s))
        