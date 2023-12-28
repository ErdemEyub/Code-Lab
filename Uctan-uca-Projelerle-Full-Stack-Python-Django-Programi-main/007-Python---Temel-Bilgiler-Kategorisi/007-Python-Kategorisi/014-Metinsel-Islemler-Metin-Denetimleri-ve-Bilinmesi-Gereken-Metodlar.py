first_name = "erDem"
last_name = "dJaNGo"

# str'nin ilk karakteri [0]
print(first_name(0))
print(last_name(1)) 

# belli bir yerden baslayan bilgiyi goster [3:10]
print(first_name[2:4])
print(last_name[3:7])



# bastan 3 karakter [:3]
print(first_name[:3])


# sondan 3 karakter [-3:]
print(first_name[-3:])


# son 3 karakteri gösterme [:-3]
print(first_name[:-3])


# ters cevir [::-1]
print(first_name[::-1])


# tumu buyuk harf olsun --> upper
full_name = first_name + " " + last_name
print(full_name.upper())


# Ilk harfi buyuk olsun --> capitalize
print(full_name.capitalize())

# Ilk Harfleri buyuk olsun --> title
print(full_name.title())

# Ters cevir --> swapcase
print(full_name.swapcase())

# Kucuk harf olsun --> lover
print(full_name.lower())

# say --> count
print(full_name.count('n'))

# Liste icindekileri birlestir --> join
names = ("pelin", "Cem", "Bilge", "Erdem", "Deniz")
print(", ".join(names))


# parcala/ayir --> split
print(full_name.split(" "))


# Sor ::: 
print(full_name)


# Baslik seklinde mi --> istitle
print("dJaNGo".istitle())
print(last_name.istitle())



# Hepsi kucuk harf mi 
print("pelin".islower())
print(first_name.islower())

print(input("Adinizi Yaz").islower())



# belli bir karakterden basliyor mu ? starswith
print("belli bir karakterden basliyor mu ? starswith", first_name.startswith("p"))



# belli bir karakterden bitiyor mu ? endswith
print("belli bir karakterden bitiyor mu ? endswift", first_name.startswith("p"))


# Aradigim bilgi str icinde var mi / find
user_name = "erdem"
print(user_name.find("3"))

print(user_name[user_name.find("7"):])


print(full_name.lover[full_name.lover().find("n"):])





# Belli bir bilgiyi degistir / replace
print(full_name.replace("pelin", "Python"))




