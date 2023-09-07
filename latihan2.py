#Latihan ITC 7 September 2023
#Input Nilai Mahasiswa
jumlah_data = int(input("Masukkan jumlah mahasiswa : "))

for i in range(jumlah_data):
    nilai = int(input(f"Masukkan nilai mahasiswa ke-{i + 1}: "))

    if nilai >= 90:
        print("Nilai anda sangat baik (A).")
    elif nilai >= 80:
        print("Nilai anda baik (B).")
    elif nilai >= 70:
        print("Nilai anda cukup (C).")
    else:
        print("Belajar perlu belajar lebih keras (D).")