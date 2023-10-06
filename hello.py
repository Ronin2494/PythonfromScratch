from datetime import date

print("Hello")

date1 = date.today()
print("Today's date is: " + str(date1)) 

parsecs = 11
light_years = parsecs * 3.26

print("{} parsecs has {} light_years ".format(parsecs,light_years)) #one way of string formating

print("\nWith Another way: \n")
print(f'{parsecs} parsecs has {light_years} light_years ') #another way of string formatting

parsecs1 = input("Enter the number: ")
parsecs_conv = int(parsecs1)

light_years1 = parsecs_conv * 3.26

print(str(parsecs1) + " parsecs is " + str(light_years1) + " light years") #third way of string formatting