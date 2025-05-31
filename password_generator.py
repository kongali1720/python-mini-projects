import random
import string

def generate_password(panjang=12):
    if panjang < 4:
        return "Panjang password minimal 4 karakter."

    semua_karakter = string.ascii_letters + string.digits + string.punctuation

    # Pastikan password punya minimal 1 huruf besar, 1 huruf kecil, 1 angka, dan 1 simbol
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Tambahkan karakter random sampai panjang tercapai
    password += random.choices(semua_karakter, k=panjang - 4)

    # Acak urutan karakter supaya tidak terprediksi
    random.shuffle(password)

    return ''.join(password)

def main():
    print("=== Generator Password ===")
    try:
        panjang = int(input("Masukkan panjang password (minimal 4): "))
    except ValueError:
        print("Input harus angka!")
        return

    hasil = generate_password(panjang)
    print(f"Password yang dihasilkan: {hasil}")

if __name__ == "__main__":
    main()
