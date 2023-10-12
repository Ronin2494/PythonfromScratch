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


######## String formatting example ######### 

names = "Ganymede"
planets = "Mars"
gravitys = "1.43"

template = """Gravity Facts about {name}
----------------------------------------
Planet name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=names, planet = planets, gravity = gravitys))


######## list example using while ########

user_input = ''

input_list = []

while (user_input.lower()!= 'done'):
    if user_input:
        input_list.append(user_input)
    
    user_input = input('Enter the values and enter done when you are done adding values: ')

print((input_list))

##### Functions ######
####Variable arguments ####

def variable_length(*args):
    #print(args)
    print (args)

one = variable_length() ##variable is showcased to tell that it could be used somewhere else by simple using the variable that contains functions output.
variable_length("one", "two")
variable_length(None)

####Variable keyword arguments####

def variable_length(**kwargs):
    print(f"{len(kwargs)} people assigned for the task")

    for title, name in kwargs.items():
        print(f"{title} : {name}")

variable_length(Pilot = 'XYZ', copilot = 'abc', crew = 'randomcrew')