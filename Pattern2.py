def pattern(num):
    for i in range(5,0,-1):
        for j in range(0,i):
            print '*',

        print
if __name__ == '__main__':
    num = input("Enter number of rows")
    r=pattern(num)





