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


########Calculate amount of water left for the astronauts to drink using file handling ##########
#### An astronaut drinks 11 litres of water per day########

def water_left(astronauts, water_left, days_left):
    #####if we pass none as days left, or a non-integer value, how to catch such errors#######
    for argument in [astronauts, water_left, days_left]:
        try:
            argument/10
        except TypeError:
            raise TypeError(f"All arguments must be of type int but riased, '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage

    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water left for {astronauts} astronauts after {days_left} days.")
    return f"Total water left after {days_left} days is: {total_water_left} litres"

water_left(5,100, 2)
