class Makanan:
    def __init__(self):
        self.menu_makanan = {}

    def tambah_makanan(self, nama, harga):
        self.menu_makanan[nama] = harga
        print(f"Menu makanan '{nama}' telah ditambahkan dengan harga {harga}.")

    def tampilkan_makanan(self):
        if not self.menu_makanan:
            print("Tidak ada menu makanan yang tersedia.")
        else:
            print("Daftar Menu Makanan:")
            for nama, harga in self.menu_makanan.items():
                print(f"- {nama} : {harga}")


class Minuman:
    def __init__(self):
        self.menu_minuman = {}

    def tambah_minuman(self, nama, harga):
        self.menu_minuman[nama] = harga
        print(f"Menu minuman '{nama}' telah ditambahkan dengan harga {harga}.")

    def tampilkan_minuman(self):
        if not self.menu_minuman:
            print("Tidak ada menu minuman yang tersedia.")
        else:
            print("Daftar Menu Minuman:")
            for nama, harga in self.menu_minuman.items():
                print(f"- {nama} : {harga}")


class DaftarMenu:
    def __init__(self):
        self.makanan = Makanan()
        self.minuman = Minuman()

    def tampilkan_menu(self):
        while True:
            print("\n===== Menu Utama ======")
            print("1. Daftar Menu Makanan")
            print("2. Daftar Menu Minuman")
            print("3. Tambah Daftar")
            print("4. Keluar")

            pilihan = input("Pilih opsi (1-4): ")

            if pilihan == '1':
                self.makanan.tampilkan_makanan()

            elif pilihan == '2':
                self.minuman.tampilkan_minuman()

            elif pilihan == '3':
                self.tambah_daftar()

            elif pilihan == '4':
                print("Terima kasih! Program selesai.")
                break

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_daftar(self):
        while True:
            print("\n===== Submenu Tambah Daftar ======")
            print("1. Tambah Makanan")
            print("2. Tambah Minuman")
            print("3. Kembali ke Menu Utama")

            sub_pilihan = input("Pilih opsi (1-3): ")

            if sub_pilihan == '1':
                while True:
                    nama = input("Masukkan nama makanan: ")
                    if nama.isalpha():  # Memastikan nama hanya berisi huruf
                        break
                    else:
                        print("Nama makanan tidak valid! Harap masukkan hanya huruf.")

                while True:
                    try:
                        harga = float(input("Masukkan harga makanan: "))
                        break
                    except ValueError:
                        print("Harga tidak valid! Harap masukkan angka.")

                self.makanan.tambah_makanan(nama, harga)

            elif sub_pilihan == '2':
                while True:
                    nama = input("Masukkan nama minuman: ")
                    if nama.isalpha():  # Memastikan nama hanya berisi huruf
                        break
                    else:
                        print("Nama minuman tidak valid! Harap masukkan hanya huruf.")

                while True:
                    try:
                        harga = float(input("Masukkan harga minuman: "))
                        break
                    except ValueError:
                        print("Harga tidak valid! Harap masukkan angka.")

                self.minuman.tambah_minuman(nama, harga)

            elif sub_pilihan == '3':
                break  # Kembali ke menu utama

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")


def main():
    daftar_menu = DaftarMenu()
    daftar_menu.tampilkan_menu()


if __name__ == "__main__":
    main()

