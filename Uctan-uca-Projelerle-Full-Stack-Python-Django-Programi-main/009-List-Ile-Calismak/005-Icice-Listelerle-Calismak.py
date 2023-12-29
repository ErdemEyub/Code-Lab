# Liste icine list Eklemek

users = []

user_1 = ["Ayse", 1234]
user_2 = ["Ahmet", 5678]

users.append(user_1)
users.append(user_2)

print(users)

products = [
    ["Laptop", "mouse", "keyboard"],
    ["Monitor", "printer"],
    "headphone",
]

# list icindeki list'e Erismek

print(products)
# print(products[0])
# print(products[0][1])
print(products[2][0])

print(users[1])

# list icindeki list'i Silmek

first_user = users.pop(0)

print("first_user:", first_user)
print("users:", users)


print("products:", type(products))
print("products 0. oge:", type(products[0]))
print("products 2. oge:", type(products[2]))


