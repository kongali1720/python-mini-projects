import time

def main():
    print("=== Stopwatch Sederhana ===")
    input("Tekan Enter untuk memulai...")
    start = time.time()
    print("Stopwatch berjalan... Tekan Enter lagi untuk berhenti.")
    input()
    end = time.time()
    elapsed = end - start
    menit = int(elapsed // 60)
    detik = elapsed % 60
    print(f"Waktu yang berlalu: {menit} menit {detik:.2f} detik")

if __name__ == "__main__":
    main()
