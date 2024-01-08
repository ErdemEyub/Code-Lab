# Kullanici ad bilgisini bildirene kadar devam et..
user = ""


# while True:
while len(user) < 5:
    print("Lutfen kullanici adi 5 karakter veya daha fazla olsun..")
    user = input("Kullanici adinizi giriniz: ")
    print(user)


# Kullanici ad ve soyad bilgisini bildirene kadar sormaya devam et..
first_name, last_name = "", ""
while len(first_name) < 5 and len(last_name) < 5:
    print("Lutfen kullanici adi 5 karakter veya daha fazla olsun..")
    first_name = input("Lutfen adinizi giriniz: ")
    last_name = input("Lutfen soyadinizi giriniz: ")




# Kullanici ad veya soyad bilgisini bildirene kadar sormaya devam et..

first_name, last_name = "", ""
while len(first_name) < 5 or len(last_name) < 5:
    print("Lutfen kullanici adi 5 karakter veya daha fazla olsun..")
    first_name = input("Lutfen adinizi giriniz: ")
    last_name = input("Lutfen soyadinizi giriniz: ")

