def natural_no_sum(no):
    sum = 0
    for i in range(1,no+1):
        sum += i
    print(sum)
no=int(input("enter number : "))
natural_no_sum(no)