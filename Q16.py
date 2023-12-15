  # GCD of two numbers

def GCD(n1,n2):
    while n1!=n2:
        if n1>n2:
            n1=n1-n2
        else:
            n2=n2-n1
    return n1

print(GCD(15,30))        