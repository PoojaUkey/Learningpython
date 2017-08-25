def Add(*args):
    sum=0
    for x in args:
        sum+=x
    return sum
res=Add(1,2,3)
print(res)
