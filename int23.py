n = int(input("Kun boshidan boshlab necha sekund o'tganini kiriting: "))

n = n % 86400            # 24 soatdan oshsa, ortig'i olinadi
soat = n // 3600
minut = (n % 3600) // 60
sekund = n % 60

print(f"{soat} soat, {minut} minut, {sekund} sekund.")