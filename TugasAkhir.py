import math

def calculate_2d_shape():
    print("\nPilih bangun datar:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    shape = input("Masukkan pilihan (1/2/3/4): ")

    if shape == '1':
        sisi = float(input("Masukkan sisi persegi: "))
        luas = sisi * sisi
        keliling = 4 * sisi
        print(f"Luas persegi: {luas}")
        print(f"Keliling persegi: {keliling}")
    elif shape == '2':
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        print(f"Luas persegi panjang: {luas}")
        print(f"Keliling persegi panjang: {keliling}")
    elif shape == '3':
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        keliling = alas + 2 * math.sqrt((alas/2)**2 + tinggi**2)
        print(f"Luas segitiga: {luas}")
        print(f"Keliling segitiga: {keliling}")
    elif shape == '4':
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = math.pi * jari_jari ** 2
        keliling = 2 * math.pi * jari_jari
        print(f"Luas lingkaran: {luas}")
        print(f"Keliling lingkaran: {keliling}")
    else:
        print("Pilihan tidak valid!")

def calculate_3d_shape():
    print("\nPilih bangun ruang:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Bola")
    print("4. Tabung")
    shape = input("Masukkan pilihan (1/2/3/4): ")

    if shape == '1':
        sisi = float(input("Masukkan sisi kubus: "))
        luas_permukaan = 6 * sisi ** 2
        volume = sisi ** 3
        print(f"Luas permukaan kubus: {luas_permukaan}")
        print(f"Volume kubus: {volume}")
    elif shape == '2':
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        volume = panjang * lebar * tinggi
        print(f"Luas permukaan balok: {luas_permukaan}")
        print(f"Volume balok: {volume}")
    elif shape == '3':
        jari_jari = float(input("Masukkan jari-jari bola: "))
        luas_permukaan = 4 * math.pi * jari_jari ** 2
        volume = (4/3) * math.pi * jari_jari ** 3
        print(f"Luas permukaan bola: {luas_permukaan}")
        print(f"Volume bola: {volume}")
    elif shape == '4':
        jari_jari = float(input("Masukkan jari-jari tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        volume = math.pi * jari_jari ** 2 * tinggi
        print(f"Luas permukaan tabung: {luas_permukaan}")
        print(f"Volume tabung: {volume}")
    else:
        print("Pilihan tidak valid!")

def main():
    print("Tugas Akhir Pemrograman Sistem")
    print("Nama : Hassanul Resky Pratama")
    print("NIM : 22030021")
    while True:
        print("\nPilih jenis bangun:")
        print("1. Bangun Datar (2D)")
        print("2. Bangun Ruang (3D)")
        print("3. Keluar")
        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            calculate_2d_shape()
        elif choice == '2':
            calculate_3d_shape()
        elif choice == '3':
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
