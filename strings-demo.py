website = "http://www.serhatemre.com"
course = "Phthon Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?

print(len(course))

# 2- 'website' içinden www karakterlerini alın.

print(website[7:10])

# 3- 'website' içinden com karakterlerini alın.

print(website[-3:])

# 4- 'course' içinden ilk 15 ve son 15 karaklerini alın.

print(course[:15]) 
print(course[-15:])

# 5- 'course' ifadesindeki karakterileri tersten yazdırın.

print(course[::-1])

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.'

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

harf = 'W'

print("Hello {}orld".format(harf))

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

print('abc' * 3)
result = 'abc' * 3


print(result)


