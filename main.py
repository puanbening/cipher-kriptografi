import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  
from vigenere import enkripsi_vigenere, dekripsi_vigenere
from playfair import enkripsi_playfair
from hill import enkripsi_hill

def baca_file():
    file_path = filedialog.askopenfilename(filetypes=[("File Teks", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        input_teks.delete(1.0, tk.END)
        input_teks.insert(tk.END, content)

def simpan_file(teks_hasil):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("File Teks", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(teks_hasil)

def proses_teks(aksi):
    teks = input_teks.get(1.0, tk.END).strip().replace(" ", "").replace("J", "I")
    kunci = kunci_entry.get().strip()

    if len(kunci) < 12:
        messagebox.showwarning("Error", "Panjang kunci minimal 12 karakter.")
        return

    pilihan_cipher = cipher_var.get()
    hasil = ''

    if pilihan_cipher == 'Vigenere Cipher':
        if aksi == 'encrypt':
            hasil = enkripsi_vigenere(teks, kunci)
        elif aksi == 'decrypt':
            hasil = dekripsi_vigenere(teks, kunci)

    elif pilihan_cipher == 'Playfair Cipher':
        if aksi == 'encrypt':
            hasil = enkripsi_playfair(teks, kunci)

    elif pilihan_cipher == 'Hill Cipher':
        if aksi == 'encrypt':
            hasil = enkripsi_hill(teks, kunci)

    output_teks.delete(1.0, tk.END)
    output_teks.insert(tk.END, hasil)

def update_decryption_button_visibility(*args):
    if cipher_var.get() == 'Vigenere Cipher':
        tombol_dekripsi.pack(side=tk.LEFT, padx=5)
    else:
        tombol_dekripsi.pack_forget()

window = tk.Tk()
window.title("Quiz Kriptografi")
window.geometry("700x700")

style = ttk.Style()
style.configure("Rounded.TButton", borderwidth=2, relief="flat", padding=(10, 5))

title_label = tk.Label(window, text="Quiz Kriptografi", font=("Poppins", 16, "bold"))
title_label.pack(pady=(10, 20))

cipher_var = tk.StringVar(value='Vigenere Cipher')
menu_cipher = tk.OptionMenu(window, cipher_var, 'Vigenere Cipher', 'Playfair Cipher', 'Hill Cipher')
menu_cipher.pack()

label_input = tk.Label(window, text="Input Teks Plain/Teks Cipher:")
label_input.pack()
input_teks = tk.Text(window, height=10)
input_teks.pack()

label_info = tk.Label(window, text="Unggah file (.txt)", font=("Poppins", 10))
label_info.pack(pady=(10, 0))

tombol_load = ttk.Button(window, text="Unggah File", style="Rounded.TButton", command=baca_file)
tombol_load.pack()

label_kunci = tk.Label(window, text="Masukkan Kunci (minimal 12 karakter)")
label_kunci.pack()
kunci_entry = tk.Entry(window)
kunci_entry.pack()

frame_tombol = tk.Frame(window)
frame_tombol.pack(pady=10)

tombol_enkripsi = ttk.Button(frame_tombol, text="Enkripsi", style="Rounded.TButton", command=lambda: proses_teks('encrypt'))
tombol_enkripsi.pack(side=tk.LEFT, padx=5)

tombol_dekripsi = ttk.Button(frame_tombol, text="Dekripsi", style="Rounded.TButton", command=lambda: proses_teks('decrypt'))

cipher_var.trace("w", update_decryption_button_visibility)

update_decryption_button_visibility()

label_output = tk.Label(window, text="Output Teks:")
label_output.pack()
output_teks = tk.Text(window, height=10)
output_teks.pack()

window.mainloop()
