x = 3.14159265358
x_bar = 3.14

galat = abs(x - x_bar)
print(galat)

error_relatif = abs((x - x_bar) / x)
print(error_relatif)

error_rh = abs((x - x_bar) / x_bar)
print(error_rh)

persentase_relatif = error_relatif * 100
print(persentase_relatif)

persentase_rh = error_rh * 100
print(persentase_rh)
