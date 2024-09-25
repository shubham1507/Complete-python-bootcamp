"""
Implement a function which takes a List a parameter and groups them according to their data types (integer or string) and return dictionary.

Hint :

Use isinstance() function to check data type.

Use fromkeys() method to solve this challenge

Example

custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
group_types(custom_list)


Output

{
 10: 'Integer', 
 'one' : 'String', 
 'two' : 'String', 
 'ten' : 'String', 
 20 : 'Integer', 
 30 : 'Integer', 
 'five' : 'String', 
 40 : 'Integer', 
 'nine' : 'String', 
 50 : 'Integer'
}
"""
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]

def group_types(p_list):
    out_di = dict.fromkeys(p_list)
    for key in out_di:
        if isinstance(key,int):
            out_di[key] = "Integer"
        else:
            out_di[key] = "String"

    return out_di

print(group_types(custom_list))
