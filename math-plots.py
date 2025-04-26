import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Task 1: Plot a function y = x^2 * e^(-x)
x = np.arange(-1, 2, 0.1)
y = x**2 * np.exp(-x)
plt.plot(x, y)
plt.show()

# Task 2: Parametric plot using trigonometric expressions
a = 10
b = 2
c = 0.25
t = np.arange(0, 10 * np.pi, 0.1)
x = a * np.cos(c * t) - b * np.cos(t + c * t)
y = a * np.sin(c * t) - b * np.sin(t + c * t)
plt.plot(x, y)
plt.axis('equal')  # Maintain aspect ratio
plt.show()

# Task 3: 3D surface plot of a combined sine function
h = float(input("Enter step size: "))

a = 2
b = 5
x = np.arange(-2 * np.pi, 2 * np.pi, h)
y = np.arange(-2 * np.pi, 2 * np.pi, h)
X, Y = np.meshgrid(x, y)
Z = a * np.sin(X) + b * np.sin(Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')  # Color map for better visualization
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.show()
