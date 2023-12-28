# Input ile first_name bilgisini al
# Input ile last_name bilgisini al
# Input ile year_of_birth bilgisini al
# first_name ve last_name karakter sayilarini yaz
# fString ile kullanicinin adinin ilk harfi ve buyuk olacak sekilde full_name yazdir
# fString ile kullanicinin yasini yazdir ve gelecek seneki yasini yazdir
# 18 yasindan buyukse True olacak sekilde bilgisini don

import datetime

first_name = input("First name: ")
last_name = input("Last name: ")
year_of_birth = int(input("Year of birth: "))
print(f"Ad Karakter Sayisi: {len(first_name)},Soyad Karakter Sayisi: {len(last_name)}")
full_name = f"{first_name[0]}. {last_name}".upper()
print(full_name)

current_year = datetime.datetime.now().year
age = current_year - year_of_birth
next_year = current_year + 1
print(f"Yasiniz: {age}, Gelecek Yil ... Yasinda Olacaksiniz")

import datetime

first_name = input("First name: ")
last_name = input("Last name: ")
year_of_birth = int(input("Year of birth: "))

print(f"Ad Karakter Sayisi: {len(first_name)},Soyad Karakter Sayisi: {len(last_name)}")
full_name = f"{first_name[0]}. {last_name}".upper()
print(full_name)

current_year = datetime.datetime.now().year
age = current_year - year_of_birth
next_year = current_year + 1

print(f"Yasiniz: {age}, Gelecek Yil ... Yasinda Olacaksiniz: {age + 1}")
