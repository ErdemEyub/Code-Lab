# test skoru rakamsal bilgi icermemelidir
# test skoru 0 ile 100 arasinda olmalidir
# test Skoru 45 alti ise Kaldi 
# test skoru 45 ve uzeri ise gecer 
# test skoru 55 ve uzeri ise orta   
# test skoru 75 ve uzeri ise iyi
# test skoru 85 ve uzeri ise cok iyi

from curses.ascii import isdigit


test_score = input("Test Skorunu Giriniz: ")

if not test_score.isdigit():
    print("Lütfen Rakamsal Bilgi Giriniz")
# else:
#     if int(test_score) <= 100:

elif 0 <= int(test_score) <= 100:
    test_score = int(test_score)
    if test_score >= 85:
        result = "Pekiyi"
    elif test_score >= 75:
        result = "Iyi"  
    elif test_score >= 55:
        result = "Orta"
    elif test_score >= 45:
        result = "Gecer"
    elif test_score < 45:
        result = "Kaldi"
else:
    print("Lütfen 0 ile 100 arasinda bir deger giriniz")

print(result )




