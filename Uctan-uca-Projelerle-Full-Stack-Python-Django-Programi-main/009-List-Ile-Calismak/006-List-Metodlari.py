# liste icinde kac oge var -> len
liste = [1, 2, 3, 4, 5]
eleman_sayisi = len(liste)
print("Liste eleman sayısı:", eleman_sayisi)

# liste icinde oge var mı? -> in
# Yöntem 1: if ile yineleme kullanma
oge = [
    1,
    2,
    3,
    4,
]
liste_icinde_oge_varmi = False
for i in liste:
    if i == oge:
        liste_icinde_oge_varmi = True
        break

# Yöntem 2: in keyword kullanma
liste_icinde_oge_varmi = oge in liste

# Yöntem 3: any keyword kullanma
liste_icinde_oge_varmi = any(i == oge for i in liste)

# liste icinde bir oge kac kez var? -> count
from collections import Counter

# İstenen listenizi tanımlayın
list_icinde = ['a', 'b', 'c', 'a', 'b', 'a']

# Listenin elemanlarını ve tekrar sayılarını sayma
frequency = Counter(list_icinde)

# Sonuçları gösterme
for key, value in frequency.items():
    print(f"{key} adlı oge {value} kez var")

from collections import Counter

# İstenen listenizi tanımlayın
list_icinde = ['a', 'b', 'c', 'a', 'b', 'a']

# Listenin elemanlarını ve tekrar sayılarını sayma
frequency = Counter(list_icinde)

# Sonuçları gösterme
for key, value in frequency.items():
    print(f"{key} adlı oge {value} kez var")

# liste icindeki ogenin yeri(index) nedir? -> index
# List oluşturma
liste = ['kedi', 'köpek', 'kala', 'kuş', 'domuz']

# Aranacak değer
aranan_deger = 'köpek'

# Öğenin yeri(index) bulma
for index, deger in enumerate(liste):
    if deger == aranan_deger:
        print(f"{aranan_deger} listede bulunduğu yer(index): {index}")
        break

# liste icindeki oge adlarini sil? -> remove



    

