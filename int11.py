a = int(input("Uch xonali son kiriting: "))
hundreds = a // 100
tens = a // 10
ten = tens % 10
ones = a % 100
one = ones % 10
sum = hundreds + ten + one 
print(f"Siz kiritgan sonning raqamlar yig'indisi: {sum}")