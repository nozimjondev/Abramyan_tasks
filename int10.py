a = int(input("Uch xonali son kiriting: "))
hundreds = a // 100
tens = a // 10
ten = tens % 10
ones = a % 100
one = ones % 10
print(f"Siz kiritgan sonning yuzlar xonasidagi raqam: {hundreds}\nSiz kiritgan sonning o'nliklar xonasidagi raqam: {ten}\nSiz kiritgan sonning birliklar xonasidagi raqam: {one} ")