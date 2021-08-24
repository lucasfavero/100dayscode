print("Welcome to the tip calculator.\n")
total_bill = int(input("What was the total bill? "))
percentage_tip = float(input("What percentage tip would you like to give? "))
split_bill = int(input("How many people to split the bill? "))
payment = (total_bill + (total_bill * (percentage_tip / 100))) / split_bill
print(f"Each person should pay: ${payment}")
