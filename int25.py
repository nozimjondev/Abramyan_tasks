
# Hafta kunlari ro'yxati
hafta_kunlari = ["payshanba", "juma", "shanba", "yakshanba", "dushanba", "seshanba", "chorshanba"]

# Foydalanuvchidan K kunini so'rash
K = int(input("1 dan 365 gacha bo'lgan K kunini kiriting: "))

# Kuning hafta kunini hisoblash
# 1-yanvar = payshanba, ya'ni 5
# indeksni hisoblash uchun (K - 5) + 1
kun_hafta_index = (K % 7) - 1 # 0: yakshanba, 1: dushanba,...6: shanba
# Ro'yxatdan nomini olish
kun_hafta_nomi = hafta_kunlari[kun_hafta_index]

print(f"{K}-kun haftaning {kun_hafta_nomi} kuniga to'g'ri keladi.")