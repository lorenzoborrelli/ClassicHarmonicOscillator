import matplotlib.pyplot as plt
import math as m

v=0.0   #Velocità Iniziale
h=0.01  #Passo
x=5.0   #Posizione Iniziale
g=9.8

#k=16.0, m=1.0

w=m.sqrt(16.0)

t=0.0
ta,xa,xb=[],[],[]

while t<16.0:

    ta.append(t)
    xa.append(x)
    xb.append(5*m.cos(w*t))

    v=v-(w*w)*x*h               #k=16.0, m=1.0, w=4.0
    x=x+v*h
    t=t+h

plt.figure()

plt.plot(ta,xa)                 #ta,xb

plt.xlabel('$t$ $[a.u.]$')      #t(s)
plt.ylabel('$x(t)$ $[a.u.]$')   #(m)

plt.show()
