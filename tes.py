# Meminta pengguna untuk memasukkan persamaan f(x), batas a dan b, serta nilai N dan H
def f(x, persamaan):
    return eval(persamaan)

def metode_bisection_tabel(a, b, N, H, persamaan):
    # Membuat header tabel
    print("--------------------------------------------------------------")
    print("|  i  |    xi   |   f(xi)   |  f(xi+1)  |   f(xi) * f(xi+1)  |")
    print("--------------------------------------------------------------")

    nilai_xi = [a + i * H for i in range(N+1)]  # Membuat daftar nilai xi
    for i in range(N):
        xi = nilai_xi[i]
        f_xi = f(xi, persamaan)
        
        # Jika iterasi terakhir, nilai f(xi+1) dianggap 0
        if i == N-1:
            f_xi_berikutnya = 0
        else:
            xi_berikutnya = nilai_xi[i + 1]
            f_xi_berikutnya = f(xi_berikutnya, persamaan)

        hasil_kali = f_xi * f_xi_berikutnya

        # Mencetak baris tabel
        print(f"| {i:^3} | {xi:^7.4f} | {f_xi:^9.4f} | {f_xi_berikutnya:^9.4f} | {hasil_kali:^18.4f} |")

    print("--------------------------------------------------------------")

# Meminta input dari pengguna
persamaan = input("Masukkan persamaan f(x), misal x**3 - 3*x + 7: ")
a = float(input("Masukkan batas bawah a: "))
b = float(input("Masukkan batas atas b: "))
N = int(input("Masukkan jumlah iterasi N: "))
H = float(input("Masukkan nilai step pembagi H: "))

# Memanggil fungsi dengan input dari pengguna
metode_bisection_tabel(a, b, N, H, persamaan)

