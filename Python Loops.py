# Program to print even numbers between 1 and 100

for number in range(1, 101):  # Loop from 1 to 100
    if number % 2 == 0:       # Check if the number is even
        print(number)
        # Print even numbers between 1 and 100 (2 to 98)
for number in range(2, 100, 2):  # start=2, stop=100 (exclusive), step=2
    print(number)
    # Create a list called numbers with values from 1 to 10
numbers = list(range(1, 11))

# Use a loop to display the contents of the list
for num in numbers:
    print(num)
    # Initialize the counter
number = 1

# Loop until number is greater than 10
while number <= 10:
    square = number ** 2        # Calculate square
    print(square)
    number += 1                 # Increment counter
    # Initialize the counter
number = 1

# Loop until number is greater than 10
while number <= 10:
    if number == 5:
        number += 1   # Increment before skipping
        continue      # Skip number 5
    print(number)
    number += 1
   # Given list
numbers = [99, 55, 67, 10, 89, 78, 56, 57, 87]

# Loop through the list with index
for i in range(len(numbers)):
    if numbers[i] == 10:
        print(i)
        break  # Stop loop after finding the number