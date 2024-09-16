# Program to take the average any number of numbers

# Input numbers from the user separated by spaces
numbers = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of floats
numbers_list = [float(num) for num in numbers.split()]

# Average all the numbers
average = sum(numbers_list)/len(numbers_list)

# Print the result
print(f"The sum of the numbers is {average}")