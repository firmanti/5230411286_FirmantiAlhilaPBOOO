class Music:
    def __init__(self, judul, penyanyi, genre):  
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def tampilMusik(musicList):
        if not musicList:
            print("Tidak ada musik yang tersedia.")
        else:
            musicList.sort(key=lambda musik: musik.judul)
            print("\nDaftar Musik:")
            for musik in musicList:
                print(f"Judul: {musik.judul}, Penyanyi: {musik.penyanyi}, Genre: {musik.genre}")
        print()

    def tambahMusik(musicList, genre):
        judul = input("Masukkan judul musik: ")
        penyanyi = input("Masukkan nama penyanyi: ")
        musik_baru = Music(judul, penyanyi, genre)
        musicList.append(musik_baru)
        print(f"Musik '{judul}' berhasil ditambahkan.\n")

    def cariMusik(musicList):
        penyanyi_dicari = input("\nMasukkan Penyanyi yang Ingin Dicari: ")
        print(f"\nJudul {'Penyanyi':<20} {'Genre':<20}")
        print("="*60)
        found = False
        for musik in musicList:
            if musik.penyanyi.lower() == penyanyi_dicari.lower():
                print(f"{musik.judul:<20} {musik.penyanyi:<20} {musik.genre:<20}")
                found = True
        if not found:
            print("Lagu tidak ditemukan.")
        input("\nTekan Enter untuk melanjutkan...")

    def hapusMusik(musicList):
        judul = input("Masukkan judul musik yang ingin dihapus: ")
        for i in range(len(musicList)):
            if musicList[i].judul == judul:
                del musicList[i]
                print(f"Musik dengan judul '{judul}' telah dihapus.\n")
                return
        print(f"Musik dengan judul '{judul}' tidak ditemukan.\n")


def main():
    musicList = [
        Music("Kan Goo", "bright", "Thailand"),
        Music("why dont you stay", "jeff satur", "Thailand"),
        Music("seng bang bang", "indigo", "Thailand"),
        Music("all-time famous band since the 2000s", "potato", "Thailand"),
        Music("Blush", "Zom Marie", "Thailand"),
        Music("Fine", "Taeyeon", "Korea"),
        Music("i will show you", "ailee", "Korea"),
        Music("Good day", "IU", "Korea"),
        Music("beautiful", "crush", "Korea"),
        Music("no.1", "BoA", "Korea"),
        Music("west coast", "Lana Del Rey", "English"),
        Music("As It Was", "Harry Styles", "English"),
        Music("perfect", "Ed Sheeran", "English"),
        Music("levitating", "Dua Lipa", "English"),
        Music("cinnamon girl", "Lana Del Rey", "English")
    ]

    while True:
        print("================ Playlist Music ================")
        print("0. keluar")
        print("1. Thailand Song")
        print("2. Korean Song")
        print("3. English Song")
        print("4. Tampilkan semua musik")
        print("5. Cari Musik")
        print("6. Hapus Musik")

        pilihan = input("Masukkan Pilihan Menu: ")

        if pilihan == '0':
            break

        elif pilihan == '1':
            while True:
                print("\nThailand Songs Menu:")
                print("0. Kembali")
                print("1. Tampilkan Lagu")
                print("2. Tambah Lagu")
                sub_pilihan = input("Masukkan Pilihan: ")

                if sub_pilihan == '0':
                    break
                elif sub_pilihan == '1':
                    thailand_songs = [m for m in musicList  if "Thailand" in m.genre]
                    Music.tampilMusik(thailand_songs)
                elif sub_pilihan == '2':
                    genre = 'Thailand'
                    Music.tambahMusik(musicList, genre)

        elif pilihan == '2':
            while True:
                print("\nKorean Songs Menu:")
                print("0. Kembali")
                print("1. Tampilkan Lagu")
                print("2. Tambah Lagu")
                sub_pilihan = input("Masukkan Pilihan: ")

                if sub_pilihan == '0':
                    break
                elif sub_pilihan == '1':
                    korean_songs = [m for m in musicList  if "Korea" in m.genre]
                    Music.tampilMusik(korean_songs)
                elif sub_pilihan == '2':
                    genre = 'K-Song'
                    Music.tambahMusik(musicList, genre)

        elif pilihan == '3':
            while True:
                print("\nEnglish Songs Menu:")
                print("0. Kembali")
                print("1. Tampilkan Lagu")
                print("2. Tambah Lagu")
                sub_pilihan = input("Masukkan Pilihan: ")

                if sub_pilihan == '0':
                    break
                elif sub_pilihan == '1':
                    english_songs = [m for m in musicList if "English" in m.genre]
                    Music.tampilMusik(english_songs)
                elif sub_pilihan == '2':
                    genre = 'English'
                    Music.tambahMusik(musicList, genre)

        elif pilihan == '4':
            Music.tambahMusik(musicList)

        elif pilihan == '5':
            Music.cariMusik(musicList)

        elif pilihan == '6':
            Music.hapusMusik(musicList)


if __name__ == "__main__": 
    main()
    
