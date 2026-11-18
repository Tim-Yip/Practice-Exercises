employees = ['John', 'Sarah', 'Michael', 'Jennifer', 'David']
sales = [5200, 6800, 4500, 7200, 5800]

def calculate_total(sales):
    total = 0

    for amount in sales:
        total += amount

    return total

total = calculate_total(sales)

print(f"Total Monthly Sales: ${total:,.2f}")

def calculate_average(total, number_of_employees):
    return total / number_of_employees

total = sum(sales)
average = calculate_average(total, len(employees))

print(f"Average Sales per Employee: ${average:,.2f}")

def evaluate_performance(amount):
    if amount >= 7000:
        return "Excellent"
    elif amount >= 6000:
        return "Good"
    elif amount >= 5000:
        return "Average"
    else:
        return "Needs Improvement"

print("\nEMPLOYEE SALES PERFORMANCE")
print("----------------------------------------------")

for i in range(len(employees)):
    performance = evaluate_performance(sales[i])
    print(f"{employees[i] + ':':<10} ${sales[i]:>8,.2f} - {performance}")

def find_highest_sales(sales):
    highest = sales[0]
    for amount in sales:
        if amount > highest:
            highest = amount
    return highest

highest = find_highest_sales(sales)
print(f"\nHighest Sales Amount: ${highest:,.2f}")

def calculate_commission(amount, rate):
    return amount * rate

commission = calculate_commission(5200, 0.05)
print(f"John's Commission: ${commission:,.2f}")

print("\nEMPLOYEE SALES SUMMARY")
print("-" * 54)
print(f"{'Employee':<12}{'Sales':<12}{'Performance':<20}{'Commission'}")
print("-" * 54)

for i in range(len(employees)):
    performance = evaluate_performance(sales[i])
    commission = calculate_commission(sales[i], 0.05)

    sales_amount = f"${sales[i]:,.2f}"
    commission_amount = f"${commission:,.2f}"

    print(f"{employees[i]:<12}{sales_amount:<12}{performance:<20}{commission_amount}")