"""
Delete Restricted Items
Set of items and set of restricted items are given, based on the beach type (family or normal) the list of items should be printed to the console. Restricted items are not allowed to family beach and everything else can be taken to normal beach except drugs.

general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}
 
restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
    }


Example Input

Select Beach Type (1 - Family beach, 2 - Normal Beach): 1

Example Output

See below the list of items that you can take.
    Alcholic Drinks
    Sand toys
    Snacks
    Sunglasses
    Hats
    Beach umbrella
    Beach towels
    Camp chair
    Camera
"""


# Define the sets of items
general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}

restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
}

# Prompt the user for input and handle EOFError
try:
    user_input = input("Select Beach Type (1 - Family beach, 2 - Normal Beach): ")
except EOFError:
    print("No input received. Defaulting to Family beach.")
    user_input = "1"

# Validate user input and modify the general_items set accordingly
if user_input == "1":
    # Remove all restricted items from general_items if it's a family beach
    for item in restricted_items:
        general_items.discard(item)
elif user_input == "2":
    # Remove only "Drugs" if it's a normal beach
    general_items.discard("Drugs")
else:
    print("Invalid selection. Please choose 1 or 2.")

# Print the list of items that can be taken
print("See below the list of items that you can take:")
for item in general_items:
    print(f"\t{item}")
