#!/usr/bin/python3
def remove_char_at(str, n):
    # If n is negative or greater than or equal to the length of the string, return the original string
    if n < 0 or n >= len(str):
        return str
    
    # Create a new string with the characters up to the position n
    new_str = str[:n]
    
    # Add the characters after the position n to the new string
    if n < len(str) - 1:
        new_str += str[n+1:]
    
    return new_str
