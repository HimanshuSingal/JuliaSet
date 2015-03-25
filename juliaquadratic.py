# Author	Himanshu Singal
# Roll No	B13312
# Title		Julia Set plot for f(z)=z^2+c
import cmath
x=input('Enter real part of constant')
y=input('Enter complex part of constant')
c=complex(x,y)
scale=1000
start=-10.0
end=10.0
fout = open('out','w')
fact=(end-start)/(scale)

re=start
im=start
for y in range(1,scale+1):
 re=start
 for x in range(1,scale+1):
  z=complex(re,im)
  k=1
  while abs(z)<10:
   z=z*z+c
   if k == 25:
     break
   k=k+1
  if k==25:
   fout.write(str(re)+' '+str(im)+'\n')
  re=re+fact
 im=im+fact
fout.close()
