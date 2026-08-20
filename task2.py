
"""Task 1

Create variables for name, age, marks, and student status and print all four values in 
one print() statement."""

# Getting student details
name = input("Enter your name:")
age = int(input("Enter your age:"))
marks = float(input("Enter your marks:"))
status = input("Enter your status:")
# print function
print(f"Your Name is {name}, you are {age} years old, your secured {marks} marks in the exam and you {status} student in the class")

"""Task 2

Create variables with int, float, str, and bool values. Use type() to display
the data type of each variable."""

# Getting user inputs;
Name_of_the_car = input("Enter the name of the car:")
Price_of_the_car = float(input("Enter the price of the car:"))
How_many_do_you_have = int(input("Enter the quantities you have:"))
Is_performance_car = True

# Finding the data types of each variable;
print(type(Name_of_the_car))
print(type(Price_of_the_car))
print(type(How_many_do_you_have))
print(type(Is_performance_car))

"""Task 3

Convert the string "50" into an int and a float. Print the converted values and their data types."""

values = input("Enter the values:")
conv_values_int  = int(values)
conv_values_float = float(values)

# Printing converted values and it's data types;
print(type(values),values)
print(type(conv_values_int),conv_values_int)
print(type(conv_values_float),conv_values_float)

"""Task 4

Get the user’s name, age, and height using input(). Convert age to int and height
to float, then display them using an f-string."""

Name = input("Enter your name:")
Age = input("Enter your age:")
Height = input("Enter your height:")

#converting and displaying them using f"string";
print(f"your name is {Name}, your age is {int(Age)} and your height is {float(Height)} cm.")

"""Task 5

Write a program to calculate the area of a circle by taking the radius from the user."""

# Importing math library;
import math
radius = float(input("Enter the radius of the circle:"))
area_of_circle = math.pi * radius**2

# Printing the area of the circle;
print(f"The entered Radius is :{radius}. Area of the circle is :{area_of_circle}")

"""Task 6

Create a Student Report program that accepts the student’s name, age, Python marks, and SQL marks,
calculates the total marks, and displays the result in a formatted output."""

# Getting student details;
std_name = input("Enter the student's name:")
std_age = int(input("Enter the student's age:"))
python_marks = float(input("Enter the python marks:"))
sql_marks = float(input("Enter the sql marks:"))

# Calculating total marks and displaying the results;
total_marks = python_marks + sql_marks
print(f"The student name is {std_name}, \n Student's age :{std_age}, \n Marks Obtained :{total_marks} marks.")

