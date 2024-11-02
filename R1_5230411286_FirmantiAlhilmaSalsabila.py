class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat


class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga


class Transaksi:
    def __init__(self, nomer_transaksi, pegawai, produk, jumlah):
        self.nomer_transaksi = nomer_transaksi
        self.pegawai = pegawai
        self.produk = produk
        self.jumlah = jumlah
        self.total_harga = self.produk.harga * self.jumlah

    def cetak_struk(self):
        print("\n=== Struk Transaksi ===")
        print(f"Nomer Transaksi: {self.nomer_transaksi}")
        print(f"Nama Pegawai: {self.pegawai.nama}")
        print(f"Nama Produk: {self.produk.nama_produk}")
        print(f"Jumlah Produk: {self.jumlah}")
        print(f"Harga Total: {self.total_harga}")
        print("========================\n")

pegawai_list = [
    Pegawai("001", "firmanti", "Jakarta"),
    Pegawai("002", "alhilma", "Bandung"),
    Pegawai("003", "salsabila", "Surabaya")
]

produk_list = [
    Produk("P001", "momogi", "Snack", 15000),
    Produk("P002", "bakso", "Makanan", 25000),
    Produk("P003", "Teh Botol", "Minuman", 10000)
]

transaksi_list = []

def menu_pegawai():
    while True:
        print("=== Menu Pegawai ===")
        print("1. Tambah Pegawai")
        print("2. Lihat Pegawai")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            nik = input("Masukkan NIK Pegawai: ")
            nama = input("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            pegawai = Pegawai(nik, nama, alamat)
            pegawai_list.append(pegawai)
            print("Pegawai berhasil ditambahkan.\n")

        elif pilihan == '2':
            print("=== Daftar Pegawai ===")
            if not pegawai_list:
                print("Belum ada pegawai yang terdaftar.\n")
            else:
                index = 1
                for pegawai in pegawai_list:
                    print(f"{index}. {pegawai.nama} (NIK: {pegawai.nik}, Alamat: {pegawai.alamat})")
                    index += 1
            print()

        elif pilihan == '3':
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")


def menu_produk():
    while True:
        print("=== Menu Produk ===")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            kode_produk = input("Masukkan Kode Produk: ")
            nama_produk = input("Masukkan Nama Produk: ")
            jenis_produk = input("Masukkan Jenis Produk (Snack/Makanan/Minuman): ")
            harga = int(input("Masukkan Harga Produk: "))
            produk = Produk(kode_produk, nama_produk, jenis_produk, harga)
            produk_list.append(produk)
            print("Produk berhasil ditambahkan.\n")

        elif pilihan == '2':
            print("=== Daftar Produk ===")
            if not produk_list:
                print("Belum ada produk yang terdaftar.\n")
            else:
                index = 1
                for produk in produk_list:
                    print(f"{index}. {produk.nama_produk} (Jenis: {produk.jenis_produk}, Harga: {produk.harga})")
                    index += 1
            print()

        elif pilihan == '3':
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")


def menu_transaksi():
    while True:
        print("=== Menu Transaksi ===")
        print("1. Lakukan Transaksi")
        print("2. Lihat Transaksi")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            if not pegawai_list:
                print("Belum ada pegawai yang terdaftar. Silakan tambahkan pegawai terlebih dahulu.\n")
                continue
            if not produk_list:
                print("Belum ada produk yang terdaftar. Silakan tambahkan produk terlebih dahulu.\n")
                continue

            print("=== Daftar Pegawai ===")
            index = 1
            for pegawai in pegawai_list:
                print(f"{index}. {pegawai.nama} (NIK: {pegawai.nik})")
                index += 1
            pegawai_index = int(input("Pilih pegawai (nomor): ")) - 1
            pegawai = pegawai_list[pegawai_index]

            print("=== Daftar Produk ===")
            index = 1
            for produk in produk_list:
                print(f"{index}. {produk.nama_produk} (Jenis: {produk.jenis_produk}, Harga: {produk.harga})")
                index += 1
            produk_index = int(input("Pilih produk (nomor): ")) - 1
            produk = produk_list[produk_index]

            jumlah = int(input("Masukkan jumlah produk: "))
            nomer_transaksi = input("Masukkan nomer transaksi: ")
            transaksi = Transaksi(nomer_transaksi, pegawai, produk, jumlah)
            transaksi_list.append(transaksi)
            transaksi.cetak_struk()

        elif pilihan == '2':
            print("=== Daftar Transaksi ===")
            if not transaksi_list:
                print("Belum ada transaksi yang dilakukan.\n")
            else:
                for transaksi in transaksi_list:
                    print(f"Nomer Transaksi: {transaksi.nomer_transaksi}, Pegawai: {transaksi.pegawai.nama}, "
                          f"Produk: {transaksi.produk.nama_produk}, Jumlah: {transaksi.jumlah}, "
                          f"Harga Total: {transaksi.total_harga}")
                print()

        elif pilihan == '3':
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")


while True:
    print("=== Menu Utama ===")
    print("1. Menu Pegawai")
    print("2. Menu Produk")
    print("3. Menu Transaksi")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        menu_pegawai()
    elif pilihan == '2':
        menu_produk()
    elif pilihan == '3':
        menu_transaksi()
    elif pilihan == '4':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.\n")
