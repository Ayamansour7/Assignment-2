#Question 3
# This function compares two strings by checking if they contain the same characters, regardless of their order.
def reordering(s1, s2):
    return sorted(s1) == sorted(s2)
# Prompt the user to enter the first parameter
s1 = str(input("Enter your first parameter: "))
# Prompt the user to enter the second parameter
s2 = str(input("Enter your second parameter: "))
# Call the reordering function with the input parameters
result = reordering(s1, s2)
# Print the result of the comparison
print(result)