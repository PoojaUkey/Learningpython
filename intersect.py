def intersect(l1, l2):
  l1.sort()
  l2.sort()
  i,j = 0,0
  l3 = []
  while i < len(l1) and j < len(l2):
      if l1[i] == l2[j]:
          l3.append(l1[i])
          i += 1
          j += 1
      elif(l1[i]<l2[j]):
          i+=1
      else:
          j+=1
  print(l3)
if __name__ == '__main__':
    l1, l2 = input("Enter two lists")
    r = intersect(l1,l2)