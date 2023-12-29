items = [
    "cable",
    "keyboard",
    "pc",
]

digital_products = ["laptop", "monitor", "mouse"]
other_profucts = ["lorem", "ipsum", "dolor"]

# new_items = [*items] # cok okunaklı olmuyor
new_items = items.copy() # 1. yontem
new_items[0] = "mic"

print("items", items)
print("new_items", new_items)

# items.append(digital_products) # listeyi oldugu gibi icine atiyor
# items.extend(digital_products) # 2. yontem
# items += digital_products # 3. yontem
items += digital_products + other_profucts # 4. yontem

# items = items + digital_products + other_profucts 
# items = [items, digital_products, other_profucts]
items = [*items, 
         *digital_products, 
         *other_profucts,
         1,
         2,
         3,
         4,
]
print("items", items) # Daha islevsel
# print(items[5])

print("id of items", id(items))
print("id of new_items", id(new_items))
print("items[0]", items[0])
print("new_items[0]", new_items[0])
print("id of items[0]", id(items[0]))
print("id of new_items[0]", id(new_items[0]))
print("items[1]", items[1])
print("new_items[1]", new_items[1])
print("id of items[1]", id(items[1]))
print("id of new_items[1]", id(new_items[1]))
print("items[2]", items[2])
print("new_items[2]", new_items[2])
print("id of items[2]", id(items[2]))
print("id of new_items[2]", id(new_items[2]))


