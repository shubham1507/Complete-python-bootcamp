"""
Remove Empty Items
Implement a function which takes as a parameter dictionary and removes empty items from it and return new dictionary. If there is not any empty item in the dictionary it will return itself.

Example

custom_dict = {
    "name" : "Elshad",
    "age" : 28,
    "city" : None
}
remove_empty_items(custom_dict)
Output

{'name': 'Elshad', 'age': 28}
"""

def remove_empty_items(p_dict):
  for key, value in list(p_dict.items()):
      if value is None:
          p_dict.pop(key, value)
  return p_dict

custom_dict = {
  "name" : "Elshad",
  "age" : 28,
  "city" : None
}

print(remove_empty_items(custom_dict))


"""
if we use "for key, value in p_dict.items():"
we will get error because we are changing the dictionary while iterating over it.



"""
