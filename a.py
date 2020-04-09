def area():
  (x1,y1)=map(int,input("Enter the coordinates of centre").strip().split())
  (x2,y2)=map(int,input("Enter the coordinates of point on perimeter").strip().split())
  area = 3.14*((((x1-x2)**2+(y1-y2)**2)**0.5)**2)  
  print("The area of circle is {} unit sq.".format(area))
area()