print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
total_tip = int(input("What percentage tip would you like to give? "))
total_people = int(input("How many people to split the bill? "))

each_to_pay = (total_tip / 100 * total_bill + total_bill) / total_people
final_amount = round(each_to_pay, 2)
print(f"Each person owes: £{final_amount}")

