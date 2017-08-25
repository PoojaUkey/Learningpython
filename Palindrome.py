#!usr/bin/python
def palindrome(num):
    rev=0
    temp=num
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=int(num/10)
    if(temp==rev):
        print("number is palindrome")
    else:
        print("number is not palindrome")
if __name__ == '__main__':
    num=input("Enter number")
    result = palindrome(num)
