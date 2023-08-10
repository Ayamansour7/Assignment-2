#Question 5
# This function counts the number of digits in a number.
def counter(n):
    if n < 10:   # If the number is less than 10, it has only one digit
        return 1
    else:
        return 1 + counter(n // 10)   # Recursively divide the number by 10 and add 1 to the count
# Prompt the user to enter a number
n = int(input("Enter your number here: "))
# Call the counter function with the input number
digit_count = counter(n)
# Print the number of digits
print("Number of digits:", digit_count)