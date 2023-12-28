age = input("Yasinizi Giriniz: ")

# Kullanici 18 Yasindan Buyuk mu

# if age.isdigit() and int(age) > 18:
#     print("18 Yasindan Buyuksunuz")
# else:
#     print("18 Yasindan Kucuksunuz")

if not age.isdigit():
    print('Yas Bilgisini Girmediniz')
else:
    if int(age) > 18:
        print("18 yasindan buyuk")
    else:
        print("18 yasinda kucuk")

 




