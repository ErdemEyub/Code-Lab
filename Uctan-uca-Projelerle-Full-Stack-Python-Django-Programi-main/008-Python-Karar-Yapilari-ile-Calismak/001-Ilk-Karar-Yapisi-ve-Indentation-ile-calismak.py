# Yas Bilgisi int Olarak Girildi Mi
# Eger Kosul
# Dogruysa Bunu Yap...
# Degilse
# Bunu Yap...

age = input("Yasinizi Giriniz: ")

age = input("Yasinizi Giriniz: ")
print(type(age))

if age.isdigit():
    age = int(age)
    age += 1

print(age)


# Kullanici Adi Dogru mu
SYS_USER_NAME = 'lorem ipsum'
user_name = input("Kullanici Adinizi Giriniz: ").lower()
# user_name = user_name.lower()

if SYS_USER_NAME == user_name:
    print("Kullanici Adi Dogru")
else:
    print("Kullanici Adi Yanlis")





# Kullanici 18  Yasindan Buyuk mu

if age.isdigit() and int(age) > 18:
    print("18 Yasindan Buyuk")