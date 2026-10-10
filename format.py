name = "Serhat"
surname = "Sıkı"

# print("My name is {} {}".format(name, surname)) # format() methodu ile stringin içine değişkenleri ekleyebiliriz.
# print("My name is {1} {0}".format(name, surname)) # format() methodu ile stringin içine değişkenleri ekleyebiliriz. index numarası ile değişkenlerin sırasını değiştirebiliriz.
print("My name is {s} {n}".format(n=name, s=surname)) # format() methodu ile stringin içine değişkenleri ekleyebiliriz. keyword argümanları ile değişkenlerin sırasını değiştirebiliriz.
print("My name is {} {} and I am {} years old.".format(name, surname, "19"))

result = 200 / 700
print("The result is {}".format(result))
print("The result is {r:1.3}".format(r=result)) # 1.3, 1 basamak tam sayı ve 3 basamak ondalık sayı demektir. Yani yuvarlama yapar.

print(f"My name is {name} {surname} and I am {19} years old.") 
