#!usr/bin/python
def gcd(num1,num2):
    while num1!=num2:
        if num1>num2:
            num1=num1-num2
        else:
           num2=num2-num1
    return num1
if __name__=='__main__':
    num1,num2=input("Enter number1 and number2")
    result=gcd(num1,num2)
    print(num1,num2,result)
