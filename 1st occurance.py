def replace(input,replace1):
    return input[0]+input[1:].replace(input[0],replace)


if __name__ == '__main__':
   input,replace1=input("Enter two strings")
   r=replace(input,replace1)
   print(r)

