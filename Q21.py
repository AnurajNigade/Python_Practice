## Number word in sentence

def number_word(sent):
    slist=len(sent.split())
    print(slist)

def number_word1(sent):
    len1=0
    for i in sent:
        if i==" ":
            len1+=1
    len1+=1
    print(len1)

number_word("Anuraj nigade")
number_word1("Anuraj nigade Cdac")

