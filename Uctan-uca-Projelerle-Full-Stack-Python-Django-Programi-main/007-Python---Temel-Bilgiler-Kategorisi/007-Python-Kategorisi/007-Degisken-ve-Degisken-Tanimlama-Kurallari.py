# Degisken Isimleri Nasil Olmalidir ?
# degisken isimleri kucuk harfle baslar
# degisken isimleri kelimenin ilk harfi buyuk olur
# deger atanmadigi degiskenlere "None" verilir.
# degisken isimleri tamamen sayilar iceremez
def isim_olustur(degisken):
    if not degisken:  # eger degiskene atama yapilmamis ise None 
        return "None"
    isim = str(degisken)   # diger
    return isim
sayi1=5
sayi2=6
print(sayi1+sayi2)
print(isim_olustur(sayi1))
print(isim_olustur(sayi2))
print(isim_olustur(sayi1+sayi2))
print(isim_olustur(sayi1-sayi2))
print(isim_olustur(sayi1*sayi2))
print(isim_olustur(sayi1/sayi2))
print(isim_olustur(sayi1//sayi2))
print(isim_olustur(sayi1**sayi2))
print(isim_olustur(sayi1%sayi2))
print(isim_olustur(sayi1>sayi2))
print(isim_olustur(sayi1<sayi2))
print(isim_olustur(sayi1==sayi2))
print(isim_olustur(sayi1!=sayi2))
print(isim_olustur(sayi1>=sayi2))
print(isim_olustur(sayi1<=sayi2))
print(isim_olustur(sayi1 and sayi2))
print(isim_olustur(sayi1 or sayi2))
print(isim_olustur(not sayi1))
print(isim_olustur(not sayi2))
print(isim_olustur(sayi1 is sayi2))
print(isim_olustur(sayi1 is not sayi2))
print("*" * 30)
print("*" * 30)

# Degisken Isimleri Nasil Olmalidir ?
# g14 = "Python"
# print(g14)
# print("*" * 30)
x = 1
# x, i, y, z gibi Degisken Isimleri Kullanmayin


# Degisken Isimleri Ingilizce mi olmali ?
# kullanici_adi = "Gamze"
first_name = "Gamze" # Lutfen Degisken Isimlerini Ingilizce Kullanalim



# Degisken Isimleri Rakamla Baslayabilir mi ?
# 123_Deneme = "Deneme" --> Rakam ile Baslayamaz.
d_123 = "Deneme" # Bu Kullanilabilir


# Degisken Isimleri Buyuk Harfle Baslayabilir mi ?
password = "1234" # Buyuk harf ile Olmali miydi? olur
SERWER_IP = "127.0.0.1" # Değişmeyecek Kesin Bilgi oldugu Durumlarda kullanılır


# Degisken Isimleri Birden Fazla kez Kullanilabilir mi ?
print(first_name)
first_name = "Aylin"
print(first_name) # Once gamze sonra aylin diye run edecek, dinamik bir yapı 
# vardır kodlamada bu yüzden değiştirilebilir.


# Degisken Isimleri Buyuk Harf Yazmak ile 
# Kucuk Harf Yazmak Arasinda Fark Var mi ?
# Eger Buyuk Harf ile yaziliyorsa bu Bilgi Degistirilmeyecek Bir Bilgidir...


# Degisken Isimleri Kucuk Harfle(user_name) ve 
# Buyuk Harfle(USER_NAME) Yazilsa da Ayni Sonucu Alir miyiz ?
user_name = "lorem ipsum"
USER_NAME = "lorem ipsum"

print(user_name)
print(USER_NAME)



