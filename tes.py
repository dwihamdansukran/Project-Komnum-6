def f(x):
    return x**3 - 3*x + 7  # Fungsi f(x)

def metode_tabel(x0, x1, H, N):
    # Mencetak header tabel dengan tambahan kolom f(xi)
    print("\n----------------------------------------------------------------------------")
    print("|                             Metode Tabel                                 |")
    print("----------------------------------------------------------------------------")
    print(f"|{'Iterasi':<10}|{'xi':<15}|{'f(xi)':<15}|{'f(x(i+1))':<15}|{'f(xi)*f(x(i+1))':<15}|")
    print("----------------------------------------------------------------------------")

    iterasi = 0
    xi = x0
    xi_lanjut = x1
    
    while iterasi < N:
        f_xi = f(xi)  # Nilai f(xi)
        f_xi_lanjut = f(xi_lanjut)  # Nilai f(xi+1)
        
        # Perhitungan error (selisih xi+1 dan xi)
        iterasiError = abs(xi_lanjut - xi)
        
        # Menampilkan setiap iterasi dalam format tabel dengan pembatasan 6 angka di belakang koma
        print(f"|{iterasi+1:<10}|{xi:<15.3f}|{f_xi:<15.3f}|{xi_lanjut:<15.3f}|{f_xi*xi_lanjut:<15.3f}|")
        
        # Cek apakah error sudah di bawah batas toleransi
        if iterasiError < H:
            print("----------------------------------------------------------------------------")
            print("Kondisi error terpenuhi.")
            return xi_lanjut, f(xi_lanjut)  # Mengembalikan nilai akar dan f(akar)
        
        # Update nilai xi dan xi_next untuk iterasi selanjutnya
        xi = xi_lanjut
        xi_lanjut = xi_lanjut - f_xi_lanjut  # Misalnya menggunakan f(x) untuk memperbarui xi_next
        
        iterasi += 1
    
    print("----------------------------------------------------------------------------")
    return xi_lanjut, f(xi_lanjut)  # Mengembalikan nilai dari iterasi sebelumnya dan f(akar)

# Fungsi utama untuk input dari user
def main():
    x0 = float(input("\nMasukkan X bawah(xa)\t\t: "))
    x1 = float(input("Masukkan X atas (xb)\t\t: "))
    H = float(input("Masukkan step pembagi (H)\t: "))
    N = int(input("Masukkan maksimum iterasi (N)\t: "))
    
    nilai_akar, f_akar = metode_tabel(x0, x1, H, N)
    print(f"Akar terletak di x: {nilai_akar:.6f}")
    print(f"Dengan Nilai f(x): {f_akar:.6f}\n")

# Jalankan program
main()
