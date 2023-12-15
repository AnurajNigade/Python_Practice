# Write a Python program that takes a list of strings as input and returns a new list containing 
# only the strings that start with the letter 'a'.

List = []
Strings = input("Please enter a list of strings: ")
List = Strings.split(" ")
print(List)
ans = []
for i in List :
    if i[0]=='a'or i[0]=='A':
        ans.append(i)

print(ans)
