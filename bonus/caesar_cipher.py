def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("🔐 Caesar Cipher - Text Encryptor/Decryptor 🔐")
    print("----------------------------------------------")
    choice = input("Pilih mode (e untuk encrypt / d untuk decrypt): ").lower()

    if choice not in ['e', 'd']:
        print("Pilihan tidak valid. Harus 'e' atau 'd'.")
        return

    text = input("Masukkan teks: ")
    try:
        shift = int(input("Masukkan jumlah pergeseran (1-25): "))
        if shift < 1 or shift > 25:
            raise ValueError
    except ValueError:
        print("Pergeseran harus berupa angka antara 1 sampai 25.")
        return

    if choice == 'e':
        result = caesar_encrypt(text, shift)
        print("\n🔐 Hasil Enkripsi:")
    else:
        result = caesar_decrypt(text, shift)
        print("\n🔓 Hasil Dekripsi:")

    print(result)
    print("\n✅ Selesai!")

if __name__ == "__main__":
    main()
