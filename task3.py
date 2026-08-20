# Task 1

# Create two numbers and perform addition, subtraction, multiplication, 
# division, floor division, modulus, and power.

# Getting user inputs;
num_1 = int(input("Enter the first value: "))
num_2 = int(input("Enter the second value: "))

# Performing arithamatic operations;
print(f"ADDITION OF {num_1} & {num_2} IS:{num_1 + num_2}")
print(f"SUBTRACTION OF {num_1} & {num_2} IS:{num_1 - num_2}")
print(f"MULTIPLICATION OF {num_1} & {num_2} IS:{num_1 * num_2}")
print(f"DIVISION OF {num_1} & {num_2} IS:{num_1 / num_2}")
print(f"FLOOR DIVISION OF {num_1} & {num_2} IS:{num_1 // num_2}")
print(f"MODULUS OF {num_1} & {num_2} IS:{num_1 % num_2}")
print(f"POWER OF {num_1} & {num_2} IS:{num_1 ** num_2}")

# Task 2

# Take two numbers from the user and check whether the first number is greater than, less than, or 
# equal to the second number.

num_1 = int(input("Enter the num 1 value: "))
num_2 = int(input("Enter the num 2 value: "))

# Performing Relational operations;
if num_1 > num_2:
    print(f"The first value:  {num_1} is greater than second value:  {num_2}")
elif num_1 < num_2:
    print(f"The second value:  {num_2} is greater than first value:  {num_1}")
elif num_1 == num_2:
    print(f"The entered value 1 & value 2 are equal")

# Task 3

# Take a student’s marks and check whether the student has passed or failed 
# using a comparison operator.

mark_1 = int(input("Enter the mark-1: "))
mark_2 = int(input("Enter the mark-2: "))
mark_3 = int(input("Enter the mark-3: "))
mark_4 = int(input("Enter the mark-4: "))
mark_5 = int(input("Enter the mark-5: "))

total_marks = mark_1+mark_2+mark_3+mark_4+mark_5
avg_marks = round((int(total_marks)/5),2)

if mark_1 > 35:
    print("Pass")
else:
    print("Fail")
if mark_2 > 35:
    print("Pass")
else:
    print("Fail")
if mark_3 > 35:
    print("Pass")
else:
    print("Fail")
if mark_4 > 35:
    print("Pass")
else:
    print("Fail")
if mark_5 > 35:
    print("Pass")
else:
    print("Fail")

print(f"The total mark secured is: {total_marks} and the avg mark is: {avg_marks}")


# Task 4

# Take the user’s age and check whether they are eligible to vote.

age = input("What is your age? ")
if int(age) >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

# Task 5
# 
# Take the user’s age and marks and check whether:
# 
# * Age is 18 or above
# * Marks are 40 or above
# 
# Use the and operator.
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 18 and marks >= 40:
    print("True...!")
else:
    print("False...!")

# Task 6
#
# Create a variable balance = 1000 and use +=, -=, *=, and /= to modify the balance.
balance = 1000
balance +=500
print(balance)
balance -= 100
print(balance)
balance *= 10
print(balance)
balance /= 2
print(balance)


# Task 7
#
# Write a program to calculate how many complete groups can be formed from a given
# number of students using //, and how many students remain using %.

total_students = int(input("Enter the total number of students: "))
group_size = int(input("Enter the number of students per group: "))

complete_groups = total_students // group_size
remaining_students = total_students % group_size

print(f"\nTotal complete groups formed: {complete_groups}")
print(f"Students remaining without a group: {remaining_students}")

# Task 8 
#
# Create a multi-operation calculator that accepts two numbers and displays:
#
# * Addition
# * Subtraction
# * Multiplication
# * Division
# * Floor division
# * Remainder
# * Power

n1 = float(input("Enter a 1st number: "))
n2 = float(input("Enter a 2nd number: "))
print("-----------Mutli-operation calculator--------------")
print(f"Addition: {n1 + n2}")
print(f"Subtraction: {n1 - n2}")
print(f"Multiplication: {n1 * n2}")
print(f"Division: {n1 / n2}")
print(f"Floor division: {n1 // n2}")
print(f"Remainder: {n1 % n2}")
print(f"Power: {n1 ** n2}")

# Task 9 
#
# Create a program that accepts three numbers and calculates their average.
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

# Calculating the average of entered values;
avg_num = (num_1 + num_2 + num_3) / 3
print(f"The average is: {round(avg_num,3)}")

