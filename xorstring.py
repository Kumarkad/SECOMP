s="Hello World"
x=[]
a=[]
for char in s:
    x.append(ord(char)^127)
for char in s:
    a.append(ord(char)&127)
print("Original  ", " xor ","        and")
for i in range(len(s)):
    print(s[i],"      :   ",x[i],"    :   ",a[i])