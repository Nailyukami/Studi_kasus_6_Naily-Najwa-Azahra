import json

while True:
    print("1. Lihat barang")
    print("2. Tambah barang")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        with open("Data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        print()
        for barang in data:
            print(barang["nama"], "- stok:", barang["stok"], "- harga:", barang["harga"])

    elif pilih == "2":
        with open("Data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        nama = input("Nama barang: ")
        stok = int(input("Stok: "))
        harga = int(input("Harga: "))

        barang_baru = {"nama": nama, "stok": stok, "harga": harga}
        data.append(barang_baru)

        with open("Data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("Barang berhasil ditambahkan!")

    elif pilih == "3":
        print("Selesai")
        break

    else:
        print("Menu tidak ada")