import math

def Check_per_cube(no):
    ans = round(math.cbrt(no))
    if ans*ans*ans == no:
        print(ans)
        return True
    return False

no = int(input("Enter Number :"))
print(Check_per_cube(no))

str="Anuraj"
print(str[::-1])