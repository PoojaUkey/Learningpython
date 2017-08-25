#!usr/bin/python
def armstrong(num):
    sum=0
    temp=num
    while(num!=0):
        rem=num%10
        sum=sum+rem*rem*rem
        num=int(num/10)
        if(temp==sum):
            print("number is armstrong")
        else:
            print("number is not armstrong")
if __name__ == '__main__':
    num=input("Enter number")
    result = armstrong(num)
