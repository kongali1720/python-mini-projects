import os
import subprocess
import sys

projects = {
    "1": {
        "name": "Kalkulator Sederhana",
        "folder": "kalkulator-sederhana",
        "file": "kalkulator.py"
    },
    "2": {
        "name": "Game Tebak Angka",
        "folder": "game-tebak-angka",
        "file": "tebak_angka.py"
    },
    "3": {
        "name": "Stopwatch",
        "folder": "stopwatch",
        "file": "stopwatch.py"
    },
    "4": {
        "name": "Konversi Suhu",
        "folder": "konversi-suhu",
        "file": "konversi_suhu.py"
    },
    "5": {
        "name": "Generator Password",
        "folder": "generator-password",
        "file": "password_generator.py"
    },
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_project(choice):
    proj = projects.get(choice)
    if not proj:
        print("Pilihan tidak valid! Coba lagi ya.")
        return

    script_path = os.path.join(proj["folder"], proj["file"])

    if not os.path.isfile(script_path):
        print(f"File {script_path} tidak ditemukan.")
        return

    print(f"\nMenjalankan proyek: {proj['name']}\n---\n")

    try:
        # Jalankan script Python sesuai OS
        subprocess.run([sys.executable, script_path])
    except Exception as e:
        print("Error saat menjalankan proyek:", e)

def main():
    while True:
        clear_screen()
        print("=== Python Mini Projects Launcher ===")
        for key, val in projects.items():
            print(f"{key}. {val['name']}")
        print("0. Keluar")

        choice = input("\nPilih nomor proyek yang mau dijalankan: ").strip()
        if choice == "0":
            print("Terima kasih sudah mencoba! Sampai jumpa! 👋")
            break

        run_project(choice)
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
