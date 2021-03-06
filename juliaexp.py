# Author	Himanshu Singal
# Roll No	B13312
# Title		Julia Set plot for f(z)=e^(z^3)-0.621
import cmath
c=complex(-0.621,0)
scale=1000
fout = open('out','w')
fact=4.0/(scale)
re=-2.0
im=-2.0
for y in range(1,scale+1):
 re=-2.0
 for x in range(1,scale+1):
  z=complex(re,im)
  k=1
  while abs(z)<8:
   z=cmath.e**(z*z*z) + c
   if k == 25:
     break
   k=k+1
  if k==25:
   fout.write(str(re)+' '+str(im)+'\n')
  re=re+fact
 im=im+fact
fout.close()
