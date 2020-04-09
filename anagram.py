n = int(input())
while(n>0):
  a = input()
  b = input()
  c = b
  r= 0
  for i in a:
   d = b.find(i)
   if(d<0):
     r=r+1
   else:
     b = b[0:d]+b[d+1:]
  for i in c:
    d = a.find(i)
    if(d<0):
     r=r+1
    else:
     a = a[0:d]+a[d+1:]
  print(r)
  n=n-1