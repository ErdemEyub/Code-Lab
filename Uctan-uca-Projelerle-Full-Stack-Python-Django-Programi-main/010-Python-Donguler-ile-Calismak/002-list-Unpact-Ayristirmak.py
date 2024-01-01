user_info = ["admin", "123234sdfsdzawa23", ]
user, password = user_info
# print(user_info[0], user_info[1])
# print(user, password)

user_detail = ["admin", 
               "12314134sfsaf", 
               "admin@admin.com", 
               "mail-master@admin.com", 
]

user_name, user_password, *mail_list = user_detail
print(user_name, user_password, mail_list)

products = [
    ["laptop", "mouse", "keybord"],
    ["monitor", "printer"],
    "Sony XYZ",
]

*otherproducts, headphone = products

print("other_products", otherproducts)
print("headphone", headphone)

# liste icindeki verileri tek tek islemek
users = ["Aysen", "Fatma", "Cigdem", "Hasan", "Ahmet", "Mehmet"]

# item ve index bilgisi ile listleri dongude kullanmak --> enumerate
for index, item in enumerate(users):
    if index % 2 != 0:
        print(index, user)
          



