# Write a program to print the sum of all the elements
# of an array of size N where N can be any integer between 1 and 100. 1≤N≤100
N = input()

# Get the input
numArray = map(int, input().split())

sum_integer = 0
# Write the logic to add these numbers here
for number in numArray:
    sum_integer += number

# Print the sum
print(sum_integer)