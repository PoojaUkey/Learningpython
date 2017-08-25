def intersection(list1,list2):
    listele1=[]
    listele2=[]
    for x in range(0,list1):
        ele1=int(input("Enter elements for list1"))
        listele1.append(ele1)
    for x in range(0,list2):
        ele2 = int(input("Enter elements for list2"))
        listele2.append(ele2)
        a=list(listele1)&(listele2)
        print intersection(ele1, ele2)
    print("The intersection is :")

if __name__=="__main__":
    list1 = input("enter number of elements in list 1")
    list2 = input("enter number of elements in list 2")
    intersection(list1,list2)