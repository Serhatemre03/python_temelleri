maasMehmet = 5000
maasAhmet = 4000
vergi = 0.27

print(maasMehmet - (maasMehmet * vergi))
print(maasAhmet - (maasAhmet * vergi))

# Değişken Tanımlama Kuralları
# 1. Değişken isimleri harf veya alt çizgi ile başlamalı

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

# 2. Degişken tanımlarken büyük/küçük harf duyarlılığı vardır. Örn: number1 ve Number1 farklı değişkenlerdir.

age = 20
Age = 30

print(age)
print(Age)

# 3. Değişken tanımlarken Türkçe karakterler kullanılmamalıdır. Örn: yaş = 20 gibi bir tanımlama yapılmamalıdır.

# yaş = 20 burası hatalı bir tanımlamadır. Yaş değişkeni tanımlanamaz.
# AGE = 20 burası doğru bir tanımlamadır. AGE değişkeni tanımlanabilir.

x = 1                # intreger
y = 2.3              # float
name = "Bulut"       # string
isStudent = True     # boolean

# x, y, name, isStudent = (1, 2.3, "Bulut", True)

a = '10'
b = '20'
print(a + b) # => 1020

first_name = "Alparslan"
last_name = " Koyuncu"

print(first_name + last_name) # Alparslan Koyuncu
