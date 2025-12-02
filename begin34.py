'''X kg shokolad A so`m turadi va Y kg konfet B so`m turadi. 
1 kg shokolad 1 kg konfetdan qancha qimmat turishini aniqlovchi programma tuzilsin'''
X = float(input("X kg shokolad massasini kiriting (kg): "))
A = float(input("A so'm narxini kiriting (so'm): "))
Y = float(input("Y kg konfet massasini kiriting (kg): "))
B = float(input("B so'm narxini kiriting (so'm): "))

choc_per_kg = A / X
candy_per_kg = B / Y
chocolate_expense = choc_per_kg - candy_per_kg
candy_expense = candy_per_kg - choc_per_kg
print(f"1 kg chocolate narxi: {choc_per_kg} so'm")
print(f"1 kg konfet narxi: {candy_per_kg} so'm")

if choc_per_kg > candy_per_kg:
    print(f"1 kg shokolad narxi 1kg konfetdan {chocolate_expense} so'm qimmatroq. ")
elif candy_per_kg > choc_per_kg:
    print(f"1 kg konfet narxi 1kg shokoladdan {candy_expense} so'm qimmatroq. ")



