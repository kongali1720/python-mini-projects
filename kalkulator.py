def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagi tidak boleh 0!"
    return a / b

def main():
    print("=== Kalkulator Sederhana ===")
    print("Operasi: +, -, *, /")
    
    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus angka! Coba lagi.")
            continue

        op = input("Pilih operasi (+, -, *, /): ")
        if op == '+':
            hasil = tambah(angka1, angka2)
        elif op == '-':
            hasil = kurang(angka1, angka2)
        elif op == '*':
            hasil = kali(angka1, angka2)
        elif op == '/':
            hasil = bagi(angka1, angka2)
        else:
            print("Operasi tidak dikenal, coba lagi.")
            continue

        print(f"Hasil: {hasil}")

        lanjut = input("Mau hitung lagi? (y/n): ").lower()
        if lanjut != 'y':
            print("Terima kasih sudah menggunakan kalkulator sederhana!")
            break

if __name__ == "__main__":
    main()
