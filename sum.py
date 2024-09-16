# Program to add any number of numbers

# Input numbers from the user separated by spaces
numbers = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of floats
numbers_list = [float(num) for num in numbers.split()]

# Add all the numbers
total_sum = sum(numbers_list)

# Print the result
print(f"The sum of the numbers is {total_sum}")