a = int(input("Uch xonali son kiriting: ")) # 246
hundreds = a // 100 #2
tens = a // 10 #24
ten = tens % 10 # 4
ones = a % 100 #46
one = ones % 10 #6
merged = str (one) + str(tens)
print(f" Siz kiritgan sonning o'ngdan birinchi raqamini o'chirib chap tarafiga yozishdan hosil bo`lgan son: {merged}")