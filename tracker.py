# ... Installment 3: ...
print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tTrack your expenses easily")
print("=" * 40)

name = input("Enter your name: ")
print(f"\nWelcome, {name}! Let's log two expenses.\n")
subtotal = 0

item1 = input("Enter first expense item: ")
amount1 = float(input("Enter first expense amount: "))
subtotal += amount1

item2 = input("Enter second expense item: ")
amount2 = float(input("Enter second expense amount: "))
subtotal += amount2

average = subtotal / 2

tax_percent = float(input("\nEnter tax rate (%): "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax

budget = float(input("Enter your budget: "))

over_budget = total > budget

left = budget - total

print("\nSUMMARY")
print("-" * 40)
print(f"Item 1:\t\t{item1}")
print(f"Amount:\t\t{amount1}")
print(f"Item 2:\t\t{item2}")
print(f"Amount:\t\t{amount2}")
print(f"Subtotal:\t{subtotal}")
print(f"Average:\t{average}")
print(f"Tax ({tax_percent}%):\t{tax}")
print(f"Grand total:\t{total}")
print(f"Over budget?:\t{over_budget}")
print(f"Left in budget:\t{left}")
print("-" * 40)

print(f"Made by: \"Janrie Euhann Oasan\"\t|\tInstallment 3")
print("=" * 40)