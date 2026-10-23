# f(x) = x^5 + x^3 + 3 = 0
def f(x):
    return x**5 + x**3 + 3
x0 = -1
x1 = -1.1
toleransi = 0.0001
maks_iterasi = 100
r = 1
while r <= maks_iterasi:
    f_x0 = f(x0)
    f_x1 = f(x1)
    x_hasil = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
    selisih = abs(x_hasil - x1)
    print(
        f"Iterasi {r}: x = {x_hasil:.5f}, f(x) = {f(x_hasil):.5f}, selisih = {selisih:.5f}"
    )
    if selisih < toleransi:
        break
    # geser: x1 jadi x0, x_hasil jadi x1 (untuk putaran berikutnya)
    x0 = x1
    x1 = x_hasil
    r += 1
print(f"f({x_hasil:.5f}) = {f(x_hasil):.5f}")
print(f"\nHampiran akar: {x_hasil:.5f}")
