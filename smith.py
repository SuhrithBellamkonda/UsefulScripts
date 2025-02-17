# Plotting a Smith Chart using equations covered in lecture (in parametric form)
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)
R = [0, 0.5, 1, 2, 4, 8]
X = [0.5, 1, 2, 4, 8]

plt.figure(figsize=(7, 7))
plt.gca().set_aspect('equal')

def masked_points(u, v):
    mask = (u**2 + v**2) <= 1
    return u[mask], v[mask]

#Resistance Circles
for r in R: 
    u = r/(1+r) + 1/(1+r) * np.cos(theta)
    v = 1/(1+r) * np.sin(theta)
    u, v = masked_points(u, v)
    plt.plot(u, v, color = "#76cbff")

#Reactance Circles
for x in X:
    u = 1 + (1/x) * np.cos(theta)
    v = (1/x) * (1 + np.sin(theta))
    u1, v1 = masked_points(u, v)
    u2, v2 = masked_points(u, -v)
    plt.plot(u1, v1, color = "#76cbff")
    plt.plot(u2, v2, color = "#76cbff")

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.xlabel("u")
plt.ylabel("v")
plt.title("Smith Chart")
plt.grid(True)
plt.show()