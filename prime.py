def prime( n):
 if n in l:
  return True
 else:
  for i in l:
   if(n%i==0):
    return False
  l.append(n)
  return True
l=[2,3,5,7,11,13]
n = int(input())
for i in range(2,n):
    b  = prime(i)
    if(b):
       print(i,end=" ") 