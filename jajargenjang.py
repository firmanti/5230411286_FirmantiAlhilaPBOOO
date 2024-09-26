#Tugas Bangun Ruang JajarGenjang 
#Nama : Firmanti Alhilma Salsabila
#NPM : 5230411286


def hitung_luas(jumlah_alas, tinggi):
    return jumlah_alas * tinggi

def hitung_keliling(sisi_a, sisi_b):
    return 2 * (sisi_a + sisi_b)

def main():
    print("=== Program Hitung Jajar Genjang ===")
    print("1. Hitung Luas")
    print("2. Hitung Keliling")
    print("3. Keluar")

    while True:
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            alas = float(input("Masukkan panjang alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            luas = hitung_luas(alas, tinggi)
            print(f"Luas jajar genjang adalah: {luas:.2f} satuan luas")
        
        elif pilihan == '2':
            sisi_a = float(input("Masukkan panjang sisi a: "))
            sisi_b = float(input("Masukkan panjang sisi b: "))
            keliling = hitung_keliling(sisi_a, sisi_b)
            print(f"Keliling jajar genjang adalah: {keliling:.2f} satuan panjang")
        
        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

