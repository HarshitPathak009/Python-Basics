x = [1,"abcd",2,"effgh",[3,4]]
print(x)
y=x[0:50]
print(y)
z=y
print(z)
w=x
print(w)
x[1] = x[1]+'d'
print(x)
y[2]=4;
print(y)
x[1][1]='y' #this line is incorrect you cannot assign y to the location 1,1 directly but ot can be done using concatenation and other processes 
print(x)
z[0]=0
print(z)
w[4][0]=1000
print(w)
a=(x[4][1]==4)
print(a)