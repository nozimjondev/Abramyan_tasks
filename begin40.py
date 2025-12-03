a1 = float(input("A1 koeffisentini kiriting: "))
b1 = float(input("B1 koeffisentini kiriting: "))
c1 = float(input("C1 koeffisentini kiriting: "))
a2 = float(input("A2 koeffisentini kiriting: "))
b2 = float(input("B2 koeffisentini kiriting: "))
c2 = float(input("C2 koeffisentini kiriting: "))
d = a1 * b2 - a2 * b1
if d != 0:
    x = (b1 * c2 - b2 * c1) / d
    y = (a2 * c1 - a1 * c2) / d
    print(f"x = {x}, y = {y}")
else:
    print("Tenglama sistemasining yechimi yo'q yoki cheksiz ko'p yechimlari bor.")
