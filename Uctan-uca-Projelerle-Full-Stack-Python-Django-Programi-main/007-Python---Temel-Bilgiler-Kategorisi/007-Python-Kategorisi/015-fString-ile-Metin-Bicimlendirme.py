# https://pyformat.info/

first_name = "Pelin"
last_name = "KaYa"

full_name = f"{first_name} {last_name}"

# Birden fazla degisken icindeki bilgiyi birlestirmek
hello = first_name[0].upper() + ". " + last_name # P. seklinde yazdirdik
print(hello)


# fString ile Yazimi:
hello = f"Merhaba {first_name} {last_name}"
print(hello)

hello = f"Merhaba {first_name[0].upper()}. {last_name}" # P. seklinde yazdik
print(hello)
  

# Hesaplama yaparak str sonuc donmek
# print("sonuc: " + 10 * 10) # Calismaz cunku str ve int birlesmez... 
print("sonuc: ",   10 * 10, sep=" ") #  
result = "sonuc: 10 * 10"
result = "sonuc: " + str(10 * 10)
print(result)

result = f"Sonuc: {10 * 10}"
print(result)


# fuction icinde yapilan hesaplamanin sonucunu donmek
def calculate(number):
    return number * number

result = f"Sonuc: {calculate(10)}"
print("multiply fonksiyonu kullanildi:", result)
print(f"Sonuc: {calculate(10)}")
 



# uzun iceriklerin belli bir kismini gostermek
print(f"{result[:4]}")


# yazilari ortalamak veya saga yaslamak
print("-" * 30)
print(f"{full_name:-^30}")
print(f"{'Python':->30}")
print(f"{'Django':->30}")
print("-" * 30)

# belli bir uzunlukta int yapilar olusturmak. 00034 gibi











