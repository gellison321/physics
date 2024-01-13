import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(6, 6))

# Unit Circle setup
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Unit Circle with Triangle")

# Drawing the unit circle
circle = plt.Circle((0, 0), 1, fill=False, color='black', linestyle='--')
ax.add_artist(circle)

# Radius line and point on the circle
radius_line, = ax.plot([], [], 'b-', lw=2)
cos_point, = ax.plot([], [], 'bo')
sine_line, = ax.plot([], [], 'g--', lw=1)  # Line for sine
cosine_line, = ax.plot([], [], 'r--', lw=1)  # Line for cosine

# Triangle patch for geometric representation
triangle = Polygon([[0, 0], [1, 0], [1, 0]], closed=True, fill=None, edgecolor='orange')
ax.add_patch(triangle)

# Labels and text for unit circle
ax.set_xlabel(r"$\hat{x}$", fontsize=14)
ax.set_ylabel(r"$\hat{y}$", fontsize=14, rotation=0)
ax.yaxis.set_label_coords(-0.05,0.5)

# Initialize the lines and point
def init():
    radius_line.set_data([], [])
    cos_point.set_data([], [])
    sine_line.set_data([], [])
    cosine_line.set_data([], [])
    triangle.set_xy([[0, 0], [0, 0], [1, 0]])
    return radius_line, cos_point, sine_line, cosine_line, triangle

# Update function for the animation
def update(frame):
    # Compute cosine and sine
    x = np.cos(frame)
    y = np.sin(frame)

    # Update the radius line in the unit circle plot
    radius_line.set_data([0, x], [0, y])
    cos_point.set_data(x, y)
    sine_line.set_data([x, x], [0, y])  # Vertical line for sine value
    cosine_line.set_data([0, x], [y, y])  # Horizontal line for cosine value

    # Update the triangle's coordinates
    triangle.set_xy([[0, 0], [x, 0], [x, y]])

    # Adding labels for the triangle sides
    ax.text(x/2 - 0.1, y/2 + 0.1, r'$1$', ha='center', fontsize=12)  # Hypotenuse
    ax.text(x/2, -0.1, r'$\cos(\theta)$', ha='center', fontsize=12, color='red')  # Adjacent
    ax.text(x + 0.1, y/2, r'$\sin(\theta)$', va='center', fontsize=12, color='green')  # Opposite

    # Draw and label the angle theta
    arc_radius = 0.2
    arc = np.linspace(0, frame, 50)
    ax.plot(arc_radius*np.cos(arc), arc_radius*np.sin(arc), 'k-')  # Arc for theta
    ax.text(arc_radius/2, 0.1, r'$\theta$', fontsize=14)  # Label for theta

    return radius_line, cos_point, sine_line, cosine_line, triangle

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), init_func=init, blit=True, interval=50)

# Show the plot
plt.show()
