import numpy as np

def enkripsi_hill(teks_plain, kunci):
    teks_plain = teks_plain.upper().replace(" ", "")
    kunci = kunci.upper().replace(" ", "")
    
    n = int(len(kunci) ** 0.5)
    matriks_kunci = np.array([ord(huruf) - ord('A') for huruf in kunci]).reshape(n, n)
    
    while len(teks_plain) % n != 0:
        teks_plain += 'X'
    
    teks_cipher = ''
    for i in range(0, len(teks_plain), n):
        blok = np.array([ord(huruf) - ord('A') for huruf in teks_plain[i:i + n]])
        blok_cipher = np.dot(matriks_kunci, blok) % 26
        teks_cipher += ''.join(chr(num + ord('A')) for num in blok_cipher)
    
    return teks_cipher
