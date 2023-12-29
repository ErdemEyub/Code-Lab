# list icindeki ogelere erişmek
first_item, second_item, third_item = "first", "second", "third"

items = [
    first_item,
    second_item,
    third_item,
]

print(items)
print(items[0])
print(items[1])
print(items[2])

# List icerisine yeni oge eklemek
fourth_item = 'fourth'
items.append(fourth_item)
items.append('fifth')
items.append(1)
print(items)

# List icindeki ogenin icindeki bilgiyi degistirmek
# items[0] = 'birinci Oge'
# len(items) # icinde kac oge oldugunu biliyoruz 
print(len(items))
items[len(items) -1] = 'birinci oge'
items[-1] = 'gercekten sonuncu oge..'
print(items)

# list icinde belli bir yere oge eklemek
items.insert(3, "yeni oge")
items.insert(0, "en basa eklenen oge")
items.insert(len(items), "en sonnnn")
print(items)

# list icindeki belli bir bolumu listelemek
print(items[2:5])
print(items[2:])

#  list'in ilk 3 ogesi
print(items[:3])

#  list'in son 3 ogesi
print(items[len(items) -3 :])

#  list'i Terse Cevir
print(items[::-1])
print(items) # degismemis
# items = items[::-1] # esitlemis olduk

# son ogeye ulas
print(items[-1])

# STEP belirleyerek Bilgileri al.. 1. 3. 5.
step_items = items[::2]
print(step_items)

