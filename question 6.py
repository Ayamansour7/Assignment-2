#Question 6
# This function simulates a hopping game using a list of jumps.
def list_jumps(jumps):
    index = 0   # Variable to store the current index
    visited = set()   # Set to store visited indices
    # Continue the game until the index is out-of-bounds or a cycle is detected
    while index >= 0 and index < len(jumps):
        if index in visited:   # If the current index has been visited before
            return "cycle"   # Return "cycle"
        visited.add(index)   # Add the current index to the visited set
        index += jumps[index]   # Move to the next index based on the jump value
    return "out-of-bounds"   # Return "out-of-bounds" if the index is out-of-bounds
  
# Example jumps
jumps = [2, -1, 3, 0, 5]
print(list_jumps(jumps))  # Output: out-of-bounds

jumps = [2, -1, 3, -1, 5]
print(list_jumps(jumps))  # Output: out-of-bounds

jumps = [2, -1, 2, 1, -2]
print(list_jumps(jumps))  # Output: cycle