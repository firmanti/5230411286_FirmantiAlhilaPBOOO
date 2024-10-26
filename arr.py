from flask import Flask

app = Flask(__name__)

class Order:
    def __init__(self, ID, nama, rincian, jumlah, harga):
        self._ID = ID  
        self.nama = nama
        self.rincian = rincian
        self.jumlah = jumlah
        self.harga = harga

    def set_order(self, nama, rincian, jumlah, harga):
        self.nama = nama
        self.rincian = rincian
        self.jumlah = jumlah
        self.harga = harga
        print(f"Pesanan diperbarui: Nama - {self.nama}, Rincian - {self.rincian}, Jumlah - {self.jumlah}, Harga - {self.harga}")

    def _get_order_id(self):
        return self._ID

    def get_total_harga(self):
        return self.jumlah * self.harga

class Delivery:
    def __init__(self, id, nama, informasi, tanggal, alamat):
        self._id = id  
        self.nama = nama
        self.informasi = informasi
        self.tanggal = tanggal
        self.alamat = alamat

    def proses_pengiriman(self):
        print(f"Memproses pengiriman untuk {self.nama} pada {self.tanggal} ke {self.alamat}.")

    def _get_delivery_id(self):
        return self._id


class Client:
    def __init__(self, client_id, nama, alamat):
        self.client_id = client_id
        self.nama = nama
        self.alamat = alamat
        self.pesanan = []  

    def buat_pesanan(self, nama_pesanan, rincian, jumlah, harga):
        order_id = len(self.pesanan) + 1  
        pesanan_baru = Order(order_id, nama_pesanan, rincian, jumlah, harga)
        self.pesanan.append(pesanan_baru)
        print(f"Pesanan dibuat: {nama_pesanan} (ID: {order_id}) untuk klien {self.nama}")
        return pesanan_baru

    def lihat_pesanan(self):
        if not self.pesanan:
            print("Tidak ada pesanan.")
        else:
            print(f"Daftar pesanan untuk klien {self.nama}:")
            for pesanan in self.pesanan:
                print(f"ID: {pesanan._get_order_id()}, Nama: {pesanan.nama}, Rincian: {pesanan.rincian}, Jumlah: {pesanan.jumlah}, Total Harga: {pesanan.get_total_harga()}")


if __name__ == "__main__":
    klien1 = Client(1, "Firmanti", "Jalan Pagilaran")

    while True:
        print("\n=== Program Pesanan Klien ===")
        print("1. Buat pesanan baru")
        print("2. Lihat semua pesanan")
        print("3. Proses pengiriman")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == "1":
            nama_pesanan = input("Masukkan nama pesanan: ")
            rincian = input("Masukkan rincian pesanan: ")
            jumlah = int(input("Masukkan jumlah: "))
            harga = float(input("Masukkan harga per item: "))
            klien1.buat_pesanan(nama_pesanan, rincian, jumlah, harga)

        elif pilihan == "2":
            klien1.lihat_pesanan()

        elif pilihan == "3":
            if not klien1.pesanan:
                print("Tidak ada pesanan yang tersedia untuk pengiriman.")
            else:
                pesanan = klien1.pesanan[0]
                pengiriman = Delivery(pesanan._get_order_id(), klien1.nama, f"Mengirim {pesanan.nama}", "2024-10-27", klien1.alamat)
                pengiriman.proses_pengiriman()

        elif pilihan == "4":
            print("Terimakasih telah menggukan program ini.")
            break

        else:
            print("Opsi tidak valid. Silakan pilih lagi.")


