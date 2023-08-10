#Question 3
# This function finds the maximum value in a list and returns the maximum value along with its index.
def max_num(l):
    index = 0   # Variable to store the index of the maximum value
    # Iterate through the list starting from the second element
    for i in range(1, len(l)):
        if l[i] > l[index]:   # If the current element is greater than the maximum value
            index = i   # Update the index to the current element's index
    max_value = l[index]   # Get the maximum value using the index
    return "The highest value in the list is {} at index {}".format(max_value, index)
# Define a list of numbers
l = [5, 6, 3, 9, 7, 166, 0, 1, 6]
# Call the max_num function with the list
result = max_num(l)
# Print the result
print(result)


#Bonus Question
# This function finds the minimum value in a list and returns the minimum value along with its index.
def min_num(l):
    index = 0   # Variable to store the index of the minimum value
    # Iterate through the list starting from the second element
    for i in range(1, len(l)):
        if l[i] < l[index]:   # If the current element is smaller than the minimum value
            index = i   # Update the index to the current element's index
    min_value = l[index]   # Get the minimum value using the index
    return "The lowest value in the list is {} at index {}".format(min_value, index)
# Define a list of numbers
l = [5, 6, 3, 9, 7, 166, 0, 1, 6]
# Call the min_num function with the list
result = min_num(l)
# Print the result
print(result)