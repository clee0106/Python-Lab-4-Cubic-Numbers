
"""
Program Name: Lab 4 - Plotting Cubic Numbers
Author: Colin Lee
Purpose: Generate and plot the first 5 and first 5000 cubic numbers using matplotlib.
Starter Code: Based on Chapter 15 of Python Crash Course, 3rd Edition by Eric Matthes.
Date: November 22, 2026
"""


import matplotlib.pyplot as plt

# Create the first 5 cubic numbers.
input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Create the graph.
fig, ax = plt.subplots()
ax.plot(input_values, cubes, linewidth=3)

# Add a title and axis labels.
ax.set_title("First 5 Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Save the graph as an image.
plt.savefig("cubes_5.png", bbox_inches="tight")


# Generate the first 5000 cubic numbers.
input_values = list(range(1, 5001))
cubes = [value**3 for value in input_values]

# Create the second graph.
fig, ax = plt.subplots()
ax.plot(input_values, cubes, linewidth=3)

# Add a title and axis labels.
ax.set_title("First 5000 Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Save the second graph as an image.
plt.savefig("cubes_5000.png", bbox_inches="tight")

