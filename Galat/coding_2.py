import math

eksak_akar_2 = math.sqrt(2)

x = 1
e = 1
n = 0

while True:
    y = x
    x = (y + 2 / y) / 2
    e = abs(x - y)

    if e >= 0.00001:
        n = n + 1
        print(f"Iterasi ke-{n}")
        print(f"x = {x:.15f}")
        print(f"e = {e:.15f}\n")

    if e < 0.00001:
        break

galat = abs(eksak_akar_2 - y)

print(f"Eksak          = {eksak_akar_2:.15f}")
print(f"Jumlah iterasi = {n}")
print(f"Pendekatan     = {y:.15f}")
print(f"Error          = {galat:.15f}")


# Iterasi	e	Apakah e >= 0.00001?	Ditampilin?
# 1	0.5	Ya	 n jadi 1, print "Iterasi ke-1"
# 2	0.08333	Ya	 n jadi 2, print "Iterasi ke-2"
# 3	0.00245	Ya	 n jadi 3, print "Iterasi ke-3"
# 4	0.0000021	Tidak (lebih kecil)	❌ dilewati, nggak di-print, n tetep 3
