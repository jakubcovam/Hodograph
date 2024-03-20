import numpy as np
import matplotlib.pyplot as plt
import math

# Points defined by their velocity (m/s) and direction (degrees)
points = {
    "P1": {"velocity": 4, "direction": (110+180)},
    "P2": {"velocity": 8, "direction": (178+180)},
    "P3": {"velocity": 13, "direction": (200+180)},
    "P4": {"velocity": 18, "direction": (220+180)},
    "P5": {"velocity": 23, "direction": (250+180)},
}

# Wind speed for the plot (m/s)
velocity_max = max(point['velocity'] for point in points.values())
number_of_points = len(points)
wind_speeds_step = math.ceil(velocity_max / number_of_points)
wind_speeds = np.arange(1, number_of_points+1) * wind_speeds_step

# Set wind directions for the plot (degrees)
wind_directions = np.array([0, 45, 90, 135, 180])  # From North, Eastward

# Set up the plot for circles with central axes
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
    ax.text(-3, -speed, f'{speed} m/s', horizontalalignment='center', verticalalignment='top')

# Add a horizontal and vertical line through the origin to represent the axes
ax.axhline(y=0, color='black', linewidth=1.5)
ax.axvline(x=0, color='black', linewidth=1.5)

# Extract (u, v) coordinates for each point and plot them
u_values = []
v_values = []
for point, attributes in points.items():
    u = attributes["velocity"] * np.sin(np.radians(attributes["direction"]))
    v = attributes["velocity"] * np.cos(np.radians(attributes["direction"]))
    u_values.append(u)
    v_values.append(v)
    ax.plot(u, v, marker='o', markersize=10, color='red', label=f'{point}: {attributes["velocity"]} m/s, {attributes["direction"]}°')

# Connect points with a solid line
ax.plot(u_values, v_values, marker='', linestyle='-', color='red')

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
