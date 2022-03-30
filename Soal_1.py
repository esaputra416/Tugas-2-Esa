# TUGAS PEMBUATAN MENU KONTAK

# input nama dan no telepon
Nama = ["Esa", "Jeane"]
NoTelepon = ["087755085774", "081761129231"]


def daftarKontak():                            # menu 1 untuk menampilkan kontak yang tersedia
    print("Daftar Kontak:")
    for i in range(len(Nama)):
        print("Nama: {}".format(Nama[i]))
        print("No Telepon: {}".format(NoTelepon[i]))


def tambahKontak():                            # menu 2 untuk menambahkan kontak yang berisikan nama dan no telepon
    Nama.append(input("Nama: "))               # input nama
    NoTelepon.append(input("No Telepon: "))    # input no telepon
    print("Kontak berhasil ditambahkan")       # output setelah dimasukan nama dan no telepon


print("Selamat datang!")
while True:
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    menu = int(input("Pilih Menu: "))
    if menu == 1:                              # jika memilih menu 1
        daftarKontak()
    elif menu == 2:                            # jika memilih menu 2
        tambahKontak()
    elif menu == 3:                            # jika memilih menu 3
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")