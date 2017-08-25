def cube(num):
    sum=0
    for x in range(0,num):
        n = input("Enter number of cube")
        cube=n*n*n
        sum = sum+cube
    print("Sum of cube of numbers is %d"%sum)
if __name__ =="__main__":
        num = input("Enter number")
        cube(num)



