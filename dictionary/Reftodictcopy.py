person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

new_person = person
new_person["city"] = "Nanded"
"""
print(person["city"])
print(new_person["city"])
"""


new_person1 = person.copy()
new_person1["city"] = "Osmanabad"

print(person["city"])
print(new_person1["city"])
