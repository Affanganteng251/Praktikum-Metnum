import math
# f(x) = x^2 - 2x - 3 = 0
def g2(x):
    return 3 / (x - 2)
def turunan_g2(x):
    return -3 / (x - 2) ** 2
print(g2(11))
print(turunan_g2(11))
# cek konvergen
x0 = 11
turunan_di_x0 = turunan_g2(x0)
print(f"g2'({x0}) = {turunan_di_x0}")
if abs(turunan_di_x0) < 1:
    print("konvergen, iterasi selanjutnya bakal aman")
else:
    print("skip, divergen")
# Langkag Iterasi
x_lama = 11
toleransi = 0.001
r = 0
while True:
    x_baru = g2(x_lama)
    selisih = abs(x_baru - x_lama)
    turunan = turunan_g2(x_baru)
    print(
        f"Iterasi {r+1}: x = {x_baru:.5f}, selisih = {selisih:.5f} g'(x) = {turunan:.5f}"
    )
    if selisih < toleransi:
        break
    x_lama = x_baru
    r += 1
def f(x):
    return x**2 - 2 * x - 3
print(f"f({x_baru:.5f}) = {f(x_baru):.5f}")
print(f"Hampiran Akar: {x_baru:.5f}")
