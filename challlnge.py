import mysql.connector

# Fungsi untuk koneksi ke database
def connect_to_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="penjualan"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Membuat database dan tabel
def setup_database():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS penjualan")
        cursor.execute("USE penjualan")

        # Tabel Pegawai
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pegawai (
                NIK INT PRIMARY KEY,
                Nama VARCHAR(100) NOT NULL,
                Alamat TEXT NOT NULL
            )
        """)

        # Tabel Transaksi
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Transaksi (
                NoTransaksi INT PRIMARY KEY,
                NIK INT NOT NULL,
                DetailTransaksi TEXT,
                FOREIGN KEY (NIK) REFERENCES Pegawai(NIK) ON DELETE CASCADE
            )
        """)

        # Tabel Produk
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produk (
                KodeProduk INT PRIMARY KEY,
                NamaProduk VARCHAR(100) NOT NULL,
                JenisProduk ENUM('Snack', 'Makanan', 'Minuman') NOT NULL,
                HargaProduk DECIMAL(10, 2) NOT NULL
            )
        """)

        # Tabel Struk
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Struk (
                IdStruk INT AUTO_INCREMENT PRIMARY KEY,
                NoTransaksi INT NOT NULL,
                KodeProduk INT NOT NULL,
                JumlahProduk INT NOT NULL,
                TotalHarga DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (NoTransaksi) REFERENCES Transaksi(NoTransaksi) ON DELETE CASCADE,
                FOREIGN KEY (KodeProduk) REFERENCES Produk(KodeProduk) ON DELETE CASCADE
            )
        """)

        print("Database dan tabel berhasil dibuat sesuai struktur.")
        db.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Validasi Input
def validasi_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input salah! Masukkan angka yang valid.")

def validasi_string(prompt):
    while True:
        data = input(prompt)
        if data.isalpha():
            return data
        else:
            print("Input salah! Hanya boleh huruf.")

def validasi_jenis_produk():
    while True:
        print("\nPilih Jenis Produk:")
        print("1. Snack")
        print("2. Makanan")
        print("3. Minuman")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            return "Snack"
        elif pilihan == "2":
            return "Makanan"
        elif pilihan == "3":
            return "Minuman"
        else:
            print("Pilihan tidak valid, coba lagi.")


def add_pegawai(nik, nama, alamat):
    db = connect_to_db()
    if db is None:
        return
    cursor = db.cursor()
    try:
        sql = "INSERT INTO Pegawai (NIK, Nama, Alamat) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nik, nama, alamat))
        db.commit()
        print("Pegawai berhasil ditambahkan!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()

def add_produk(kode_produk, nama_produk, jenis_produk, harga_produk):
    db = connect_to_db()
    if db is None:
        return
    cursor = db.cursor()
    try:
        sql = "INSERT INTO Produk (KodeProduk, NamaProduk, JenisProduk, HargaProduk) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (kode_produk, nama_produk, jenis_produk, harga_produk))
        db.commit()
        print("Produk berhasil ditambahkan!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()

def add_transaksi(no_transaksi, nik, detail_transaksi):
    db = connect_to_db()
    if db is None:
        return
    cursor = db.cursor()
    try:
        sql = "INSERT INTO Transaksi (NoTransaksi, NIK, DetailTransaksi) VALUES (%s, %s, %s)"
        cursor.execute(sql, (no_transaksi, nik, detail_transaksi))
        db.commit()
        print("Transaksi berhasil ditambahkan!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()

def add_struk(no_transaksi, kode_produk, jumlah_produk):
    db = connect_to_db()
    if db is None:
        return
    cursor = db.cursor()
    try:
        cursor.execute("SELECT HargaProduk FROM Produk WHERE KodeProduk = %s", (kode_produk,))
        result = cursor.fetchone()
        if not result:
            print("Produk tidak ditemukan.")
            return
        harga_produk = result[0]
        total_harga = harga_produk * jumlah_produk

        sql = """
            INSERT INTO Struk (NoTransaksi, KodeProduk, JumlahProduk, TotalHarga) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (no_transaksi, kode_produk, jumlah_produk, total_harga))
        db.commit()
        print("Struk berhasil ditambahkan!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()

def tampilkan_data(query, headers):
    db = connect_to_db()
    if db is None:
        return
    cursor = db.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n" + headers)
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()

def hapus_data_tabel(tabel, kolom, id_value):
    db = connect_to_db()
    if db is None:
        return
    cursor = db.cursor()
    try:
        sql = f"DELETE FROM {tabel} WHERE {kolom} = %s"
        cursor.execute(sql, (id_value,))
        db.commit()
        print(f"Data dari tabel {tabel} berhasil dihapus!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()

def populate_initial_data():
    db = connect_to_db()
    if db is None:
        return
    cursor = db.cursor()

    try:
        # Tambahkan data awal untuk Pegawai
        pegawai_data = [
            (101, "Firmanti", "Jl. Magelang"),
            (102, "Alhilma", "Jl. Kaliurang"),
            (103, "Salsa", "Jl. Adisucipto"),
            (104, "Bila", "Jl. Palagan"),
            (105, "Cici", "Jl. Solo"),
        ]
        cursor.executemany("INSERT IGNORE INTO Pegawai (NIK, Nama, Alamat) VALUES (%s, %s, %s)", pegawai_data)

        # Tambahkan data awal untuk Produk
        produk_data = [
            (201, "Keripik Pisang", "Snack", 50000.00),
            (202, "Bakso", "Makanan", 25000.00),
            (203, "Matcha Latte ", "Minuman", 48000.00),
            (204, "Americano", "Minuman", 30000.00),
            (205, "Cilok", "Snack", 12000.00),
        ]
        cursor.executemany("INSERT IGNORE INTO Produk (KodeProduk, NamaProduk, JenisProduk, HargaProduk) VALUES (%s, %s, %s, %s)", produk_data)

        # Tambahkan data awal untuk Transaksi
        transaksi_data = [
            (301, 101, "Pembelian Keripik Pisang dan Matcha Latte"),
            (302, 102, "Pembelian Bakso dan Cilok"),
            (303, 103, "Pembelian Americano"),
            (304, 104, "Pembelian Bakso dan Matcha Latte"),
            (305, 105, "Pembelian Keripik Pisang"),
        ]
        cursor.executemany("INSERT IGNORE INTO Transaksi (NoTransaksi, NIK, DetailTransaksi) VALUES (%s, %s, %s)", transaksi_data)

        # Tambahkan data awal untuk Struk
        struk_data = [
            (301, 201, 2),  # NoTransaksi 301, KodeProduk 201, Jumlah 2
            (302, 202, 1),  # NoTransaksi 302, KodeProduk 202, Jumlah 1
            (302, 205, 3),  # NoTransaksi 302, KodeProduk 205, Jumlah 3
            (303, 204, 1),  # NoTransaksi 303, KodeProduk 204, Jumlah 1
            (304, 203, 4),  # NoTransaksi 304, KodeProduk 203, Jumlah 4
        ]

        for no_transaksi, kode_produk, jumlah_produk in struk_data:
            cursor.execute("SELECT HargaProduk FROM Produk WHERE KodeProduk = %s", (kode_produk,))
            result = cursor.fetchone()
            if result:
                harga_produk = result[0]
                total_harga = harga_produk * jumlah_produk
                cursor.execute(
                    "INSERT IGNORE INTO Struk (NoTransaksi, KodeProduk, JumlahProduk, TotalHarga) VALUES (%s, %s, %s, %s)",
                    (no_transaksi, kode_produk, jumlah_produk, total_harga)
                )

        
        db.commit()
        print("Data awal berhasil ditambahkan!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        db.close()


# Menu Utama dan Sub-Menu
def menu_pegawai():
    while True:
        print("\n--- Menu Pegawai ---")
        print("1. Tambah Pegawai")
        print("2. Tampilkan Pegawai")
        print("3. Hapus Pegawai")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih menu: ")

        if choice == "1":
            nik = validasi_angka("Masukkan NIK Pegawai: ")
            nama = validasi_string("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            add_pegawai(nik, nama, alamat)

        elif choice == "2":
            query = "SELECT * FROM Pegawai"
            headers = "--- Data Pegawai ---\nNIK | Nama | Alamat"
            tampilkan_data(query, headers)

        elif choice == "3":
            nik = validasi_angka("Masukkan NIK Pegawai yang ingin dihapus: ")
            hapus_data_tabel("Pegawai", "NIK", nik)

        elif choice == "4":
            break

        else:
            print("Pilihan tidak valid! Coba lagi.")

    

def menu_produk():
    while True:
        print("\n--- Menu Produk ---")
        print("1. Tambah Produk")
        print("2. Tampilkan Produk")
        print("3. Hapus Produk")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih menu: ")

        if choice == "1":
            kode_produk = validasi_angka("Masukkan Kode Produk: ")
            nama_produk = input("Masukkan Nama Produk: ")
            jenis_produk = validasi_jenis_produk()
            harga_produk = float(input("Masukkan Harga Produk: "))
            add_produk(kode_produk, nama_produk, jenis_produk, harga_produk)

        elif choice == "2":
            query = "SELECT * FROM Produk"
            headers = "--- Data Produk ---\nKode | Nama | Jenis | Harga"
            tampilkan_data(query, headers)

        elif choice == "3":
            kode_produk = validasi_angka("Masukkan Kode Produk yang ingin dihapus: ")
            hapus_data_tabel("Produk", "KodeProduk", kode_produk)

        elif choice == "4":
            break

        else:
            print("Pilihan tidak valid! Coba lagi.")


def menu_transaksi():
    while True:
        print("\n--- Menu Transaksi ---")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Transaksi")
        print("3. Hapus Transaksi")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih menu: ")

        if choice == "1":
            no_transaksi = validasi_angka("Masukkan No Transaksi: ")
            nik = validasi_angka("Masukkan NIK Pegawai yang melakukan transaksi: ")
            detail_transaksi = input("Masukkan detail transaksi: ")
            add_transaksi(no_transaksi, nik, detail_transaksi)

        elif choice == "2":
            query = "SELECT * FROM Transaksi"
            headers = "--- Data Transaksi ---\nNoTransaksi | NIK | Detail"
            tampilkan_data(query, headers)

        elif choice == "3":
            no_transaksi = validasi_angka("Masukkan No Transaksi yang ingin dihapus: ")
            hapus_data_tabel("Transaksi", "NoTransaksi", no_transaksi)

        elif choice == "4":
            break

        else:
            print("Pilihan tidak valid! Coba lagi.")


def menu_struk():
    while True:
        print("\n--- Menu Struk ---")
        print("1. Tambah Struk")
        print("2. Tampilkan Struk")
        print("3. Hapus Struk")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih menu: ")

        if choice == "1":
            no_transaksi = validasi_angka("Masukkan No Transaksi: ")
            kode_produk = validasi_angka("Masukkan Kode Produk: ")
            jumlah_produk = validasi_angka("Masukkan Jumlah Produk: ")
            add_struk(no_transaksi, kode_produk, jumlah_produk)

        elif choice == "2":
            query = """
                SELECT 
                    s.IdStruk, 
                    s.NoTransaksi, 
                    p.NamaProduk, 
                    s.JumlahProduk, 
                    s.TotalHarga
                FROM Struk s
                JOIN Produk p ON s.KodeProduk = p.KodeProduk
            """
            headers = "--- Data Struk ---\nIdStruk | NoTransaksi | NamaProduk | Jumlah | TotalHarga"
            tampilkan_data(query, headers)

        elif choice == "3":
            id_struk = validasi_angka("Masukkan ID Struk yang ingin dihapus: ")
            hapus_data_tabel("Struk", "IdStruk", id_struk)

        elif choice == "4":
            break

        else:
            print("Pilihan tidak valid! Coba lagi.")


def main_menu():
    while True:
        print("\n--- Menu Utama ---")
        print("1. Pegawai")
        print("2. Produk")
        print("3. Transaksi")
        print("4. Struk")
        print("5. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            menu_pegawai()
        elif choice == "2":
            menu_produk()
        elif choice == "3":
            menu_transaksi()
        elif choice == "4":
            menu_struk()
        elif choice == "5":
            print("Terima kasih telah menggunakan sistem!")
            break
        else:
            print("Pilihan tidak valid!")



if __name__ == "__main__":
    setup_database()
    populate_initial_data()
    main_menu()

