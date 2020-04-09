t = int(input())
while(t):
    (a,b,n)=map(int,input().split())
    j=a^b
    if(j>2**(n-1)):
        print(b)
    else:
        print(min(a,b)-~(j))
    t=t-1