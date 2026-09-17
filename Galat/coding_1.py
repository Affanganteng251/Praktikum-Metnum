import math

eksak_akar_2 = math.sqrt(2)

x = 1
n = int(input("Masukkan n = "))

for i in range(n):
    y = x
    x = (y + 2 / y) / 2

galat = abs(eksak_akar_2 - x)

print(f"Pendekatan    = {x:.6f}")
print(f"Eksak         = {eksak_akar_2:.6f}")
print(f"Error         = {galat:.6f}")
print(f"Error Relatif = {galat/x:.6f}")
