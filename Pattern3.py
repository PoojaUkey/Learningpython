def pattern(n):
    for i in range(0,n):
        for j in range(0, i):
            print '\t',
            for k in range(n - i, 0, -1):
                print'*\t',
    print('\n')

if __name__ == '__main__':
    n = input("Enter number of rows")
    pattern(n)


