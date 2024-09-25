original_dict = {
  "names" : ["Elshad", "John", "Edy"],
  "numbers" : [1,2,3,4,5]
}

def deep_copy(p_dict):
  new_dict = {}
  for key,value in p_dict.items():
      new_value = value.copy()
      new_dict[key] = new_value
  return new_dict

coped_dict = deep_copy(original_dict)

print(original_dict)
coped_dict["names"].append("Jack")
coped_dict["numbers"].append(6)
print(coped_dict)
