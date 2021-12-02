#this program should simulate a point charge

import matplotlib.pyplot as plt
import numpy as np

xo=[]
yo=[]

n=-10
i=n

while i != -n+1 :
    xo.append(i)
    i+=1
yo=xo

x,y=np.meshgrid(xo,yo)

#-----------------------------------------------------------

e=9*10**-12
q=4*10**-6
d=0.05
p=q*d


def Ex(y,z):
    return (p/(4*np.pi*e))*(3*y*z/((y**2+z**2)**(5/2)))

def Ey(y,z):
    return ((-p/(4*np.pi*e))*((1/((y**2+z**2)**(3/2)))-((3*z**2)/((y**2+z**2)**(5/2)))))
#---------------------------------------------------------------
print("dipole charge (Q)=", q, "C")
print("dipole separation distance (d)=", d, "m")
print("dipole moment=", p, "C-m")
#---------------------------------------------------------------
i=0
E1=[]
Ex1=np.array([])
while i != len(xo):
    j=0
    while j != len(yo):
        if xo[i]==0 and yo[j]==0:
            E1.append(0)
            j+=1
        else:
            E1.append(Ex(xo[i],yo[j]))    
            j+=1
    i+=1
Ex1=np.append(Ex1,E1)
Ex2=Ex1.reshape(len(xo),len(xo))
#---------------------------------------------
i=0
E1=[]
Ey1=np.array([])
while i != len(xo):
    j=0
    while j != len(yo):
        if xo[i]==0 and yo[j]==0:
            E1.append(Ey(0.001,0.001))
            j+=1
        else:
            E1.append(Ey(xo[j],yo[i]))    
            j+=1
    i+=1
Ey1=np.append(Ey1,E1)
Ey2=Ey1.reshape(len(yo),len(yo))


#---------------------------------------------------------------

plt.streamplot(x,y,Ex2, Ey2)
plt.show()
