# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:32:52 2020

@author: meroo

AirPollution: Module 4 HW
"""

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------------- #
# -- Stability Conditions 
# --------------------------------------------------------------- #

A = {'a': 213, 'b': 0.894, 'c': [440.8, 459.7], 'd': [1.941, 2.094], 'f': [9.27, -9.6]}
B = {'a': 156, 'b': 0.894, 'c': [106.6, 108.2], 'd': [1.149, 1.098], 'f': [3.3, 2.0]}
C = {'a': 104, 'b': 0.894, 'c': [61.0, 61.0], 'd': [0.911, 0.911], 'f': [0, 0]}
D = {'a': 68, 'b': 0.894, 'c': [33.2, 44.5], 'd': [0.725, 0.516], 'f': [-1.7, -13.0]}
E = {'a': 50.5, 'b': 0.894, 'c': [22.8, 55.4], 'd': [0.678, 0.305], 'f': [-1.3, -34.0]}
F = {'a': 34, 'b': 0.894, 'c': [14.35, 62.6], 'd': [0.740, 0.180], 'f': [-0.35, -48.6]}

def steady_state(Q, x, stability, u, y, z, H):
    
    sig_y = stability['a'] * x ** stability['b']
    
    if x < 1:
        sig_z = stability['c'][0] * x ** stability['d'][0] + stability['f'][0]
    else:
        sig_z = stability['c'][1] * x ** stability['d'][1] + stability['f'][1]

    C = Q / (2 * np.pi * u * sig_y * sig_z)
    C *= np.exp(0.5 * ((y**2) / (sig_y**2)))
    C *= np.exp( -0.5 * ( (z - H)**2 / (sig_z)**2 ) ) + np.exp( -0.5 * ( (z - H)**2 / (sig_z)**2 ) )
    return C

# --------------------------------------------------------------- #
# -- 20.10: Stability Class D
# --------------------------------------------------------------- #

H = 150; Q = 800e6; u = 8; x = [0.5, 1, 2, 4, 7, 10, 15]; y = 0; z = 0    
C = []
for i in range(len(x)):
    s = steady_state(Q, x[i], D, u, y, z, H)
    print(s)
    C.append(s)
    

#%% Problem 2a

def problem2a():
    Q = 800e6; u = 8; x = np.arange(0.001, 50, 0.001); y = 0; z = 0    
    C1 = []; C2 = []
    for i in range(len(x)):
        C1.append(steady_state(Q, x[i], D, u, y, z, 150))
        C2.append(steady_state(Q, x[i], D, u, y, z, 300))
    
    plt.figure(figsize=(10,6))
    plt.rcParams.update({'font.size': 22})
    plt.plot(x, C1, '-', label='150 m', markersize=0.1, linewidth=2)
    plt.plot(x, C2, '-', label='300 m', markersize=0.1, linewidth=2)
    plt.xlabel('Distance from Point Source (m)', labelpad=10)
    plt.ylabel(u"Concentration (\u03BCg/s)", labelpad=10)
    plt.title('Non-Reactive Pollutant Transport')
    plt.legend(title='Effective Stack Height')
    return

problem2a()

#%% Problem 2b

def problem2b():
    Q = 800e6; u = 8; x = np.arange(0.001, 50, 0.001); y = 0; z = 0    
    C1 = []; C2 = []
    for i in range(len(x)):
        C1.append(steady_state(Q, x[i], D, u, y, z, 150))
        C2.append(steady_state(Q, x[i], A, u, y, z, 150))
    
    plt.figure(figsize=(10,6))
    plt.rcParams.update({'font.size': 22})
    plt.plot(x, C1, '-', label='D', markersize=0.1, linewidth=2)
    plt.plot(x, C2, '-', label='A', markersize=0.1, linewidth=2)
    plt.xlabel('Distance from Point Source (m)', labelpad=10)
    plt.ylabel(u"Concentration (\u03BCg/s)", labelpad=10)
    plt.title('Non-Reactive Pollutant Transport')
    plt.legend(title='Stability Class')
    return

problem2b()

#%% Problem 2c

def problem2c():
    Q = 800e6; u = 8; x = np.arange(0.001, 50, 0.001); y = 0; z = 0    
    C1 = []; C2 = []
    for i in range(len(x)):
        C1.append(steady_state(Q, x[i], D, u, y, z, 150))
        C2.append(steady_state(Q, x[i], D, 4, y, z, 150))
    
    plt.figure(figsize=(10,6))
    plt.rcParams.update({'font.size': 22})
    plt.plot(x, C1, '-', label=f'{u} m/s', markersize=0.1, linewidth=2)
    plt.plot(x, C2, '-', label='4 m/s', markersize=0.1, linewidth=2)
    plt.xlabel('Distance from Point Source (m)', labelpad=10)
    plt.ylabel(u"Concentration (\u03BCg/s)", labelpad=10)
    plt.title('Non-Reactive Pollutant Transport')
    plt.legend(title='Wind Speed')
    return

problem2c()