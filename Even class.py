#!user/bin/python
n=input("Enter upper bound")
sum=0
for x in range(2,n+1,2):
    sum+=x
print("Sum of even  no.s upto %d is %d"%(n,sum))