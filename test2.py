data=int(input("input number:"))
list=[]
for i in range(1,data+1):
    if(i%15==0):
        list.append(i)
    elif(i%3==0 or i%5==0):
        continue
    else:
        list.append(i)
print(len(list))  


for test1 :1651896132198