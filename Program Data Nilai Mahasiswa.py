# Program Pengelolaan Nilai Mahasiswa
mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    mahasiswa[nama] = {'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
    print(f"Data mahasiswa {nama} berhasil ditambahkan.")

def ubah_data():
    nama = input("Masukkan nama mahasiswa yang akan diubah: ")
    if nama in mahasiswa:
        print(f"Data lama: {mahasiswa[nama]}")
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        mahasiswa[nama] = {'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
        print(f"Data mahasiswa {nama} berhasil diubah.")
    else:
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

def hapus_data():
    nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print(f"Data mahasiswa {nama} berhasil dihapus.")
    else:
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

def tampilkan_data():
    if mahasiswa:
        print("Daftar Nilai Mahasiswa:")
        print(f"{'Nama':<20}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Nilai Akhir':<10}")
        print("=" * 60)
        for nama, nilai in mahasiswa.items():
            print(f"{nama:<20}{nilai['Tugas']:<10}{nilai['UTS']:<10}{nilai['UAS']:<10}{nilai['Nilai Akhir']:<10.2f}")
    else:
        print("Tidak ada data mahasiswa.")

def cari_data():
    nama = input("Masukkan nama mahasiswa yang akan dicari: ")
    if nama in mahasiswa:
        print(f"Data Mahasiswa {nama}: {mahasiswa[nama]}")
    else:
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

while True:
    print("\nMenu Pilihan:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '6':
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
