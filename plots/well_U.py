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
V0 = 0.04
top = 30 * V0
L = 1.8*a
xmax = a

def Well_potential (x):
    return V0 * np.tan (np.pi*x/2./a)**2
def Harmonic_potential (x):
    return V0 * (np.pi*x/2./a)**2

# create a time array from 0..t_stop sampled at 0.02 second steps

# integrate your ODE using scipy.integrate.
dx = 0.01
x = np.arange (-xmax, xmax, dx)
xhar = np.arange (-L, L, dx)
U = Well_potential (x)
Uhar = Harmonic_potential (xhar)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(0., top))
fmt = "{:.2f}"
ax.set_title ("Well potintial")
ax.grid()
ax.plot (x, U, ',-', label='Well')
ax.plot (xhar, Uhar, ',-', label='Harmonic')
ax.vlines ([-a, a], ymin=0., ymax=top, color="red", label='Wall')
ax.hlines (0., xmin=-a, xmax=a, color="red")
ax.set(xlabel='x [a. u.]')
ax.set(ylabel='U [a. u.]')
ax.legend ()
plt.show ()