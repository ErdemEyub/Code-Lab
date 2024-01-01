# Aralik dongusunu Belirterek for dongusunu calistirmak --> range(aralık demek)

# for item in range(10): # 0 dan baslar 10 a kadar
for item in range(1, 101): # 1 den baslar 10 a kadar
    if item % 5 == 0:
        print(item)


# liste icindeki verileri tek tek islemek
users = ["Aysen", "Fatma", "Cigdem", "Hasan", "Ahmet", "Mehmet"]

print("*" * 30)

for user in users:
    print(user)

print("*" * 30)

# item ve index bilgisi ile listleri dongude kullanmak --> enumerate
for obj in enumerate(users):
    print(obj[0], obj[1])
    print(users[obj[0]])





