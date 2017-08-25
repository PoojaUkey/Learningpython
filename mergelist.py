def merge(l1,l2):
    l3=[]
    i=0
    j=0
    l1.sort()
    l2.sort()
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    if i<len(l1):
        l3.extend(l1[i:])
    if j<len(l2):
        l3.extend(l2[j:])
        return(l3)
    print(l3)
if __name__ == '__main__':
    l1,l2=input("Enter two lists")
    r = merge(l1, l2)