def reverse_word (str):
    ls = str.split(" ")
    ls.reverse()
    print(ls)
    ans=" ".join(ls)
    print(ans)

def reverse_word1(str):
    ls=[]
    temp=""
    for i in str:
        if i.isalpha():
            temp=temp+i
        elif i == " ":
            ls.append(temp)
            temp=""
    ls.append(temp)
    ans=ls[::-1]
    # print(ls)
    # print(ans)
    ans_str=""
    for i in ans:
        ans_str=ans_str+i+" "
    print(ans_str)

reverse_word1("My name is anuraj")
