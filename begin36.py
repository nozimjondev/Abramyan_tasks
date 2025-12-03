v1 = float(input("Birinchi avtomobilning tezligi (V1 km/soat)ni kiriting: "))
v2 = float(input("Ikkinchi avtomobilning tezligi (V2 km/ soat)ni kiriting: "))
s = float(input("Ular orasiddagi masofa (S km)ni kiriting: "))
t = float(input("Ular bir biridan uzoqlasha boshlasa, qancha vaqtdan keyingi masofani bilmoqchi siz, (T soat)ni kiriting:  "))
S_new = s + (v1 + v2) * t
print(f"Avtomobillar orasidagi yangi masofa: {S_new} km")