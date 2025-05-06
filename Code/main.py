import json
import queue

# Load konfigurasi saat runtime
with open("config.json") as f:
    CONFIG = json.load(f)

# Antrian berdasarkan tingkat kerusakan
queues = {
    "ringan": queue.Queue(),
    "sedang": queue.Queue(),
    "berat": queue.Queue()
}

def tambah_antrian():
    nama = input("Masukkan nama pelanggan: ")
    kerusakan = input("Tingkat kerusakan (ringan/sedang/berat): ").lower()
    if kerusakan in queues:
        queues[kerusakan].put(nama)
        print(f"{nama} ditambahkan ke antrian {kerusakan}.")
    else:
        print("Jenis kerusakan tidak dikenal.")

def proses_antrian():
    for level in CONFIG["priority_order"]:
        if not queues[level].empty():
            nama = queues[level].get()
            waktu = CONFIG["service_times"][level]
            print(f"Memproses {nama} dengan kerusakan {level} (estimasi {waktu} menit)")
            return
    print("Tidak ada antrian.")

def tampilkan_antrian():
    for level in CONFIG["priority_order"]:
        print(f"Antrian {level}: {[queues[level].queue[i] for i in range(queues[level].qsize())]}")

# Table-driven construction: mapping input ke fungsi
actions = {
    "1": tambah_antrian,
    "2": proses_antrian,
    "3": tampilkan_antrian,
    "4": lambda: exit()
}

def main():
    while True:
        print("\n--- Menu Antrian Bengkel ---")
        print("1. Tambah Antrian")
        print("2. Proses Antrian")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        action = actions.get(pilihan)
        if action:
            action()
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()