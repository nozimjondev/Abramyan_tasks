""" Sonlar o`qida A, B, C nuqtalar berilgan.
 C nuqta A va B nuqtalar orasida joylashgan.
 AC va BC kesmalar uzunligining ko`paytmasini toping"""
A = 10
B = 40
C = 14

AC = abs(C - A)
BC = abs(C - B)
Multiple = AC * BC
print(f'AC = {AC}, BC = {BC} and Multiple = {Multiple}')