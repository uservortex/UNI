import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Crear una nueva figura
fig, ax = plt.subplots()

# Dibujar la cara (un óvalo)
face = patches.Ellipse((0.5, 0.5), 0.4, 0.6, edgecolor='black', facecolor='orange')
ax.add_patch(face)

# Dibujar los ojos
left_eye = patches.Ellipse((0.4, 0.6), 0.07, 0.1, edgecolor='black', facecolor='white')
right_eye = patches.Ellipse((0.6, 0.6), 0.07, 0.1, edgecolor='black', facecolor='white')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Dibujar las pupilas
left_pupil = patches.Ellipse((0.4, 0.6), 0.03, 0.05, edgecolor='black', facecolor='black')
right_pupil = patches.Ellipse((0.6, 0.6), 0.03, 0.05, edgecolor='black', facecolor='black')
ax.add_patch(left_pupil)
ax.add_patch(right_pupil)

# Dibujar la boca
mouth = patches.Arc((0.5, 0.4), 0.2, 0.1, angle=0, theta1=0, theta2=180, edgecolor='black', facecolor='red')
ax.add_patch(mouth)

# Dibujar el pelo (simplificado)
hair = patches.Ellipse((0.5, 0.8), 0.5, 0.15, angle=-20, edgecolor='black', facecolor='yellow')
ax.add_patch(hair)

# Configurar los límites del gráfico y mostrar
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.axis('off')
plt.show()
