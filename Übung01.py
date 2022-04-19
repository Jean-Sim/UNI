#! /usr/bin/env python3
# -*- coding: utf-8 -*-

### Vorlagendatei für die Übungen zur Datenverarbeitung ###

# Bitte ergänzen Sie hier die Daten der Abgebenden. Ersetzen Sie nur
# die Punkte ('...'), aber lassen Sie den Rest der Zeilen und ihre Reihenfolge
# ansonsten unverändert, da Ihre Abgabe sonst nicht elektronisch verarbeitet
# werden kann.
#
# 1)
# Matrikelnummer: ...
# Name: ...
# Email: ...
#
# 2)
# Matrikelnummer: ...
# Name: ...
# Email: ...

# Häufig benötigte Module (auskommentieren, wenn notwendig):
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

import time


print("Aufgabe 1")
x, y = sp.symbols('x y')
circ = sp.Eq(x**2 + y**2 + 6*y - 91, 0)
circ_solve = sp.solve(circ, y)
solu = sp.solve(sp.Eq(sp.sqrt(100 - x**2) - 3, (1/9)*x**2 + 1), x)
print(solu)

sp.plot((1/9)*x**2 + 1, circ_solve[-1], circ_solve[0], show=True)

time.sleep(3)

print("")
print("Aufgabe 2")

ex = (1/sp.sqrt(2*sp.pi))*sp.exp(-(x**2)/2)
sp.plot(ex, show=True)

print("integral [-1,1]:")
print(sp.integrate(ex, (x, -1, 1,)).evalf())
print("integral [-2,2]:")
print(sp.integrate(ex, (x, -2, 2,)).evalf())
print("integral [-3,3]:")
print(sp.integrate(ex, (x, -3, 3,)).evalf())
print("integral [-inf,inf]:")
print(sp.integrate(ex, (x, -sp.oo, sp.oo,)).evalf())


time.sleep(3)

print("")
print("Aufgabe 3")


import scipy.constants as sc
import uncertainties


M = uncertainties.ufloat(1.990*10**30, 0.005*10**30)
m = uncertainties.ufloat(5.970*10**24, 0.00*10**24)
a = uncertainties.ufloat(149.6*10**9, 0)
G = uncertainties.ufloat(sc.physical_constants['Newtonian constant of gravitation'][0],
                         sc.physical_constants['Newtonian constant of gravitation'][-1])
c = a*m
T = sp.sqrt(((a**3)*(4*sc.pi**2))/(G*(M+m)))

print(f"Die Umlaufzeit ist: {T}")
