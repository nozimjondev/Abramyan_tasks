A = int(input("To'g'ri to'rtburchakning A tomoni: "))
B = int(input("To'g'ri to'rtburchakning B tomoni: "))
C = int(input("Kvadratning C tomoni: "))

n = (A // C) * (B // C)   # joylashadigan kvadratlar soni
remain = A * B - n * (C * C)  # joylashmay qolgan qismi yuzasi

print(f"Kvadratlar soni: {n}")
print(f"Joylashmay qolgan qismi yuzasi: {remain}")

