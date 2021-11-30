#--------------------------------------------------------------------------------
#---this program is supposed to model the electric field of----------------------
#----------a dipole and to find its dipole moment--------------------------------
#--------------------------------------------------------------------------------





import numpy as np
import matplotlib.pyplot as plt

yo=[]
zo=[]
i=-10
n=1-i
#----------------------------building the grid---------------------

while i != n:
    if i==0:
        yo.append(0)
    else:
        yo.append(i)
    i+=1
zo=yo


#---------------------------electric field grid---------------------

    
q=1 #C
d= 10**-2 #m
p=q*d 
e= 8.85418782*(10**-12)
Ez=[]
Ey=[]


def E1(y,z):
    #horizontal
    return (p/(4*np.pi*e))*(3*y*z/((y**2+z**2)**(5/2)))
    

def E2(y,z):
    return ((-p/(4*np.pi*e))*((1/((y**2+z**2)**(3/2)))-((3*z**2)/((y**2+z**2)**(5/2)))))


#----------------------------------------------------------------------
#----------------------------printing results--------------------------


print("dipole charge (Q)=", q, "C")
print("dipole separation distance (d)=", d, "m")
print("dipole moment=", p, "C-m")


#-----------------------------------------------------------------------


i=0

while i != len(yo):
    j=0
    while j != len(zo):
        if yo[i]==0:
            if zo[j]==0:
                exit
            elif zo[j] != 0:
                plt.quiver(yo[i],zo[j],E1(yo[i],zo[j]),E2(yo[i],zo[j]))    
        else:
            plt.quiver(yo[i],zo[j],E1(yo[i],zo[j]),E2(yo[i],zo[j]))
        j+=1
    i+=1


plt.show()










