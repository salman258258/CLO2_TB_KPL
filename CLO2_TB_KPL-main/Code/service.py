import queue

class BengkelAntrian:
    def __init__(self, config):
        self.config = config
        self.queues = {
            "ringan": queue.Queue(),
            "sedang": queue.Queue(),
            "berat": queue.Queue()
        }

    def tambah_antrian(self, nama, kerusakan):
        if kerusakan in self.queues:
            self.queues[kerusakan].put(nama)
            return f"{nama} ditambahkan ke antrian {kerusakan}."
        return "Jenis kerusakan tidak dikenal."

    def proses_antrian(self):
        for level in self.config["priority_order"]:
            if not self.queues[level].empty():
                nama = self.queues[level].get()
                waktu = self.config["service_times"][level]
                return f"Memproses {nama} dengan kerusakan {level} (estimasi {waktu} menit)"
        return "Tidak ada antrian."

    def tampilkan_antrian(self):
        return {
            level: list(self.queues[level].queue)
            for level in self.config["priority_order"]
        }