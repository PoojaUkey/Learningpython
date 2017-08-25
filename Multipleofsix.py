#!user/bin/python
n=input("Enter range")
sum=0
for x in range(6,n+1,6):
 sum+=x
print ("Sum of multiple of 6 upto %d is %d"%(n,sum))