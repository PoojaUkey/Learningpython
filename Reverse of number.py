#!usr/bin/python
def reverse(num):
    rev=0
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=int(num/10)
    return rev
if __name__ == '__main__':
    num=input("Enter number")
    result = reverse(num)
    print(result)
