a = float(input("A koeffisentini kiriting: (A 0dan katta bo'lsin) "))
b = float(input("B koeffisentini kiriting: "))
c = float(input("C koeffisentini kiriting: "))
d = b ** 2 - 4 * a * c
print(d)
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a) 
if d > 0:
    print(f"x1 = {x1}, x2 = {x2} " )
elif d == 0:
    print(f"x1, x2 = {x1}")
else:
    print("Diskriminant 0 dan kichkina. ")


