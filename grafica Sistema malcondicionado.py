import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la matriz A (coeficientes de las ecuaciones)
A = np.array([[0.0001, 1, 1],
              [1, 0.0001, 1],
              [1, 1, 0.0001]])

# Definir el vector b (términos independientes)
b = np.array([1, 2, 3])

# Resolver el sistema de ecuaciones A * x = b
x = np.linalg.solve(A, b)

# Mostrar solución del sistema
print("Solución del sistema original:")
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])

# Crear gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Ejes de la gráfica
x_range = np.linspace(-1, 3, 10)
y_range = np.linspace(-1, 3, 10)
X1, Y1 = np.meshgrid(x_range, y_range)

# Ecuaciones de los planos
# Plane 1: 0.0001*x1 + y1 + z1 = 1
Z1 = (1 - 0.0001 * X1 - Y1)

# Plane 2: x2 + 0.0001*x1 + z2 = 2
Z2 = (2 - X1 - 0.0001 * Y1)

# Plane 3: x3 + y3 + 0.0001*x1 = 0.0001
Z3 = (0.0001 - X1 - Y1)

# Graficar los planos
ax.plot_surface(X1, Y1, Z1, alpha=0.5, rstride=100, cstride=100, color='red', label='Plane 1')
ax.plot_surface(X1, Y1, Z2, alpha=0.5, rstride=100, cstride=100, color='blue', label='Plane 2')
ax.plot_surface(X1, Y1, Z3, alpha=0.5, rstride=100, cstride=100, color='green', label='Plane 3')

# Agregar las soluciones originales y perturbadas
ax.scatter(x[0], x[1], x[2], color='black', s=100, label='Solución Original')

# Pequeño cambio en A para mostrar su impacto
A_perturbada = A.copy()
A_perturbada[2, 2] += 0.0001  # Perturbación en la posición (3,3)

# Resolver el sistema perturbado
x_perturbado = np.linalg.solve(A_perturbada, b)

# Mostrar solución del sistema perturbado
print("\nSolución del sistema perturbado:")
print("x1 =", x_perturbado[0])
print("x2 =", x_perturbado[1])
print("x3 =", x_perturbado[2])

# Agregar la solución perturbada
ax.scatter(x_perturbado[0], x_perturbado[1], x_perturbado[2], color='orange', s=100, label='Solución Perturbada')

# Etiquetas de los ejes
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')

# Título y leyenda
ax.set_title('Soluciones del Sistema de Ecuaciones (3D) con Planos')
ax.legend()

# Mostrar la gráfica
plt.show()
