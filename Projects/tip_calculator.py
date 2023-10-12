print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?"))
tip = int(input("How much % tip would you like to give i.e. 10, 12 or 15?"))/100
no_of_people = int(input("How many people would you like to split the bill with?"))

total_bill = (bill * tip) + bill
payment = total_bill/no_of_people

print(f"Each has to pay: {round(payment,2)}")