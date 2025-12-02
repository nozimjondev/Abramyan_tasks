
X = float(input("X kg konfet massasini kiriting (kg): "))
A = float(input("A so'm narxini kiriting (so'm): "))
Y = float(input("Y kg konfet massasini kiriting (kg): "))

price_per_kg = A / X
price_for_Y_kg = price_per_kg * Y

print(f"1 kg konfet narxi: {price_per_kg:.2f} so'm")
print(f"{Y} kg konfet narxi: {price_for_Y_kg:.2f} so'm")