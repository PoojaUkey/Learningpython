def pattern(n):
    for i in range(0,n):
        ch=65
        for j in range(0,i):
            print'%c\t'%ch,
        print('\n')
        ch=ch+1
if __name__ == '__main__':
    n = input("Enter  number")
    r=pattern(n)