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

beach_selection = int(input("Select Beach Type (1 - Family beach, 2 - Normal Beach):\n"))

if beach_selection == "1":
    for item in restricted_items:
        general_items.discard(item)
else:
    general_items.discard("Drugs")
    
print("See below the list of items that you can take.")
for item in general_items:
    print(f"\t{item}")

