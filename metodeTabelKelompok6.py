import numpy as np
import pandas as pd
from tabulate import tabulate
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Fungsi untuk menjalankan evaluasi fungsi yang dimasukkan pengguna
def f(x):
    try:
        return eval(func_input.get())
    except Exception as e:
        messagebox.showerror("Error", f"Error in function evaluation: {e}")
        return None

# Fungsi utama untuk melakukan perhitungan dan menampilkan hasil
def hitung():
    global data  # Menyimpan data ke variabel global untuk digunakan di plot
    try:
        N = int(entry_N.get())  # Mengambil jumlah langkah N dari input
        batas_bawah = float(entry_bawah.get())  # Mengambil batas bawah dari input
        batas_atas = float(entry_atas.get())  # Mengambil batas atas dari input

        # xera Menyiapkan list untuk menyimpan data tabel

        # Melakukan iterasi untuk menghitung xi, f(xi), dan f(xi+1)
        for i in range(1, N + 2):
            xi = batas_bawah + (i - 1) * H
            fi = f(xi)

            if i < N + 1:
                fi_next = f(batas_bawah + i * H)
            else:
                fi_next = None

            product = fi * fi_next if fi_next is not None else None
            data.append([xi, fi, fi_next, product])

            # Mengecek kondisi |f(xk)| < |f(xk+1)| dan menyimpan iterasi pertama yang memenuhi syarat
            if chosen_iteration is None and i < N + 1 and abs(fi) < abs(fi_next):
                chosen_iteration = i
                chosen_x = xi

        # Membuat DataFrame untuk menyimpan hasil perhitungan
        df = pd.DataFrame(data, columns=['      xi', '      f(xi) ', '          f(x(i+1)) ', '      f(xi) * f(x(i+1))'])

        # Menghapus konten sebelumnya dari TextBox hasil
        result_box.delete(1.0, tk.END)

        # Menggunakan tabulate untuk merapikan tampilan tabel dalam bentuk grid
        table_str = tabulate(df, headers='keys', floatfmt=".4f", numalign="center")
        result_box.insert(tk.END, table_str)  # Menampilkan tabel dalam TextBox

        # xera Menampilkan hasil iterasi yang memenuhi syarat
    
# Fungsi untuk menampilkan plot
def tampilkan_plot():
    if not data:
        messagebox.showerror("Error", "Tidak ada data untuk diplot. Harap hitung terlebih dahulu.")
        return

    # Memisahkan data untuk plot
    x_values = [row[0] for row in data]
    y_values = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')
    plt.title('Plot Fungsi f(x)')
    plt.xlabel('xi')
    plt.ylabel('f(xi)')
    plt.grid(True)
    plt.axhline(0, color='red',linewidth=2.0, ls='--')  # Garis horizontal pada y=0
    plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Garis vertikal pada x=0
    plt.show()

# Fungsi untuk menambah karakter ke input fungsi saat tombol di keyboard virtual ditekan
def tambahkan_karakter(value):
    func_input.insert(tk.END, value)

# Membuat aplikasi utama
root = tk.Tk()
root.title("Metode Tabel Kelompok 6")
root.geometry("500x950")  # Menambah tinggi window untuk keyboard
root.configure(bg='#001F3F')  # Warna background navy

# Judul Aplikasi
judul = tk.Label(root, text="Metode Tabel", font=('Comic Sans MS', 16, 'bold'), bg='#001F3F', fg='#FFFFFF')
judul.pack(pady=10)

# xera Frame utama untuk mengelompokkan input, hasil, dan keyboard

# Bingkai untuk input pengguna
frame_input = tk.Frame(main_frame, bg='#001F3F', borderwidth=2, relief='groove')  # Bingkai dengan relief dan border
frame_input.pack(pady=8, fill=tk.X)

# Gaya Label
label_style = {'bg': '#001F3F', 'fg': '#FFFFFF', 'font': ('Comic Sans MS', 12)}

# Input fungsi
tk.Label(frame_input, text="Fungsi f(x):", **label_style).grid(row=0, column=0, padx=5, pady=5)
func_input = tk.Entry(frame_input, width=30, font=('Comic Sans MS', 12))
func_input.grid(row=0, column=1, padx=5, pady=5)

# Input jumlah langkah N
tk.Label(frame_input, text="Jumlah Langkah (N):", **label_style).grid(row=1, column=0, padx=5, pady=5)
entry_N = tk.Entry(frame_input, width=10, font=('Comic Sans MS', 12))
entry_N.grid(row=1, column=1, padx=5, pady=5)

# Input batas bawah
tk.Label(frame_input, text="Batas Bawah:", **label_style).grid(row=2, column=0 padx=5, pady=5)
entry_bawah = tk.Entry(frame_input, width=10, font=('Comic Sans MS', 12))
entry_bawah.grid(row=2, column=1, padx=5, pady=5)

# Input batas atas
tk.Label(frame_input, text="Batas Atas:", **label_style).grid(row=3, column=0, padx=5, pady=5)
entry_atas = tk.Entry(frame_input, width=10, font=('Comic Sans MS', 12))
entry_atas.grid(row=3, column=1, padx=5, pady=5)

# xera Tombol untuk menjalankan perhitungan

# Tombol untuk menampilkan plot
btn_plot = tk.Button(main_frame, text="Tampilkan Plot", command=show_plot, font=('Arial', 12, 'bold'), bg='#8B4000', fg='#FFFFFF', width=20)
btn_plot.pack(pady=7)

# Bingkai untuk text box hasil
frame_result = tk.Frame(main_frame, bg='#001F3F', borderwidth=2, relief='groove')  # Bingkai untuk hasil
frame_result.pack(pady=7, fill=tk.BOTH)

# Text box untuk menampilkan 
result_box = tk.Text(frame_result, height=40, width=70, bg='#FFFFFF', fg='#000000', font=('Comic Sans MS', 10))  # Menggunakan font Comic Sans MS
result_box.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
