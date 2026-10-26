import random


def pilih_kesulitan():
    print("\n=== PILIH KESULITAN ===")
    print("1. Mudah (angka 1-10, 5 kesempatan)")
    print("2. Sedang (angka 1-50, 7 kesempatan)")
    print("3. Sulit (angka 1-100, 5 kesempatan)")

    while True:
        pilihan = input("Pilih kesulitan (1-3): ")

        if pilihan == "1":
            return 10, 5
        if pilihan == "2":
            return 50, 7
        if pilihan == "3":
            return 100, 5
        print("Pilihan tidak valid! Silakan coba lagi.")


def main_game():
    batas_angka, kesempatan = pilih_kesulitan()
    angka_rahasia = random.randint(1, batas_angka)
    print(f"\nTebak angka dari 1 sampai {batas_angka}!")
    print(f"Kamu punya {kesempatan} kesempatan.")

    for percobaan in range(1, kesempatan + 1):
        while True:
            try:
                tebakan = int(input(f"Tebakan ke-{percobaan}: "))
            except ValueError:
                print("Masukkan angka yang benar, ya!")
                continue

            if 1 <= tebakan <= batas_angka:
                break
            print(f"Masukkan angka dari 1 sampai {batas_angka}!")

        if tebakan == angka_rahasia:
            print("Benar! Kamu berhasil menang!")
            return
        if tebakan < angka_rahasia:
            print("Terlalu kecil.")
        else:
            print("Terlalu besar.")
    else:
        print(f"Kesempatan habis! Angkanya adalah {angka_rahasia}.")


def petunjuk():
    print("\n=== PETUNJUK GAME ===")
    print("1. Komputer memilih angka secara acak.")
    print("2. Kamu harus menebak angka tersebut.")
    print("3. Komputer memberi petunjuk terlalu besar atau terlalu kecil.")
    print("4. Kamu menang jika menebak dengan benar.")
    print("5. Jumlah kesempatan bergantung pada tingkat kesulitan.")


def menu_utama():
    while True:
        print("\n=====================")
        print("         GAME TEBAK ANGKA")
        print("1. Mulai permainan")
        print("2. Petunjuk")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            main_game()
        elif pilihan == "2":
            petunjuk()
        elif pilihan == "3":
            print("Terima kasih sudah bermain!")
            break
        else:
            print("Menu tidak tersedia! Coba lagi.")


if __name__ == "__main__":
    menu_utama()