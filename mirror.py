def pattern(num):
    for j in range(1,num+1):
        for i in range(1, i + 1):
            print '*',
        print
if __name__ == '__main__':
    num = input("Enter number of rows")
    r=pattern(num)
