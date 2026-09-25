import numpy as np


# pakai baris i untuk menolkan A[h, i] semua baris di bawahnya, b dikenai operasi yang sama
def nolkan_bawah_pivot(A, b, i):
    n = len(A)
    for h in range(i + 1, n):
        m = A[h, i] / A[i, i]
        A[h, :] -= m * A[i, :]
        b[h] -= m * b[i]


# jalankan nolkan_bawah_pivot untuk tiap kolom; berhenti dengan error kalau pivot ketemu nol
def eliminasi_maju(A, b):
    n = len(A)
    for i in range(n - 1):
        if A[i, i] == 0:
            raise ValueError(
                "pivot nol di baris %d, tanpa tukar baris eliminasi berhenti" % i
            )
        nolkan_bawah_pivot(A, b, i)
    if A[n - 1, n - 1] == 0:
        raise ValueError("matriks singular, solusi tidak tunggal")
    return A, b


# hitung x dari A yang sudah segitiga atas, dari baris paling bawah naik ke atas
def substitusi_mundur(U, y):
    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]
    return x


# pembungkus: salin input -> eliminasi maju tanpa tukar baris -> substitusi mundur
def gauss(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    U, y = eliminasi_maju(A, b)
    return substitusi_mundur(U, y), U


if __name__ == "__main__":
    print("1) pivot kebetulan bagus")
    A = [[1, 2, 1], [2, 3, 3], [3, 2, 1]]
    b = [4, 10, 5]
    x, U = gauss(A, b)
    print("   U =\n", np.round(U, 4))
    print("   x =", np.round(x, 4))
    print("   cek A x =", np.round(np.array(A, dtype=float) @ x, 4))

    print()
    print("2) pivot nol")
    try:
        gauss([[0, 2], [1, 3]], [4, 7])
    except ValueError as e:
        print("  ", e)

    print()
    print("3) pivot sangat kecil")
    Ak = np.array([[1e-16, 1.0], [1.0, 1.0]])
    bk = np.array([1.0, 2.0])
    print("   tanpa tukar x =", gauss(Ak, bk)[0])
    print("   numpy         x =", np.linalg.solve(Ak, bk))