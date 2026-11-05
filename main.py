# analisis dan klasifikasi data
# 20 data nilai
data_nilai = [42, 55, 61, 68,73, 
             79, 82, 87, 91, 64, 
             58, 76, 84, 49, 95, 
             20, 59, 60, 80, 100]

# menghitung rata-rata
def rata_rata(data):
    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)    

# menentukan status nilai
def status_nilai(nilai):
    if nilai < 60:
        return "RENDAH"
    elif nilai < 80:
        return "SEDANG"
    else:
        return "TINGGI"

# menghitung jumlah kategori
def hitung_kategori(data):
    rendah = 0
    sedang = 0
    tinggi = 0
    for nilai in data:
        status = status_nilai(nilai)
        if status == "RENDAH":
            rendah += 1
        elif status == "SEDANG":
            sedang += 1
        else:
            tinggi += 1
    return rendah, sedang, tinggi

# menampilkan hasil klasifikasi
print("--- PROGRAM ANALISIS NILAI ---")

for i in range(len(data_nilai)):
    nilai = data_nilai[i]
    status = status_nilai(nilai)
    print(i+1, ".", nilai, "->", status)

# menghitung hasil analisis
rendah, sedang, tinggi = hitung_kategori(data_nilai)
average = rata_rata(data_nilai)

#  menampilkan ringkasan
print()
print("=== RINGKASAN DATA ===")
print("Total Data:", len(data_nilai))
print("RENDAH:", rendah)
print("SEDANG:", sedang)
print("TINGGI:", tinggi)
print("Rata-Rata Nilai:", round(average, 2))
print("Minimum:", min(data_nilai))
print("Maksimum:", max(data_nilai))
