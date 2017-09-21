def longestshortestline(name):
    fd=open(name)
    if fd!=None:
        line=fd.readline()
        max_line=line
        min_line=line
        while line!="":
            line=fd.readline()
            if line=="":
                break
            if len(line)>len(max_line):
                max_line=line
            if len(line)<len(min_line):
                min_line=line
    return max_line,min_line
    #print(max_line,min_line)
def main():
    name=input("enter line")
    max_line,min_line=longestshortestline(name)
    print(max_line,min_line)
if __name__=='__main__':
    main()
