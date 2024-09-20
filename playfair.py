def matriks_playfair(kunci):
    alfabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matriks = []
    
    for huruf in kunci.upper():
        if huruf not in matriks and huruf in alfabet:
            matriks.append(huruf)
    
    for huruf in alfabet:
        if huruf not in matriks:
            matriks.append(huruf)
    
    return [matriks[i:i + 5] for i in range(0, 25, 5)]

def temukan_posisi(matriks, huruf):
    for baris in range(5):
        for kolom in range(5):
            if matriks[baris][kolom] == huruf:
                return baris, kolom
    return None

def enkripsi_playfair(teks_plain, kunci):
    teks_plain = teks_plain.replace("J", "I").upper()
    matriks = matriks_playfair(kunci)
    teks_cipher = ''
    i = 0

    while i < len(teks_plain):
        if i + 1 >= len(teks_plain) or teks_plain[i] == teks_plain[i + 1]:
            teks_plain = teks_plain[:i + 1] + 'X' + teks_plain[i + 1:]
        
        pasangan = teks_plain[i:i + 2]
        i += 2
        posisi1 = temukan_posisi(matriks, pasangan[0])
        posisi2 = temukan_posisi(matriks, pasangan[1])

        if posisi1 is None or posisi2 is None:
            return ''

        baris1, kolom1 = posisi1
        baris2, kolom2 = posisi2

        if baris1 == baris2:
            teks_cipher += matriks[baris1][(kolom1 + 1) % 5] + matriks[baris2][(kolom2 + 1) % 5]
        elif kolom1 == kolom2:
            teks_cipher += matriks[(baris1 + 1) % 5][kolom1] + matriks[(baris2 + 1) % 5][kolom2]
        else:
            teks_cipher += matriks[baris1][kolom2] + matriks[baris2][kolom1]

    return teks_cipher
