# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:30:33 2016

@author: SAMI
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

#p1 = posicion de la masa 1 
#p1v = velocidad
#p1a = aceleracion

#Para ver distintas condiciones iniciales (con datos experimentales para contrastar)
#comentar y descomentar lo que diga "video 1,2,3": el x0, tf, b y los subplots

#5 pendulos acoplados con resortes
def resortes(p, t, k, m, g, l, b, a):
    p1, p1v, p2, p2v, p3, p3v, p4, p4v, p5, p5v = p
    if abs(p1-p2)>=a :
        F12 = 0
    else:
        F12 = (k/m)*(p1-p2)
    if abs(p2-p3)>=a :
        F23 = 0
    else:
        F23 = (k/m)*(p2-p3)
    if abs(p3-p4)>=a :
        F34 = 0
    else:
        F34 = (k/m)*(p3-p4)
    if abs(p4-p5)>=a:
        F45 = 0
    else:
        F45 = (k/m)*(p4-p5)
    p1a = - F12 - (g/l)*p1 - b*p1v
    p2a = F12 - F23 - (g/l)*p2 - b*p2v
    p3a = F23 - F34 - (g/l)*p3 - b*p3v
    p4a = F34 - F45 - (g/l)*p4 - b*p4v
    p5a = F45 - (g/l)*p5 - b*p5v
    return [p1v, p1a, p2v, p2a, p3v, p3a, p4v, p4a, p5v, p5a]
   
#Constantes del problema 
k = 2000 #cte del "resorte" --> inf
m = 0.0211 #masa de las bolitas
g = 9.82
l = 0.10 #longitud del hilo
b = 1.42e-10 #Factor de atenuacion #video 1
#b = 5.6e-11 #video 2
#b = 1.11e-10 #video 3
#b = 2.23541e-10 #video 4
a = 0.016 #distancia entre las masas, en reposo (o sea el diametro de las bolitas)
dt = 0.0001 #intervalo temporal
t0 = 0
tf = 6.015887260 #video 1 #tiempo final
#tf = 6.389138465 #video 2
#tf = 7.147606383 #video 3
#tf = 11.1014802 #video 4
t = np.arange(t0, tf, dt) #tiempo

#Condiciones iniciales:
#Esto es [posicion 1, velocidad 1, posicion 2, velocidad 2, ...]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0.01705602529 ,0] #video 1
#x0 = [-0.010134105249999997, 0, 0, 0, 0, 0, 0, 0, 0 ,0] #video 2
#x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0.009640239670000002 ,0] #video 3
#x0 = [-0.01836715252, 0, 0, 0, 0, 0, 0, 0, 0.01957167564, 0] #video 4

#La posicion inicial esta medida desde el punto de equilibrio de cada masa
# O sea si pongo todo 0, m1 esta en -2a, m2 en -a, m3 en 0, m4 en a y m5 en 2a, y no se mueven

sol = odeint(resortes, x0, t, args = (k, m, g, l, b, a,)) #integra

#Recupero las coordenadas x e y de la solucion:
x1 = l*np.sin(sol[:,0]) - 2*a
x2 = l*np.sin(sol[:,2]) - a
x3 = l*np.sin(sol[:,4])
x4 = l*np.sin(sol[:,6]) + a
x5 = l*np.sin(sol[:,8]) + 2*a
y1 = -l*np.cos(sol[:,0])
y2 = -l*np.cos(sol[:,2])
y3 = -l*np.cos(sol[:,4])
y4 = -l*np.cos(sol[:,6])
y5 = -l*np.cos(sol[:,8])

#Datos experimentales
#Pongo que inicialmente los quietos estan en x=0 (coherente con las cond. iniciales)
#Video 1:
video1data1 = np.loadtxt("v1f1.txt")
video1xdata1 = video1data1[:,1] - -3.302106449E-2
video1data2 = np.loadtxt("v1f2.txt")
video1xdata2 = video1data2[:,1] - -1.634032057E-2
video1data3 = np.loadtxt("v1f3.txt")
video1xdata3 = video1data3[:,1] - -1.708217503E-4
video1data4 = np.loadtxt("v1f4.txt")
video1xdata4 = video1data4[:,1] - 1.634032057E-2
video1data5 = np.loadtxt("v1f5.txt")
video1xdata5 = video1data5 [:,1] - 2.958319317E-2

#Video 2:
video2data1 = np.loadtxt("v2f1.txt")
video2xdata1 = video2data1[:,1] - -3.571827356E-2
video2data2 = np.loadtxt("v2f2.txt")
video2xdata2 = video2data2[:,1] - -1.599977245E-2
video2data3 = np.loadtxt("v2f3.txt")
video2xdata3 = video2data3[:,1] - 1.623069700E-4
video2data4 = np.loadtxt("v2f4.txt")
video2xdata4 = video2data4[:,1] - 1.599889274E-2
video2data5 = np.loadtxt("v2f5.txt")
video2xdata5 = video2data5[:,1] - 3.249262380E-2

#Video 3:
video3data1 = np.loadtxt("v3f1.txt")
video3xdata1 = video3data1[:,1] - -3.232989691E-2
video3data2 = np.loadtxt("v3f2.txt")
video3xdata2 = video3data2[:,1] - -1.616494845E-2
video3data3 = np.loadtxt("v3f3.txt")
video3xdata3 = video3data3[:,1] - -1.649484536E-4
video3data4 = np.loadtxt("v3f4.txt")
video3xdata4 = video3data4[:,1] - 1.566666667E-2
video3data5 = np.loadtxt("v3f5.txt")
video3xdata5 = video3data5[:,1] - 3.473089435E-2

#Video 4:
video4data1 = np.loadtxt("v4f1.txt")
video4xdata1 = video4data1[:,1] - -3.260614578E-2
video4data2 = np.loadtxt("v4f2.txt")
video4xdata2 = video4data2[:,1] - -1.637098631E-2
video4data3 = np.loadtxt("v4f3.txt")
video4xdata3 = video4data3[:,1] - -1.860339354E-4
video4data4 = np.loadtxt("v4f4.txt")
video4xdata4 = video4data4[:,1] - 1.655702025E-2
video4data5 = np.loadtxt("v4f5.txt")
video4xdata5 = video4data5[:,1] -3.326196201E-2

#Errores tracker
errx1 = 0.03324*np.ones(len(video1xdata1))
erry1 = 1.13124e-4*np.ones(len(video1xdata1))
errx2 = 0.03328*np.ones(len(video2xdata1))
erry2 = 3.10128e-4*np.ones(len(video2xdata1))
errx3 = 0.03324*np.ones(len(video3xdata1))
erry3 = 2.11075e-5*np.ones(len(video3xdata1))
errx4 = 0.03334*np.ones(len(video4xdata1))
erry4 =4.18548e-6*np.ones(len(video4xdata1))

#Graficos
fig,sub = plt.subplots(5, figsize =(8,8))
fig.subplots_adjust(hspace=0.7)
sub[0].plot(t,sol[:,0], 'b-', label = "m1")
sub[0].plot(video1data1[:,0], video1xdata1, "k-", label ="m1exp") #video 1
sub[0].errorbar(video1data1[:,0], video1xdata1, erry1, errx1, ecolor='k', linestyle = 'None')
#sub[0].plot(video2data1[:,0], video2xdata1, "k-", label ="m1exp") #video 2
#sub[0].errorbar(video2data1[:,0], video2xdata1, erry2, errx2, ecolor='k', linestyle = 'None')
#sub[0].plot(video3data1[:,0], video3xdata1, "k-", label ="m1exp") #video 3
#sub[0].errorbar(video3data1[:,0], video3xdata1, erry3, errx3, ecolor='k', linestyle = 'None')
#sub[0].plot(video4data1[:,0], video4xdata1, "k-", label ="m1exp") #video 4
#sub[0].errorbar(video4data1[:,0], video4xdata1, erry4, errx4, ecolor='k', linestyle = 'None')
sub[0].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[0].set_title('Posicion en funcion del tiempo')
sub[0].set_xlabel('tiempo (s)')
sub[0].set_ylabel('posicion (m)')
sub[0].set_xlim([0,tf])
sub[1].plot(t, sol[:,2], 'g-', label = "m2")
sub[1].plot(video1data2[:,0], video1xdata2, "k-", label ="m2exp") #video 1
sub[1].errorbar(video1data2[:,0], video1xdata2, erry1, errx1, ecolor='k', linestyle = 'None')
#sub[1].plot(video2data2[:,0], video2xdata2, "k-", label ="m2exp") #video 2
#sub[1].errorbar(video2data2[:,0], video2xdata2, erry2, errx2, ecolor='k', linestyle = 'None')
#sub[1].plot(video3data2[:,0], video3xdata2, "k-", label ="m2exp") #video 3
#sub[1].errorbar(video3data2[:,0], video3xdata2, erry3, errx3, ecolor='k', linestyle = 'None')
#sub[1].plot(video4data2[:,0], video4xdata2, "k-", label ="m2exp") #video 4
#sub[1].errorbar(video4data2[:,0], video4xdata2, erry4, errx4, ecolor='k', linestyle = 'None')
sub[1].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[1].set_xlabel('tiempo (s)')
sub[1].set_ylabel('posicion (m)')
sub[1].set_xlim([0,tf])
sub[2].plot(t, sol[:,4], 'r-', label = "m3")
sub[2].plot(video1data3[:,0], video1xdata3, "k-", label ="m3exp") #video 1
sub[2].errorbar(video1data3[:,0], video1xdata3, erry1, errx1, ecolor='k', linestyle = 'None')
#sub[2].plot(video2data3[:,0], video2xdata3, "k-", label ="m3exp") #video 2
#sub[2].errorbar(video2data3[:,0], video2xdata3, erry2, errx2, ecolor='k', linestyle = 'None')
#sub[2].plot(video3data3[:,0], video3xdata3, "k-", label ="m3exp") #video 3
#sub[2].errorbar(video3data3[:,0], video3xdata3, erry3, errx3, ecolor='k', linestyle = 'None')
#sub[2].plot(video4data3[:,0], video4xdata3, "k-", label ="m3exp") #video 4
#sub[2].errorbar(video4data3[:,0], video4xdata3, erry4, errx4, ecolor='k', linestyle = 'None')
sub[2].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[2].set_xlabel('tiempo (s)')
sub[2].set_ylabel('posicion (m)')
sub[2].set_xlim([0,tf])
sub[3].plot(t, sol[:,6], 'm-', label = "m4")
sub[3].plot(video1data4[:,0], video1xdata4, "k-", label ="m4exp") #video 1
sub[3].errorbar(video1data4[:,0], video1xdata4, erry1, errx1, ecolor='k', linestyle = 'None')
#sub[3].plot(video2data4[:,0], video2xdata4, "k-", label ="m4exp") #video 2
#sub[3].errorbar(video2data4[:,0], video2xdata4, erry2, errx2, ecolor='k', linestyle = 'None')
#sub[3].plot(video3data4[:,0], video3xdata4, "k-", label ="m4exp") #video 3
#sub[3].errorbar(video3data4[:,0], video3xdata4, erry3, errx3, ecolor='k', linestyle = 'None')
#sub[3].plot(video4data4[:,0], video4xdata4, "k-", label ="m4exp") #video 4
#sub[3].errorbar(video4data4[:,0], video4xdata4, erry4, errx4, ecolor='k', linestyle = 'None')
sub[3].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[3].set_xlabel('tiempo (s)')
sub[3].set_ylabel('posicion (m)')
sub[3].set_xlim([0,tf])
sub[4].plot(t, sol[:,8], 'y-', label = "m5")
sub[4].plot(video1data5[:,0], video1xdata5, "k-", label ="m5exp") #video 1
sub[4].errorbar(video1data5[:,0], video1xdata5, erry1, errx1, ecolor='k', linestyle = 'None')
#sub[4].plot(video2data5[:,0], video2xdata5, "k-", label ="m5exp") #video 2
#sub[4].errorbar(video2data5[:,0], video2xdata5, erry2, errx2, ecolor='k', linestyle = 'None')
#sub[4].plot(video3data5[:,0], video3xdata5, "k-", label ="m5exp") #video 3
#sub[4].errorbar(video3data5[:,0], video3xdata5, erry3, errx3, ecolor='k', linestyle = 'None')
#sub[4].plot(video4data5[:,0], video4xdata5, "k-", label ="m5exp") #video 4
#sub[4].errorbar(video4data5[:,0], video4xdata5, erry4, errx4, ecolor='k', linestyle = 'None')
sub[4].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[4].set_xlabel('tiempo (s)')
sub[4].set_ylabel('posicion (m)')
sub[4].set_xlim([0,tf])

#¡Animacion!:
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-0.05, 0.05), ylim=(-0.15, -0.05))
ax.grid()

line, = ax.plot([], [], 'o-', lw=1, markersize=73, alpha=0.5) #pantalla completa: size=154
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

#Pongo "el fondo" de cada cuadro de la animacion
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

#Defino la animacion
def animate(i):
    x1ok = [-2*a-a/2, x1[i]]
    y1ok = [0, y1[i]]
    x2ok = [-a-a/2, x2[i]]
    y2ok = [0, y2[i]]
    x3ok = [-a/2, x3[i]]
    y3ok = [0, y3[i]]
    x4ok = [a-a/2, x4[i]]
    y4ok = [0, y4[i]]
    x5ok = [2*a-a/2, x5[i]]
    y5ok = [0, y5[i]]
# Esto es [punto del que cuelga el pendulo, masa correspondiente]

    line.set_data([x1ok, x2ok, x3ok, x4ok, x5ok], [y1ok, y2ok, y3ok, y4ok, y5ok])
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(sol)),
                              interval=25, blit=True, init_func=init)

plt.draw()
plt.show()