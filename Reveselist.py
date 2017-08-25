x,y=input("Enter two list")
i=0
j=0
flag=0
while(i<len(x) and j<len(y)):
    if(x[i]==y[j]):
        i+=1
        j+=1
        flag=1
        continue
    else:
        break
if flag==1:
    print("List are same")
else:
    print("Lists are not same")