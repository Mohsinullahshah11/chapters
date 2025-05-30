# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")



# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

people = int(input("How many people are in your dinner group? "))

if people > 8:
    print("You’ll have to wait for a table.")
else:
    print("Your table is ready.")


# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")



# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.


while True:
    age = int(input("Enter your age (or type 0 to exit): "))
    if age == 0:
        break

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")



# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

# age_input = input("Enter your age (or type 0 to exit): ")

while True:
    age = int(input("Enter your age (or type 0 to exit): "))
    if age == 0:
        break

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")




# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# ctrl-C or close the window displaying the output.)

# while True:
#     print("This loop will run forever. Press Ctrl+C to stop.")



# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwich_orders = ['tuna', 'chicken', 'veggie', 'turkey']
finished_sandwiches = []
length  = len(sandwich_orders)

for i in range(length-1,-1,-1):
    print(f"I made your {sandwich_orders[i]} sandwich.")
    finished_sandwiches.append(sandwich_orders[i])
    sandwich_orders.pop(i)


print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")




# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.


sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

# Remove all 'pastrami' from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

length = len(sandwich_orders)


for i in range(length-1,-1,-1):
    print(f"I made your {sandwich_orders[i]} sandwich.")
    finished_sandwiches.append(sandwich_orders[i])
    sandwich_orders.pop(i)


print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")



# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.



responses = {}

polling_active = True


for i in range(10):
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let someone else respond? (yes/no): ")
    

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
