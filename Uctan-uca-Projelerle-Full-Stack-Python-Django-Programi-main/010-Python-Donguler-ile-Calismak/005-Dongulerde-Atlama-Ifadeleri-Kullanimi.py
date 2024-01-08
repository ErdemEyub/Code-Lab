users = [
    "user1",
    "user2",
    "Cigdem",
    "Aytug",
    "Mehmet",
    "Ahmet",
    "Ali",
]

# continue
for item in range(10):
    if item == 5:
        continue
    print(item)

print("-" * 30)

# break
for item in range(10):
    if item == 5:
        break
    print(item)

print("-" * 30)

for user in users:
    if user == "Cigdem":
        continue
    print(user)

print("-" * 30)

for user in users:
    if user == "Cigdem":
        break
    print(user)
