def match():
    n = input()
    m = n
    l=[]
    score=[]
    d=dict()
    try:
        while(n.index(":")):
            s1 = n[:n.index(":")]
            n = n[n.index(":")+1:]
            s2 = n[:n.index(":")]
            n = n[n.index(":")+1:]
            if(l.count(s1)==0):
                l.append(s1)
            if(l.count(s2)==0):
                l.append(s2)
            d = set(l)
            print(l)
            if(n[0].isnumeric()):
                n = n[n.index(" ")+1:]
    except:
        print()
    print(d)
match()