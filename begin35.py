# Qayiqning tezligi (v) Daryo oqimining tezligi (u) Oqim bo‘yicha yurish vaqti (t₁) Oqimga qarshi yurish vaqti (t₂)
v = float(input("Qayiqning tezligi (V km/soat)ni kiriting: "))
u = float(input("Daryo oqimining tezligi (U km/soat)ni kiriting (V > U): ")) 
t1 = float(input("Oqim bo'yicha yurish vaqti (T1 soat)ni kiriting: "))
t2 = float(input("Oqimga qarshi yurish vaqti (T2 soat)ni kiriting: "))
S = (v + u) * t1 + (v - u) * t2
print(f"Qayiqning yurgan yo'li {S} km")