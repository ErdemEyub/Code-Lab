items = [
    "html",
    "django",
    "python",
    "bootstrap",
    "flask",
    "css",
    "javascript",
    "react",
    "vue",
    "angular",
    "node",
    "python",
]

# liste icinde kac oge var -> len
print(len(items))

# liste icinde bir oge var mı ->
print("html" in items)
print("react" in items)
item = input("Bu Egitimde Hangi Yazilim Dili Var mi Diye Sor:")
if item in items:
    print(f"{item} Egitimde Var")
else:
    print("Yok")

# liste icinde bir oge kac kez var -> count
print("kac adet python var", items.count("python"))

# liste icindeki ogenin yeri(index) nedir -> index
print("python index:", items.index("python"))

# liste icindeki oge adlarini sil -> remove
items.remove("python")
print(items)

# liste icindeki son ogeyi cikar -> pop
last_item = items.pop()
print(items)
print(last_item)

# liste icindeki x indexli ogeyi cikar -> pop
first_item = items.pop(0)
print(items)
print(first_item)

# listeyi boşalt -> clear
items.clear()
print(items)

# liste icindeki ogeleri topla -> sum
numbers = [
    1, 2, 3, 4, 5, 6
]
print(sum(numbers))

# liste icindeki en kucuk fiyat -> min
print(min(numbers))

# liste icindeki en buyuk fiyat -> max
print(max(numbers))



