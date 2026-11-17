import statistics

days = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
]

sales = [1250, 1480, 1100, 1650, 1850,
         1420, 1700, 1300, 2100, 1950]

print("DAILY SALES REPORT")
print("-------------------")

for i in range(len(days)):
    print(f"{days[i] + ':':<12} ${sales[i]:.2f}")

mean = statistics.mean(sales)
median = statistics.median(sales)
mode = statistics.mode(sales)
stdev = statistics.stdev(sales)
sum = sum(sales)
min = min(sales)
max = max(sales)

print("\nSTATISTICS")
print("----------")
print(f"{'mean:':<20} ${mean:.2f}")
print(f"{'median:':<20} ${median:.2f}")
print(f"{'mode:':<20} ${mode:.2f}")
print(f"{'standard deviation:':<20} ${stdev:.2f}")
print(f"{'sum:':<20} ${sum:.2f}")
print(f"{'minimum:':<20} ${min:.2f}")
print(f"{'maximum:':<20} ${max:.2f}")

print("\nSALES PERFORMANCE")
print("-----------------")

for i in range(len(days)):
    if sales [i] >= 1800:
        print(f"{days[i] + ':':<12} ${sales[i]:.2f} - ", "Excellent sales performance!")
    elif sales[i] >= 1500 and sales [i] < 1800:
        print(f"{days[i] + ':':<12} ${sales[i]:.2f} - ", "Good.")
    elif sales[i] >= 1200 and sales [i] < 1500:
        print(f"{days[i] + ':':<12} ${sales[i]:.2f} - ", "Average.")
    else:
        print(f"{days[i] + ':':<12} ${sales[i]:.2f} - ", "Needs improvement.")

    excellent = 0
    good = 0
    average = 0
    needs_improvement = 0

    for i in range(len(days)):
        if sales[i] >= 1800:
            excellent += 1
        elif sales[i] >= 1500:
            good += 1
        elif sales[i] >= 1200:
            average += 1
        else:
            needs_improvement += 1

print("\nSALES PERFORMANCE SUMMARY")
print("-------------------------")
print(f"{'Excellent:':<20} {excellent}")
print(f"{'Good:':<20} {good}")
print(f"{'Average:':<20} {average}")
print(f"{'Needs Improvement:':<20} {needs_improvement}")

print("\nSALES TARGET")
print("------------")

target_met = 0

for i in range(len(days)):
    if sales[i] >= 1500:
        print(f"{days[i] + ':':<12} ${sales[i]:.2f}")
        target_met += 1

print(f"Total days that met the target: {target_met}")

print("\nFINAL ANALYSIS")
print("--------------")

if mean >= 1700:
    print("Sales performance is excellent.")
elif mean >= 1500:
    print("Sales performance is good.")
else:
    print("Sales performance needs improvement.")