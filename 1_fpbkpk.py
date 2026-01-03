def hitung_fpbkpk(a, b):
    angka1 = a
    angka2 = b

    while b != 0:
        a, b = b, a % b
    fpb = a

    kpk = (angka1 * angka2) // fpb

    return fpb, kpk

try:
    n1 = int (input("ketik angka pertama: "))
    n2 = int (input("ketik angka kedua: "))

    hasil_fpb, hasil_kpk = hitung_fpbkpk(n1, n2)

    print(f"FPB dari {n1} dan {n2} adalah: {hasil_fpb}")
    print(f"KPK dari {n1} dan {n2} adalah: {hasil_kpk}")

except ValueError:
    print("Harap masukkan angka yang valid")