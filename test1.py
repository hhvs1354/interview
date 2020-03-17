s=input("input:")

x=s.split(" ")
x=reversed(x)
str=""
for word in x:
    str+=word
    str+=" "
    
print("A:"+str)
print("B:"+s[::-1])