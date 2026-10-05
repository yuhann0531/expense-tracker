# Installation 2
print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tTrack your expenses easily")
print("=" * 40)

name = input("Enter your name: ")

print(f"\nWelcome, {name}! Let's log two expenses.\n")

item1 = input("Enter first expense item: ")
amount1 = float(input("Enter first expense amount: "))

item2 = input("Enter second expense item: ")
amount2 = float(input("Enter second expense amount: "))

total = amount1 + amount2
average = total / 2

print("\nSUMMARY")
print("-" * 40)
print(f"Item 1: {item1}")
print(f"Amount: {amount1}")
print(f"Item 2: {item2}")
print(f"Amount: {amount2}")
print(f"Total spent: {total}")
print(f"Average: {average}")
print("-" * 40)

print(f"Made by: \"Janrie Euhann Oasan\" | Installment 2")
print("=" * 40)