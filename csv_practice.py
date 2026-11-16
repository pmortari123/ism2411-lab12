# Reflection answers go here (we'll fill these in at the end)

import csv
from datetime import datetime

# Exercise 1: sales.csv is in data/sales.csv

# Exercise 2: Read and print raw rows
print("=== Exercise 2 ===")
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 3: Skip the header
print("\n=== Exercise 3 ===")
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4: Compute totals
print("\n=== Exercise 4 ===")
total_revenue = 0
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5: Filter and write
print("\n=== Exercise 5 ===")
original_count = 0
written_count = 0
with open("data/sales.csv", "r") as infile, open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)  # skip header
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count += 1
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        if total > 100:
            writer.writerow([row[0], f"{price:.2f}", quantity, f"{total:.2f}"])
            written_count += 1
print(f"Wrote {written_count} of {original_count} rows to data/cleaned.csv")

# Exercise 6: csv.DictReader
# csv.reader gives each row as a list, so you use positions like row[1]. It's fine for small files you know well.
# csv.DictReader uses column names like row["price"], which is easier to read and won't break if the columns move.
print("\n=== Exercise 6 ===")
dict_total = 0
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")
print("Matches Exercise 4:", round(dict_total, 2) == round(total_revenue, 2))

# Exercise 7: Sales summary by product
print("\n=== Exercise 7 ===")
summary = {}
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + revenue
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8: Append mode log
print("\n=== Exercise 8 ===")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as log:
    log.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")
print("Logged this run to data/run_log.txt")