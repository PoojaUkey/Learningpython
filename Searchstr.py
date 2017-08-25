def search(str1,str2):
    index=0
    count=0
    while index!=-1:
        index=input_string.find(search.string)
        if index!=-1:
          count+=1
          input_string=input_string[index+1:]
    print(search)
if __name__ == '__main__':
    str1,str2=input("Enter string")
    r = search(str1,str2)