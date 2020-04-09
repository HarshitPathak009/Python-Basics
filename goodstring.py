(n,k,m) = map(int,input().strip().split())
s = input()
l=0
n=""
for i in range(0,len(s),4):
    sub = s[i:k+i]
    c  = sub.count("1")
    if(c>m):
     r = c-m 
     for j in range(k):
        if(r==0):
           break
        if(sub[j]=="1"):
          sub  = sub[0:j]+"0"+sub[j+1]
          l+=1
          r-=1
    elif(c<m):
     r=m-c
     for j in range(k):
        if(r==0):
           break
        if(sub[j]=="1"):
          sub  = sub[0:j]+"0"+sub[j+1]
          l+=1
          r-=1
    n+=sub
print(l)
print(n)