def sumofdigits(string1):
    i=0
    sum=0
    while i<len(string1):
        if string1[i].isdigit():
            sum+=int(string1[i])
        i+=1
    return sum

if __name__ == '__main__':
     string1=input("Enter alphanumeric string")
     r=sumofdigits(string1)
     print(r)
