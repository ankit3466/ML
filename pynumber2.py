a=[]
for i in range(100,125):
  j=i+16*5
  z=np.arange(i,j,5).reshape((8,2))
  a.append(z)
  
##Printing each matrix
for i in a:
  print(i)
