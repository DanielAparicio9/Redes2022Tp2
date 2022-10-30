#--------------------------Librerias--------------------------------------------
import numpy as np
import scipy as sp
import scipy.linalg as linalg
import matplotlib.pyplot as plt
import math
#------------------------------------------------------------------------------



#--------------------Función Rk4-2d----------------------------------------
def rk4(f1,f2,t,x,y,h):
    m1 = f1(t,x,y)
    k1 = f2(t,x,y)
    m2 = f1(t+0.5*h,x+0.5*h*m1,y+0.5*h*k1)
    k2 = f2(t+0.5*h,x+0.5*h*m1,y+0.5*h*k1)
    m3 = f1(t+0.5*h,x+0.5*h*m2,y+0.5*h*k2)
    k3 = f2(t+0.5*h,x+0.5*h*m2,y+0.5*h*k2)
    m4 = f1(t+h,x+0.5*h*m3,y+0.5*h*k3)
    k4 = f2(t+h,x+0.5*h*m3,y+0.5*h*k3)
    return np.array([h*(m1+2.0*m2+2.0*m3+m4)/6.0,h*(k1+2.0*k2+2.0*k3+k4)/6.0])
#-----------------------------------------------------------------------


#--------------------------------Función v(t)-----------------------------------------------------
def f1(t,v,u):
  I=0
  if t>50.0:
    I=10.0
  return (0.04*v*v+5.0*v+140-u+I)
#------------------------------------------------------------------------------------------------------

#--------------------------------Función u(t)-----------------------------------------------------------
def f2(t,v,u):
    a = 0.02
    b = 0.2
    return (a*(b*v-u))
#------------------------------------------------------------------------------------------------------

#------------------------------Condiciones Iniciales----------------------------------------------------
tf=200#Tiempo final
c=-50.0
d=2.0
h=0.01#Paso
k=math.trunc(tf/h)
t = np.zeros(k+1)
v1 = np.zeros(len(t))
u1 = np.zeros(len(t))
t[0]=0
v1[0]=-70.0
u1[0]=0.2*v1[0]
b=np.array([[1],[2]])
#------------------------------------------------------------------------------------------------------


#----------------------------------------Simulación---------------------------------------------------
for i in range(k): 
   b=rk4(f1,f2,t[i],v1[i],u1[i],h) 
   v1[i+1]=v1[i]+b[0]
   u1[i+1]=u1[i]+b[1]
   t[i+1]=t[i]+h
   if v1[i+1]>=30:
      v1[i+1]=c
      u1[i+1]=u1[i+1]+d
#-----------------------------------------------------------------------------------------------------

#------------------------------------Corriente en función tiempo----------------------------------------
def IC(p):
 if p<50.0:
   return 0
 else:
   return 10
#--------------------------------------------------------------------------------------------------------


#---------------------------------------Grafica---------------------------------------------------------
plt.xlabel('$t$')
plt.plot(t,v1,label="$v(t)$",linestyle='-',c='blue')
plt.plot(t,u1,label="$u(t)$",linestyle='-',c='green')
plt.plot(t,np.vectorize(IC)(t),label="$I(t)$",linestyle='-',c='red')
plt.title('chattering (CH)')
plt.legend()
plt.show()
#--------------------------------------------------------------------------------------------------------