# Write Program for following requirement       input:a4b3c2   output:aaaabbbcc

string=input("Enter string : ")
output=""
for i in range(0, len(string),2):
    char=string[i]
    count=int(string[i+1])   
    output=output+char*count

print(output)
