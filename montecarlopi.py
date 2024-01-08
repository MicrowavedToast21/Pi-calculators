import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_pi(num_samples):
    np.random.seed(42)
    x_values = [random.uniform(0, 1) for _ in range(num_samples)] #creates random values for x and y in the circles
    y_values = [random.uniform(0, 1) for _ in range(num_samples)]

    inside_circle_x = []
    inside_circle_y = []

    for x, y in zip(x_values, y_values):
        distance = (x - 0.5)**2 + (y - 0.5)**2  # Distance from the center (0.5, 0.5)

        if distance <= 0.25:  # If the distance is less than or equal to the radius squared, program appends them outside
            inside_circle_x.append(x)
            inside_circle_y.append(y)

    pi_estimate = (len(inside_circle_x) / num_samples) * 4 #calculates pi
    return pi_estimate, x_values, y_values, inside_circle_x, inside_circle_y

# Asks for Number of random samples
num_samples = int(input("Enter a number of random samples for the montecarlo pi simulation: "))

# Runs the Monte Carlo simulation
pi_estimate, x_values, y_values, inside_circle_x, inside_circle_y = monte_carlo_pi(num_samples)

# Plots results
plt.figure(figsize=(8, 8))

# Plot points outside of circle in gray
plt.scatter(x_values, y_values, color='gray', alpha=0.5, label='Outside Circle')

# Plot points inside the blue circle
plt.scatter(inside_circle_x, inside_circle_y, color='blue', label='Inside Circle')

circle = plt.Circle((0.5, 0.5), 0.5, color='black', fill=False)
plt.gca().add_patch(circle)

#Draws title, labels and axes
plt.title(f'Monte Carlo Simulation for the value of π: {pi_estimate:.5f} using {num_samples} random samples')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.axis('equal')  # Set equal scaling for X and Y axes
plt.show()
