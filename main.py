import numpy as np
import matplotlib.pyplot as plt

# Sample wind speed (in m/s) and direction (in degrees)
wind_speeds = np.array([5, 10, 15, 20, 25])
wind_directions = np.array([0, 45, 90, 135, 180])  # From North, Eastward

# Setup the plot for circles with central axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', 'box')

# Set limits for the plot
max_speed = wind_speeds.max()
ax.set_xlim(-max_speed, max_speed)
ax.set_ylim(-max_speed, max_speed)

# Label the ends of the axes with the specified wind directions
ax.text(0, max_speed * 1.1, '180°', horizontalalignment='center', verticalalignment='bottom')
ax.text(max_speed * 1.1, 0, '270°', horizontalalignment='left', verticalalignment='center')
ax.text(0, -max_speed * 1.1, '360°', horizontalalignment='center', verticalalignment='top')
ax.text(-max_speed * 1.1, 0, '90°', horizontalalignment='right', verticalalignment='center')

# Draw circles for different speeds at the origin to indicate wind speed and label them
for speed in wind_speeds:
    circle = plt.Circle((0, 0), speed, color='blue', fill=False, linestyle='--', linewidth=1)
    ax.add_artist(circle)
    # Place labels below the circle by using negative speed for the y-coordinate
    ax.text(-3, -speed, f'{speed} m/s', horizontalalignment='center', verticalalignment='top')

# Add a horizontal and vertical line through the origin to represent the axes
ax.axhline(y=0, color='black', linewidth=1.5)
ax.axvline(x=0, color='black', linewidth=1.5)

# Set limits for the plot
ax.set_xlim(-max_speed, max_speed)
ax.set_ylim(-max_speed, max_speed)

# Remove x and y ticks as they're not necessary for this visualization
ax.set_xticks([])
ax.set_yticks([])

# Add grid, labels, and title
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
ax.set_title('Hodograph\n\n\n')

plt.show()
