products = [
    ["laptop", "mouse", "keyboard"],
    ["phone", "camera", "speaker"],
    ["tablet", "pen", "paper"],
    "Sony XYZ",
    "Apple Magic Keyboard",
    "Samsung Galaxy S10",
    "iPhone X",
    "Samsung Galaxy S20",
    "iPhone 12",
    12,
    23,
    34,
    True,
    False,
    (1, 2, 3,),
]

for item in products:
    if type(item) == list:
        for pr in item:
            print(pr)
    elif type(item) == str:
        print(item)



