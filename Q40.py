def count_UL(str):
    count_u=count_l=0
    for i in str:
        if i.isupper():
            count_u += 1
        elif i.islower():
            count_l += 1
    count_d=0   
    print ("Count of Upper is :",count_u,"Count of Lower is :" ,count_l)

str=input("Enter String :")
count_UL(str)
