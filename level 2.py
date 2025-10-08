import matplotlib.pyplot as plt

# Product names and sales values
products = ['A', 'B', 'C', 'D']
sales = [40, 60, 80, 100]

# Create bar chart
plt.bar(products, sales)

# Add title and labels
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

# Show the chart
plt.show()
