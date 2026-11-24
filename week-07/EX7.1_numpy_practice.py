import numpy as np

sales = np.array([
    [[1200, 1500, 1800],
     [2000, 2200, 2500]],
     
    [[1400, 1600, 1900],
     [2100, 2300, 2600]]
])

print(sales)

for x in np.nditer(sales):
    print(x)

print()

for store in sales:
    for month in store:
        for amount in month:
            print(amount)

print()

total = 0

for amount in np.nditer(sales):
    total += amount

print(f"Total sales: {total}")

print()

num_sales = 0

for num in np.nditer(sales):
    num_sales += 1

average = total / num_sales

print(f"Average sales: {average:.2f}")

highest = 0

for amount in np.nditer(sales):
    if amount > highest:
        highest = amount

print(f"Highest sales: {highest}")