def enkripsi_vigenere(teks_plain, kunci):
    kunci = kunci.upper()
    teks_cipher = ''
    j = 0
    for huruf in teks_plain.upper():
        if huruf.isalpha():
            geser = (ord(huruf) - ord('A') + ord(kunci[j % len(kunci)]) - ord('A')) % 26
            teks_cipher += chr(geser + ord('A'))
            j += 1
        else:
            teks_cipher += huruf  
    return teks_cipher

def dekripsi_vigenere(teks_cipher, kunci):
    kunci = kunci.upper()
    teks_plain = ''
    j = 0
    for huruf in teks_cipher.upper():
        if huruf.isalpha():
            geser = (ord(huruf) - ord('A') - (ord(kunci[j % len(kunci)]) - ord('A')) + 26) % 26
            teks_plain += chr(geser + ord('A'))
            j += 1
        else:
            teks_plain += huruf  
    return teks_plain