import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import sys
from sklearn.preprocessing import LabelEncoder

#fungsi preprocessing data
def preprocess_data(file_path):
    try:
        # Membaca data
        data = pd.read_excel(file_path)
        print("Data berhasil dimuat.\n")
        print("Preview data:")
        print(data.head())

        # Pisahkan kolom numerik dan kategorikal
        numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
        categorical_columns = data.select_dtypes(include=['object']).columns

        # Mengatasi nilai kosong pada kolom numerik dengan mengganti NaN dengan rata-rata kolom
        data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

        # Mengatasi nilai kosong pada kolom kategorikal dengan mengganti NaN dengan modus (nilai terbanyak)
        for col in categorical_columns:
            data[col] = data[col].fillna(data[col].mode()[0])

        # Mengkonversi kolom kategorikal menjadi numerik
        le = LabelEncoder()
        for col in categorical_columns:
            data[col] = le.fit_transform(data[col])

        # Memisahkan fitur dan target
        X = data.iloc[:, :-1]  # Semua kolom kecuali yang terakhir sebagai fitur
        y = data.iloc[:, -1]   # Kolom terakhir sebagai target

        # Normalisasi fitur
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        return data, X_scaled, y
    except Exception as e:
        print(f"Terjadi kesalahan saat preprocessing: {e}")
        sys.exit()

# Fungsi untuk menjalankan algoritma
def run_algorithm(algorithm, X_train, X_test, y_train, y_test):
    try:
        if algorithm == 'RandomForest':
            model = RandomForestClassifier()
        elif algorithm == 'SVM':
            model = SVC()
        elif algorithm == 'KNN':
            model = KNeighborsClassifier()
        else:
            print("Algoritma tidak dikenali. Gunakan 'RandomForest', 'SVM', atau 'KNN'.")
            return

        # Melatih model
        model.fit(X_train, y_train)

        # Prediksi
        y_pred = model.predict(X_test)

        # Evaluasi
        print("\nHasil evaluasi:")
        print(classification_report(y_test, y_pred))
        print(f"Akurasi: {accuracy_score(y_test, y_pred):.2f}")

        # Menyimpan model
        save_model = input("Simpan model ini? (y/n): ").lower()
        if save_model == 'y':
            filename = f"model_{algorithm}.joblib"
            joblib.dump(model, filename)
            print(f"Model disimpan sebagai {filename}.")

    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan algoritma: {e}")

# Fungsi untuk visualisasi data
def visualize_data(data):
    try:
        print("\n===== Visualisasi Data =====")
        print("1. Histogram")
        print("2. Scatter Plot")
        print("3. Heatmap Korelasi")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih jenis visualisasi: ")

        if pilihan == '1':
            data.hist(figsize=(10, 8))
            plt.show()
        elif pilihan == '2':
            print("\nKolom yang tersedia:", data.columns.tolist())  # Menampilkan kolom yang ada
            x_col = input("Masukkan nama kolom untuk sumbu x: ")
            y_col = input("Masukkan nama kolom untuk sumbu y: ")
            if x_col in data.columns and y_col in data.columns:
                sns.scatterplot(data=data, x=x_col, y=y_col)
                plt.show()
            else:
                print("Kolom tidak ditemukan. Pastikan nama kolom yang dimasukkan benar.")
        elif pilihan == '3':
            # Menghapus kolom non-numerik untuk korelasi
            numeric_data = data.select_dtypes(include=['number'])
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f", cmap="coolwarm")
            plt.show()
        elif pilihan == '4':
            return
        else:
            print("Pilihan tidak valid.")
    except Exception as e:
        print(f"Terjadi kesalahan saat visualisasi: {e}")

# Fungsi untuk menampilkan menu utama
def menu_utama():
    print("\n===== Menu Utama =====")
    print("1. Preprocessing Data")
    print("2. Visualisasi Data")
    print("3. Analisis dengan Algoritma")
    print("4. Keluar")

# Fungsi untuk menampilkan submenu analisis
def submenu_analisis():
    print("\n===== Submenu Analisis =====")
    print("1. RandomForest")
    print("2. SVM")
    print("3. KNN")
    print("4. Kembali ke Menu Utama")

# Loop utama
if __name__ == "__main__":
    while True:
        try:
            menu_utama()
            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                file_path = input("Masukkan nama file Excel (dengan path lengkap): ")
                data, X, y = preprocess_data(file_path)
                print("Preprocessing selesai.")

            elif pilihan == '2':
                if 'data' not in locals():
                    print("Harap lakukan preprocessing terlebih dahulu.")
                    continue
                visualize_data(data)

            elif pilihan == '3':
                if 'X' not in locals() or 'y' not in locals():
                    print("Harap lakukan preprocessing terlebih dahulu.")
                    continue

                submenu_analisis()
                sub_pilihan = input("Pilih algoritma: ")

                if sub_pilihan in ['1', '2', '3']:
                    algorithms = {'1': 'RandomForest', '2': 'SVM', '3': 'KNN'}
                    algorithm = algorithms[sub_pilihan]

                    # Membagi data menjadi data latih dan uji
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                    # Menjalankan algoritma pilihan user
                    run_algorithm(algorithm, X_train, X_test, y_train, y_test)

                    # Menjalankan algoritma lain untuk perbandingan
                    other_algorithms = [algo for algo in algorithms.values() if algo != algorithm]
                    for other_algorithm in other_algorithms:
                        print(f"\nMenjalankan algoritma lain untuk perbandingan: {other_algorithm}")
                        run_algorithm(other_algorithm, X_train, X_test, y_train, y_test)

                elif sub_pilihan == '4':
                    continue
                else:
                    print("Pilihan tidak valid.")

            elif pilihan == '4':
                print("Keluar dari program.")
                break

            else:
                print("Pilihan tidak valid.")
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            break
