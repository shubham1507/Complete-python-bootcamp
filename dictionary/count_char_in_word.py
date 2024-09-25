"""
Implement a function that takes a String as a parameter and returns a dictionary with characters as keys from the String and values are the occurrence of characters in the String. Basically we are counting the occurrence of characters in a given string and returning it as output in Dictionary.

Example

count_character("BABACDAS")
Output

{
 'B': 2, 
 'A': 3, 
 'C': 1, 
 'D': 1, 
 'S': 1
} 
"""
def count_character(word):
    output_dict = {}
    for character in word:
        if character not in output_dict:
            output_dict[character] = 1
        else:
            output_dict[character]=output_dict[character] + 1
    return output_dict

print(count_character("BABACDAS"))
