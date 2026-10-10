name = "Sinan"
surname = "Engin"
age = 61
# print("My name is " + name + " " + surname + " and I am " + str(age) + " " + "years old.")

# print("My name is " + name + " " + surname + "\nand I am " + str(age) + " " + "years old.")

gretting = "My name is " + name + " " + surname + "\nand I am " + str(age) + " " + "years old."
length = len(gretting)

print(len(gretting)) # stringin uzunluğunu verir
print(length)
print(gretting[length - 1]) 
print(gretting[len(gretting) - 1])
print(gretting[-1]) # -1 index, son karakteri verir
print(gretting[3:6]) # 3. index dahil, 6. index dahil değil
print(gretting[3:]) # 3. index dahil, sonuna kadar
print(gretting[:16]) # baştan 16. index dahil değil
print(gretting[2:40:2]) # 2. index dahil, 40. index dahil değil, 2'şer atlayarak
