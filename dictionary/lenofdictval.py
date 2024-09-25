"""
Length of Dictionary Values
Implement a function which takes a dictionary as a parameter and returns new dictionary.  In new dictionary the keys remain same but values will be another nested dictionary. Nested dictionary's keys will be values from original dictionary and values will be length of values from original dictionary. (I know it is confusing, see example below you will understand it :) )

Example

names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}
value_length(names_dict)
Output

{
    1: {'Elshad': 6}, 
    2: {'Renad': 5}, 
    3: {'Johanna': 7}, 
    4: {'Appmillers': 10}
}
"""

names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}

def value_length(p_dict):
    output_dict = {}
    for key, value in p_dict.items():
        output_dict[key] = {}
        output_dict[key][value] = len(value)
    return output_dict



print(value_length(names_dict))
