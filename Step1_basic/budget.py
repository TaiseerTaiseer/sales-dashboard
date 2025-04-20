# Step 1: Get user input
total = float(input("How much money do you have for today? "))
food = float(input("How much will you spend on food? "))
transport = float(input("How much will you spend on transport? "))
other = float(input("How much will you spend on other things? "))

# Step 2: Calculate remaining
remaining = total - (food + transport + other)

# Step 3: Print summary
print("You started with", total, "EUR.")
print("You spent", food, "on food,", transport, "on transport,", other, "on other.")
print("You have", remaining, "EUR left for today.")

# Step 4 (Bonus): Check budget
if remaining < 0:
    print("⚠️ Warning: You're over budget!")