"""
     Daire Alanı   : πr²
     Daire Çevresi :2πr 
     
     *Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r: 3.14)
"""

pi = 3.14

r = float(input("Yarı Çap: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("Dairenin Alanı: ", alan)
print("Dairenin Çevresi: ", cevre)

print("Dairenin Alanı: " + str(alan) + " " + "Dairenin Çevresi: " + str(cevre))
