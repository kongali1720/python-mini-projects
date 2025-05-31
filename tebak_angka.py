import random

def main():
    print("=== Game Tebak Angka ===")
    print("Aku sudah memilih angka antara 1 sampai 100.")
    print("Coba tebak ya!")

    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
            percobaan += 1
        except ValueError:
            print("Input harus angka bulat! Coba lagi.")
            continue

        if tebakan < angka_rahasia:
            print("Terlalu kecil, coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu besar, coba lagi.")
        else:
            print(f"🎉 Selamat! Tebakanmu benar dalam {percobaan} percobaan.")
            break

    print("Terima kasih sudah bermain!")

if __name__ == "__main__":
    main()
