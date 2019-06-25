# importing numpy library
import numpy as np

# taking inputs from user
r=int(input("Enter no of row"))
c=int(input("Enter no of cplumn"))

# creating array of user's dimensions
z=np.random.random((r,c))
#print(z)

# writing the content in a file using file handling
f=open('numpy.txt','w')
f.write(str(z))
f.close()
