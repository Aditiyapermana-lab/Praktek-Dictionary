import os
import datetime
#mebuat data mahasiswa dengan dictionary

mahasiswa_template = {
    "nama": "",
    "nim": "00000000",
    "jurusan": "",
    "semester": 0,
    "ipk": 0.0,
    "lahir": datetime.datetime.now().strftime("%d-%m-%Y")
}
data_mahasiswa = {}
while True:
    os.system("cls")
    print(f'{"SELAMAT DATANG DI PROGRAM DATA MAHASISWA":^60}')
    print("=" * 60)
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["nama"] = input("Masukkan nama mahasiswa: ")
    mahasiswa["nim"] = input("Masukkan NIM mahasiswa: ")
    mahasiswa["jurusan"] = input("Masukkan jurusan mahasiswa: ")
    mahasiswa["semester"] = int(input("Masukkan semester mahasiswa: "))
    mahasiswa["ipk"] = float(input("Masukkan IPK mahasiswa: "))
    TAHUN_LAHIR = int(input("Masukkan tahun lahir mahasiswa: "))
    BULAN_LAHIR = int(input("Masukkan bulan lahir mahasiswa: "))
    TANGGAL_LAHIR = int(input("Masukkan tanggal lahir mahasiswa: "))
    mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR).strftime("%d-%m-%Y")
    data_mahasiswa.update({mahasiswa["nama"]: mahasiswa})
    print(f"\n{'NAMA':<20} {'NIM':<15} {'JURUSAN':<15} {'SEMESTER':<10} {'IPK':<10} {'LAHIR':<15}")

    for KEY in data_mahasiswa:

        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        JURUSAN = data_mahasiswa[KEY]["jurusan"]
        SEMESTER = data_mahasiswa[KEY]["semester"]
        IPK = data_mahasiswa[KEY]["ipk"]
        LAHIR = data_mahasiswa[KEY]["lahir"]

        print(f"{NAMA:<20} {NIM:<15} {JURUSAN:<15} {SEMESTER:<10} {IPK:<10.2f} {LAHIR:<15}")

    Input = input("Apakah ingin menambahkan data mahasiswa lagi? (y/n): ")
    if Input.lower() != 'y':
        break
print("\nTerima kasih telah menggunakan program ini.")