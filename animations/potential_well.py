#!/usr/bin/env python3
#
# MIT License
#
# Copyright (c) 2021 Andrei Rabusov
# Derived from matplotlib.animation example for double pendulum
#
# This script animates (x, t) plot for 1D potential well with
#                      pi x
#  U (x) = V_0 tg**2 (-----)
#                      2 a
#
# Change line No. 34 from E = V0 to E = 0.1 * V0 or E = 100 * V0
# to study different cases

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

m = 1.0  # mass of pendulum 1 in kg
a = 1.0
V0 = 1.0
L = 2*a

def Well_solution (t, E):
    return 2*a/np.pi * np.arcsin(np.sqrt (E/(V0+E)) * \
            np.sin (np.pi /2./a*np.sqrt (2*(V0+E)/m)*t))
def period (E):
    return 4*a*np.sqrt (m/2./(V0+E))
    

# initial state
E =  V0
T = period (E)

# create a time array from 0..t_stop sampled at 0.02 second steps
dt = 0.005
t_stop = 5  # how many seconds to simulate
history_len = int (np.ceil (t_stop / dt))
t = np.arange(0, t_stop, dt)
show_T = t_stop
x_scale=show_T/L

# integrate your ODE using scipy.integrate.

x = x_scale*Well_solution (t, E)
L = x_scale*L/2.
y = t

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(0., show_T))
fmt = "{:.2f}"
ax.set_title ("E/V_0 = "+fmt.format (E/V0))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], ',-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
history_x, history_y = deque(maxlen=history_len), deque(maxlen=history_len)

def animate(i):
    thisx = [0, x[i]]
    thisy = [0, y[i]]

    if i == 0:
        history_x.clear()
        history_y.clear()

    history_x.appendleft(thisx[1])
    history_y.appendleft(thisy[1])

#    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)
    time_text.set_text(time_template % (i*dt))
    return line, trace, time_text


ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()

