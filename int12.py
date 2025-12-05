a = int(input("Uch xonali son kiriting: "))
hundreds = a // 100
tens = a // 10
ten = tens % 10
ones = a % 100
one = ones % 10
reverse_n = str(one) + str(ten) + str(hundreds)
print(f"Siz kiritgan sonning raqamlar o'rnini almashtirilgandagi  holati: {reverse_n} ")