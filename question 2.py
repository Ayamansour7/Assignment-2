#Question 2
# This function rearranges the characters in a string by placing uppercase characters before lowercase characters.
def rearrange_string(s):
    lowercase = ''   # Variable to store lowercase characters
    uppercase = ''   # Variable to store uppercase characters

    # Iterate over each character in the input string
    for c in s:
        if c.islower():   # If the character is lowercase
            lowercase += c   # Add it to the lowercase string
        else:
            uppercase += c   # Otherwise, add it to the uppercase string
    return uppercase + lowercase   # Concatenate the uppercase and lowercase strings and return the result
# Prompt the user to enter a word
s = str(input("Enter your word here: "))
# Call the rearrange_string function with the input word
result = rearrange_string(s)
# Print the rearranged string
print(result)