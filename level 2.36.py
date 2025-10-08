import matplotlib.pyplot as plt

# Data
X = [1, 2, 3, 4, 5]
Y = [2, 4, 1, 3, 7]

# Create scatter plot
plt.scatter(X, Y, color='blue', marker='o')

# Add labels and title
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")

# Show plot
plt.show()
