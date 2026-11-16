# Reflection answers go here (we'll fill these in at the end)

import csv

# Exercise 1: sales.csv is in data/sales.csv

# Exercise 2: Read and print raw rows
print("=== Exercise 2 ===")
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)