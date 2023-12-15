## Given number is perfect square
import math
def is_square(num):
    result=math.sqrt(num)
    print(result)
    print(int(result))
    if result==int(result):
        print("Given number is perfect square")
    else: 
        print("Not perfect square")

is_square(25)