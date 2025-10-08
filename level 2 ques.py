import random

# Generate random salaries
salaries = [random.randint(5000, 99000) for _ in range(10)]

print("Original Salaries:", salaries)

# Filter salaries greater than 50,000
high_salary = [s for s in salaries if s > 50000]

print("Salaries > 50,000:", high_salary)
