# set nedir?
# list set'e nasil Donusturulur
# set list'e nasil donusturulur
# set'e yeni veri nasil eklenilir
# set'ten pop ile veri nasil cikarilir
# set icinden discard ile veri nasil cikarilir
# iki set arasindaki fark nedir
# iki set'in kesisimi (intersection)
# iki set'in birlesimi (union)

list_info = [1, 2, 3, 4, 5, 1, 2, 3, 7, 8, 9]

new_info = list()

for item in list_info:
    if item not in new_info:
        new_info.append(item)
        
print(new_info)

unique_list = list(set(new_info))

print(set(new_info))

users = {"Duygu", "Derya", "Ahmet", "Derin", "Hasan", "Derya", "Duygu"}
users_v2 = {"Python", "Django", "Hasan", "Derya"}

print(users)

users.add("Deneme")
 

print(users.pop())
print(users)

users.discard("Deneme")
print(users)

print("-" * 30)

print("difference: ")
print(users)
print(
    users.difference(users_v2)
)

print("intersection: ")
print(
    users.intersection(users_v2)
)

print("union: ")
print(
    users.union(users_v2)
)


