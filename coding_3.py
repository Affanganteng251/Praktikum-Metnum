import math

x = float(input("Input nilai x : "))
n = int(input("Input nilai n : "))

eksak = math.exp(x)

p = 0
for i in range(n + 1):
    p = p + (x**i / math.factorial(i))

galat = abs(eksak - p)

print(f"Eksak      = {eksak:.15f}")
print(f"Pendekatan = {p:.15f}")
print(f"Error      = {galat:.15f}")
