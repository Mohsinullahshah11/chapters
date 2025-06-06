# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")



# 4-2. Animals: Think of at least three different animals that have a common char-
# acteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!


animals = ["Dog", "Cat", "Rabbit"]

for animal in animals:
    print(f"A {animal.lower()} would make a great pet.")


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

for i in range(1,21):
    print(i)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

numbers = list(range(1,1000000))
for num in numbers:
    print(num)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

numbers = list(range(1, 1_000_001))

print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))

total_sum = sum(numbers)
print("Sum of numbers from 1 to 1,000,000:", total_sum)



# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_nums = list(range(1,20,2))
print(odd_nums)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

multiples3 = list(range(3,30,3))
for multiple in multiples3:
    print(multiple)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubes = list(i**3 for i in range(1,11))
for cube in cubes:
    print(cube)



# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.

numbers = [3, 5, 7, 9, 11, 13, 17, 19, 23, 29]
print("The numbers list is:", numbers)
print("\nThe first three items in the list are:", numbers[:3])
print("\nThree items from the middle of the list are:", numbers[3:6])
print("\nThe last three items in the list are:", numbers[-3:])


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the sec-
# ond list. Make sure each new pizza is stored in the appropriate list.

pizzas = ['pepperoni', 'margherita', 'bbq chicken']
friend_pizzas = pizzas[:]

pizzas.append('tandoori chicken')
friend_pizzas.append('veggie delight')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


