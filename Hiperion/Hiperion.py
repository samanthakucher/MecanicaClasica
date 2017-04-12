# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

def h(x, t, G, l, M):
    R, Rv, T, Tv, F, Fv = x
    Ra = R*(Fv**2)-(G*M)/(R**2)-(9*G*M*((np.cos(T-F)**2))*(l**2))/(8*(R**4))
    Fa = (3*G*M*np.sin(2*(T-F))*(l**2))/(8*(R**5))-(2*Rv*Fv)/(R)
    Ta = ((3*G*M)*np.sin(2*(T-F)))/(2*(R**3))
    return [Rv, Ra, Tv, Ta, Fv, Fa]


#variables
t0 = 0
tf = 1000000
dt = 0.1
t = np.arange(t0, tf, dt)
G = 6.674e-11 #N.m**2/kg**2
M = 5.683e26 #kg
l = 360.2e3 #m

#condiciones iniciales
x0 = [981009e3, 0.001, 0, 0.01, 0, 0.00000633827] 
#x0 = [981009e3, 0.001, 0, 0.01, 0, 0.00000633827] #hace la vuelta entera
 
sol = odeint(h, x0, t, args = (G, l, M,)) #integra

#Radio constante:
#sol[:,0] = 1481009e3
#sol[:,1] = 0

x1 = sol[:,0]*np.cos(sol[:,4]) + (l/2)*np.cos(sol[:,2])
y1 = sol[:,0]*np.sin(sol[:,4]) + (l/2)*np.sin(sol[:,2])

x2 = sol[:,0]*np.cos(sol[:,4]) - (l/2)*np.cos(sol[:,2])
y2 = sol[:,0]*np.sin(sol[:,4]) - (l/2)*np.sin(sol[:,2])

#graficos
fig,sub = plt.subplots(2, figsize =(8,8))
sub[0].plot(t,sol[:,0])
sub[0].set_xlabel('tiempo')
sub[0].set_ylabel('Radio')
sub[1].plot(x1, y1, 'r-', label = 'masa 1')
sub[1].plot(x2, y2, 'b-', label = 'masa 2')
sub[1].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[1].set_xlabel('x')
sub[1].set_ylabel('y')
#sub[2].plot(x1, y1, 'r-', label = 'masa 1')
#sub[2].plot(x2, y2, 'b-', label = 'masa 2')
#sub[2].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#sub[2].set_xlabel('x')
#sub[2].set_ylabel('y')
#sub[2].set_xlim([7.48e3,7.6e3])
#sub[2].set_ylim([7.48e3,7.6e3])



#¡Animacion!:
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1.5e9, 1.5e9), ylim=(-1.5e9, 1.5e9))
ax.grid()

line, = ax.plot([], [], 'o-', lw=1, color='g')
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

#Pongo "el fondo" de cada cuadro de la animacion
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

#Defino la animacion
def animate(i):
    x1ok = [0, x1[i]]
    y1ok = [0, y1[i]]
    x2ok = [0, x2[i]]
    y2ok = [0, y2[i]]


    line.set_data([x1ok, x2ok], [y1ok, y2ok])
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(sol)),
                              interval=25, blit=True, init_func=init)

plt.draw()
plt.show()














