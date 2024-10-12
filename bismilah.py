class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama  
        self.__ktp = ktp  
        self._limit_pinjaman = limit_pinjaman  

    def get_info(self):
        return (self.nama, self.__ktp, self._limit_pinjaman)

class Pinjaman:
    def __init__(self, debitur, pinjaman, bunga, bulan):
        self.debitur = debitur
        self.pinjaman = pinjaman
        self.bunga = bunga
        self.bulan = bulan

    def hitung_angsuran(self):
        angsuran_pokok = self.pinjaman * (self.bunga / 100)
        angsuran_bulanan = (angsuran_pokok + self.pinjaman) / self.bulan
        total_angsuran = angsuran_bulanan * self.bulan
        return angsuran_pokok, angsuran_bulanan, total_angsuran

class ManajemenDebitur:
    def __init__(self):
        self.debitur_list = []

    def tambah_debitur(self, nama, ktp, limit_pinjaman):
        if any(deb._Debitur__ktp == ktp for deb in self.debitur_list):
            print("KTP sudah ada")
            return False
        
        new_debitur = Debitur(nama, ktp, limit_pinjaman)
        self.debitur_list.append(new_debitur)
        print("Debitur berhasil ditambahkan.")
        return True

    def cari_debitur(self, nama):
        for deb in self.debitur_list:
            if deb.nama == nama:
                return deb.get_info()
        print("Debitur tidak ditemukan")
        return None

    def tampilkan_semua_debitur(self):
        if not self.debitur_list:
            print("Tidak ada debitur yang terdaftar")
            return
        
        print("\n======= Daftar Debitur =======")
        for deb in self.debitur_list:
            info = deb.get_info()
            print(f"Nama: {info[0]}, KTP: {info[1]}, Limit Pinjaman: {info[2]}")

class ManajemenPinjaman:
    def __init__(self):
        self.pinjaman_list = []

    def tambah_pinjaman(self, debitur_nama, pinjaman, bunga, bulan, manajemen_debitur):
        debitur_info = manajemen_debitur.cari_debitur(debitur_nama)
        
        if debitur_info is None:
            print("Nama debitur tidak ditemukan")
            return False
        
        if pinjaman > debitur_info[2]:
            print("Pinjaman melebihi limit")
            return False
        
        new_pinjaman = Pinjaman(debitur_info[0], pinjaman, bunga, bulan)
        self.pinjaman_list.append(new_pinjaman)
        
        print("Pinjaman berhasil ditambahkan.")
        return True

    def tampilkan_pinjaman(self):
        if not self.pinjaman_list:
            print("Tidak ada pinjaman yang terdaftar.")
            return
        
        print("\n=== Daftar Pinjaman ===")
        for pinj in self.pinjaman_list:
            angsuran_pokok, angsuran_bulanan, total_angsuran = pinj.hitung_angsuran()
            print(f"Nama: {pinj.debitur}, Pinjaman: {pinj.pinjaman}, Bunga: {pinj.bunga}, Bulan: {pinj.bulan}, "
                  f"Angsuran Pokok: {angsuran_pokok:.2f}, Angsuran Bulanan: {angsuran_bulanan:.2f}, "
                  f"Total Angsuran: {total_angsuran:.2f}")

manajemen_debitur = ManajemenDebitur()
manajemen_debitur.tambah_debitur("Alhilma", "123", 1230000)
manajemen_debitur.tambah_debitur("Firman", "987", 8880000)
manajemen_debitur.tambah_debitur("Afra", "456", 990000)
manajemen_debitur.tambah_debitur("Salsa", "218", 1110000)
manajemen_debitur.tambah_debitur("Bila", "151", 1110000)

manajemen_pinjam = ManajemenPinjaman()

while True:
    print("\n====== Aplikasi Admin Pinjol =======")
    print("1. Kelola Debitur")
    print("2. Kelola Pinjaman")
    print("3. Keluar")
    pilihan_menu_utama = input("Pilih opsi (1-3): ")
    
    if pilihan_menu_utama == '1':
        while True:
            print("\n====== Menu Debitur =======")
            print("1. Tampilkan Semua Debitur")
            print("2. Cari Debitur")
            print("3. Tambah Debitur")
            print("4. Kembali")
            pilihan_menu_debitur = input("Pilih opsi (1-4): ")

            if pilihan_menu_debitur == '1':
                manajemen_debitur.tampilkan_semua_debitur()

            elif pilihan_menu_debitur == '2':
                nama = input("Masukkan Nama Debitur yang dicari: ")
                info_debitur = manajemen_debitur.cari_debitur(nama)
                if info_debitur:
                    print(f"Debitur Ditemukan: Nama: {info_debitur[0]}, KTP: {info_debitur[1]}, Limit Pinjaman: {info_debitur[2]}")

            elif pilihan_menu_debitur == '3':
                nama = input("Masukkan Nama Debitur: ")
                ktp = input("Masukkan KTP Debitur: ")
                limit_pinjaman = float(input("Masukkan Limit Pinjaman: "))
                manajemen_debitur.tambah_debitur(nama, ktp, limit_pinjaman)

            elif pilihan_menu_debitur == '4':
                break

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    elif pilihan_menu_utama == '2':
        while True:
            print("\n====== Menu Pinjaman =======")
            print("1. Tambah Pinjaman")
            print("2. Tampilkan Pinjaman")
            print("3. Kembali")

            pilihan_menu_pinjaman = input("Pilih opsi (1-3): ")

            if pilihan_menu_pinjaman == '1':
                debitur_nama = input("Masukkan Nama Debitur untuk Tambah Pinjaman: ")
                pinjaman = float(input("Masukkan Jumlah Pinjaman: "))
                bunga = float(input("Masukkan Bunga (%): "))
                bulan = int(input("Masukkan Lama Angsuran (bulan): "))
                
                manajemen_pinjam.tambah_pinjaman(debitur_nama, pinjaman, bunga, bulan, manajemen_debitur)

            elif pilihan_menu_pinjaman == '2':
                manajemen_pinjam.tampilkan_pinjaman()

            elif pilihan_menu_pinjaman == '3':
                break

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    elif pilihan_menu_utama == '3':
        print("Terimakasih Telah menggunakan program ini")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")