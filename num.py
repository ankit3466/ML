import numpy as np

r=int(input("Enter no of row"))
c=int(input("Enter no of cplumn"))

z=np.random.random((r,c))
#print(z)

f=open('numpy.txt','w')
f.write(str(z))
f.close()
