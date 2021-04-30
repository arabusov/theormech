#!/usr/bin/env python3
#
# MIT License
#
# Copyright (c) 2021 Andrei Rabusov
# Derived from matplotlib.animation example for double pendulum
#
# This script plots potential well:
#                      pi x
#  U (x) = V_0 tg**2 (-----)
#                      2 a
#

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

m = 1.0  # mass of pendulum 1 in kg
a = 1.0
V0 = 0.04
top = 3 * V0
L = 1.8*a
xmax = a

def Well_potential (x):
    return V0 * np.tan (np.pi*x/2./a)**2
def Harmonic_potential (x):
    return V0 * (np.pi*x/2./a)**2
def math_pendulum (x):
    return V0 * np.sin (np.pi*x/2./a)**2

# create a time array from 0..t_stop sampled at 0.02 second steps

# integrate your ODE using scipy.integrate.
dx = 0.01
x = np.arange (-xmax, xmax, dx)
xhar = np.arange (-L, L, dx)
U = Well_potential (x)
Umath = math_pendulum (xhar)
Uhar = Harmonic_potential (xhar)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(0., top))
fmt = "{:.2f}"
ax.set_title ("Well potintial")
ax.grid()
ax.plot (x, U, ',-', label='Well')
ax.plot (xhar, Umath, ',-', label='Math', color='green')
ax.plot (xhar, Uhar, ',-', label='Harmonic')
ax.vlines ([-a, a], ymin=0., ymax=top, color="red", label='Wall')
ax.hlines (0., xmin=-a, xmax=a, color="red")
ax.set(xlabel='x [a. u.]')
ax.set(ylabel='U [a. u.]')
ax.legend ()
plt.show ()
