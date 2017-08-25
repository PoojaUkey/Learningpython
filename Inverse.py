def inverse(list1,list2):
    listele1=[]
    listele2=[]
    for x in range(0,list1):
        ele1=int(input("Enter elements for list1"))
        listele1.append(ele1)
    for x in range(0,list2):
        ele2 = int(input("Enter elements for list2"))
        listele2.append(ele2)
        a=list(set(listele1)^set(listele2))
    print("The inverse is :")
    print(a)
if __name__=="__main__":
    list1 = input("enter number of elements in list 1")
    list2 = input("enter number of elements in list 2")
    inverse(list1,list2)