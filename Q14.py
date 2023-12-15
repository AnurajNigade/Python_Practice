def fibbo(n):
    f1,f2=0,1
    for i in range(n):
        if i==0:
            print(f1,end=" ")
        elif i==1:
            print(f2,end=" ")
        else:
            fn=f1+f2
            if fn<n:
                print(fn,end=" ")
            f1,f2=f2,fn

fibbo(20)

