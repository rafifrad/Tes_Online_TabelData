def cek_kategori(n):
    hasil = []

    hasil.append('bulat')

    if n < 0:
        hasil.append('negatif')
    else:
        hasil.append('cacah')

        if n == 0:
            hasil.append('nol')
        else:
            hasil.append('asli')
            
            if n % 2 == 0:  
                hasil.append('genap')
            else:
                hasil.append('ganjil')

            if n > 1:
                prima = True
                for i in range(2, n):
                    if n % i == 0:
                        prima = False
                        break
            
                if prima:
                    hasil.append('prima')
                else:
                    hasil.append('komposit')

    return hasil

angka_input = input("ketik angka: ")

kategori = cek_kategori(int(angka_input))

print(kategori)