# 1. print



price = 200
tax = price * 0.18
price_with_tax = price + tax


print(price_with_tax)
print("*" * 10, "Sonuc:", "*" * 10, sep="---", end=":")
print(price_with_tax)
  

# 2. help
# help(print) 

# 3. type
age = 33
is_active = False
user_name = "user"

print(type(age), type(is_active), type(user_name))
print(type(age) == int)
print(type(is_active) == bool)

# 4. len
print(len(user_name))
print(len(age))

# 5. dir
print(dir(user_name))
print(dir(str))

print("*" * 30)

print(dir(is_active))

# 6. input
user_name = input("User name: ")
print(user_name)
print(type(user_name))
age = input("Age: ")
print(age)
print(type(age))
print(type(int(age)))
print(type(float(age)))
print(type(bool(age)))

# 7. round
print(round(2.5))
print(round(2.4))

# 8. ord
print(ord("a"))
print(ord("A"))
print(ord("1"))
print(ord(" "))

# 9. chr
print(chr(97))
print(chr(65))
print(chr(49))
print(chr(32))

# 10. function
def say_hello():
    print("Hello")
    print("World")
    print("Hello World")

say_hello()


# 11. function with parameter
def say_hello(name):
    print("Hello", name)
    print("Hello", name, "again")


say_hello("Ali")
say_hello("Veli")
say_hello("Can")
say_hello("Ayse")


# 12. function with return
def say_hello(name):
    return "Hello " + name
greeting = say_hello("Ali")


print(greeting)
print(type(greeting))
print(len(greeting))
print(dir(greeting))
print(greeting.upper())
print(greeting.lower())
print(greeting.title())
print(greeting.capitalize())
print(greeting.swapcase())

# 13. function with parameter and return
def say_hello(name):
    return "Hello " + name


greeting = say_hello("Ali")
print(greeting)
print(type(greeting))




# 14. function with default parameter
def say_hello(name="Guest"):
    return "Hello " + name






# 15. function with multiple parameter
def say_hello(name, surname):
    return "Hello " + name + " " + surname





# 16. function with multiple parameter and default parameter
def say_hello(name, surname="Guest"):
    return "Hello " + name + " " + surname
print(say_hello("John"))
print(say_hello("John", "Doe"))
print(say_hello("Jane"))
print(say_hello("Jane", "Doe"))




