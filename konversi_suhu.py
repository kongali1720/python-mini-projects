def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_ke_celcius(f):
    return (f - 32) * 5/9

def main():
    print("=== Konversi Suhu ===")
    print("Pilih konversi:")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")

    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        try:
            c = float(input("Masukkan suhu dalam Celcius: "))
            f = celcius_ke_fahrenheit(c)
            print(f"{c}°C = {f:.2f}°F")
        except ValueError:
            print("Input harus angka!")
    elif pilihan == '2':
        try:
            f = float(input("Masukkan suhu dalam Fahrenheit: "))
            c = fahrenheit_ke_celcius(f)
            print(f"{f}°F = {c:.2f}°C")
        except ValueError:
            print("Input harus angka!")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
