def pattern(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print'\t',
        for j in range(0,2*i+1):
            print'*\t',
        print("\n")
if __name__ == '__main__':
    n=input("Enter number ")
    r=pattern(n)