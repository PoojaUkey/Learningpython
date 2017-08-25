def comparetwolist(l1,l2):
    flag=0
    if type(l1)!=list or type(l2)!=list:
        print("l1 or l2 is not list")
        return
    if len(l1)!=len(l2):
        return 0
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            flag=1
            continue
        break
    if(flag==1):
        print("list is same")
    else:
        print("list is not same")
if __name__ == '__main__':
    l1,l2= input("Enter two lists")
    r=comparetwolist(l1,l2)