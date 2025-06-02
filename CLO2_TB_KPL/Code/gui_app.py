import os
import tkinter as tk
from tkinter import ttk, messagebox
import json
from service import BengkelAntrian
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np

# Suppress macOS warnings
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Load config with secure fallback
try:
    with open("config.json") as f:
        CONFIG = json.load(f)
except Exception as e:
    messagebox.showerror("Error", f"Gagal membaca config.json: {e}")
    exit(1)

# Init logic
antrian = BengkelAntrian(CONFIG)

class AntrianBengkelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Antrian Bengkel")
        self.root.geometry("600x600")
        self.root.configure(bg="#e6f0ff")  # Light blue background
        self.style = ttk.Style()
        self.configure_styles()
        self.create_main_menu()

    def configure_styles(self):
        # Blue gradient theme
        self.style.theme_use('clam')
        
        # Configure button style
        self.style.configure('Blue.TButton', 
                            font=('Arial', 11, 'bold'),
                            foreground='white',
                            background='#2c7da0',
                            borderwidth=1,
                            relief='raised',
                            padding=10)
        self.style.map('Blue.TButton', 
                      background=[('active', '#1a5276'), ('pressed', '#154360')])
        
        # Configure header style
        self.style.configure('Header.TFrame', background='#1a5276')
        self.style.configure('Header.TLabel', 
                            background='#1a5276', 
                            foreground='white',
                            font=('Arial', 16, 'bold'))
        
        # Configure form style
        self.style.configure('Form.TFrame', background='#d6eaf8')
        self.style.configure('Form.TLabel', 
                            background='#d6eaf8', 
                            foreground='#154360',
                            font=('Arial', 10, 'bold'))
        
        # Configure text area style
        self.style.configure('Display.TFrame', background='#e6f0ff')
        self.style.configure('Display.TText', 
                            background='white', 
                            foreground='#154360',
                            font=('Arial', 10))

    def create_main_menu(self):
        self.clear_window()
        
        # Main container with gradient
        main_frame = tk.Frame(self.root, bg="#e6f0ff")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header with gradient effect
        header_frame = ttk.Frame(main_frame, style='Header.TFrame')
        header_frame.pack(fill="x", pady=(0, 20))
        ttk.Label(header_frame, text="📋 Menu Antrian Bengkel", 
                 style='Header.TLabel', padding=10).pack()
        
        # Title with blue gradient effect
        title_label = tk.Label(header_frame, text="Bengkel Maju Jaya", 
                              font=("Arial", 12, "bold"), 
                              fg="white", bg="#1a5276")
        title_label.pack(pady=(0, 10))
        
        # Button container
        btn_frame = tk.Frame(main_frame, bg="#e6f0ff")
        btn_frame.pack(pady=20)
        
        buttons = [
            ("➕ Tambah Antrian", self.show_tambah_antrian),
            ("🔧 Proses Antrian", self.proses_antrian),
            ("📊 Statistik Antrian", self.tampilkan_statistik),
            ("📄 Tampilkan Antrian", self.tampilkan_antrian),
            ("❌ Keluar", self.root.quit)
        ]
        
        for text, cmd in buttons:
            btn = ttk.Button(btn_frame, text=text, command=cmd, style='Blue.TButton')
            btn.pack(pady=10, ipadx=20, fill='x')
            
        # Footer
        footer_frame = tk.Frame(main_frame, bg="#1a5276", height=30)
        footer_frame.pack(side="bottom", fill="x", pady=(20, 0))
        tk.Label(footer_frame, text="©️ 2025 Bengkel Maju Jaya", 
                font=("Arial", 8), 
                bg="#1a5276", fg="white").pack(pady=5)

    def show_tambah_antrian(self):
        self.clear_window()
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#e6f0ff")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame, style='Header.TFrame')
        header_frame.pack(fill="x", pady=(0, 20))
        ttk.Label(header_frame, text="📝 Tambah Antrian", 
                 style='Header.TLabel', padding=10).pack()
        
        # Form container
        form_frame = ttk.Frame(main_frame, style='Form.TFrame')
        form_frame.pack(pady=10, padx=20, fill="x")
        
        # Form title
        tk.Label(form_frame, text="Formulir Pendaftaran Antrian", 
                font=("Arial", 12, "bold"), 
                bg="#d6eaf8", fg="#154360").grid(row=0, column=0, columnspan=2, pady=10)
        
        # Nama input
        ttk.Label(form_frame, text="Nama Pelanggan:", style='Form.TLabel').grid(row=1, column=0, sticky="w", pady=5, padx=10)
        nama_entry = ttk.Entry(form_frame, width=30, font=("Arial", 10))
        nama_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=10)
        
        # Kerusakan dropdown
        ttk.Label(form_frame, text="Tingkat Kerusakan:", style='Form.TLabel').grid(row=2, column=0, sticky="w", pady=5, padx=10)
        kerusakan_cb = ttk.Combobox(form_frame, values=["Ringan", "Sedang", "Berat"], state="readonly", font=("Arial", 10))
        kerusakan_cb.grid(row=2, column=1, sticky="ew", pady=5, padx=10)
        kerusakan_cb.current(0)
        
        # Button container
        btn_frame = tk.Frame(main_frame, bg="#e6f0ff")
        btn_frame.pack(pady=20)
        
        def submit():
            nama = nama_entry.get()
            kerusakan = kerusakan_cb.get().lower()
            if not nama:
                messagebox.showwarning("Peringatan", "Nama pelanggan harus diisi!")
                return
                
            hasil = antrian.tambah_antrian(nama, kerusakan)
            messagebox.showinfo("Info", hasil)
            if "ditambahkan" in hasil:
                self.create_main_menu()

        ttk.Button(btn_frame, text="✔ Simpan", command=submit, style='Blue.TButton').pack(side="left", padx=5)
        ttk.Button(btn_frame, text="⬅ Kembali", command=self.create_main_menu, style='Blue.TButton').pack(side="left", padx=5)

    def proses_antrian(self):
        try:
            hasil = antrian.proses_antrian()
            messagebox.showinfo("Antrian Diproses", hasil)
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def tampilkan_statistik(self):
        data = antrian.tampilkan_antrian()
        counts = {level: len(data.get(level, [])) for level in CONFIG["priority_order"]}
        
        # Create pie chart
        fig, ax = plt.subplots(figsize=(6, 4))
        colors = ['#3498db', '#2ecc71', '#e74c3c']
        ax.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%', 
               colors=colors, startangle=90, shadow=True)
        ax.set_title('Distribusi Tingkat Kerusakan')
        ax.axis('equal')
        
        # Save to temp file
        plt.savefig('temp_stats.png', dpi=100)
        plt.close()
        
        self.show_statistics_window()

    def show_statistics_window(self):
        self.clear_window()
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#e6f0ff")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame, style='Header.TFrame')
        header_frame.pack(fill="x", pady=(0, 20))
        ttk.Label(header_frame, text="📊 Statistik Antrian", 
                 style='Header.TLabel', padding=10).pack()
        
        # Load and display statistics image
        img = Image.open('temp_stats.png')
        photo = ImageTk.PhotoImage(img)
        
        img_label = tk.Label(main_frame, image=photo, bg="#e6f0ff")
        img_label.image = photo
        img_label.pack(pady=10)
        
        # Back button
        btn_frame = tk.Frame(main_frame, bg="#e6f0ff")
        btn_frame.pack(pady=20)
        ttk.Button(btn_frame, text="⬅ Kembali", command=self.create_main_menu, style='Blue.TButton').pack()

    def tampilkan_antrian(self):
        self.clear_window()
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#e6f0ff")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame, style='Header.TFrame')
        header_frame.pack(fill="x", pady=(0, 20))
        ttk.Label(header_frame, text="📄 Daftar Antrian", 
                 style='Header.TLabel', padding=10).pack()
        
        # Display frame
        display_frame = ttk.Frame(main_frame, style='Display.TFrame')
        display_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Title
        tk.Label(display_frame, text="ANTRIAN SAAT INI", 
                font=("Arial", 12, "bold"), 
                bg="#e6f0ff", fg="#154360").pack(pady=(5, 10))
        
        # Text area with scrollbar
        scrollbar = tk.Scrollbar(display_frame)
        scrollbar.pack(side="right", fill="y")
        
        text_area = tk.Text(display_frame, height=15, width=60, 
                          yscrollcommand=scrollbar.set,
                          bg="white", fg="#154360", 
                          font=("Arial", 10), relief="sunken")
        text_area.pack(fill="both", expand=True, padx=10, pady=5)
        scrollbar.config(command=text_area.yview)
        
        # Add content
        data = antrian.tampilkan_antrian()
        
        for level in CONFIG["priority_order"]:
            antrians = data.get(level, [])
            text_area.insert("end", f"--- {level.upper()} ---\n", "heading")
            
            if not antrians:
                text_area.insert("end", "  (Kosong)\n\n")
            else:
                for idx, nama in enumerate(antrians, 1):
                    text_area.insert("end", f"  {idx}. {nama}\n")
                text_area.insert("end", "\n")
        
        text_area.tag_configure("heading", 
                               font=("Arial", 10, "bold"), 
                               foreground="#2980b9")
        text_area.config(state="disabled")
        
        # Back button
        btn_frame = tk.Frame(main_frame, bg="#e6f0ff")
        btn_frame.pack(pady=20)
        ttk.Button(btn_frame, text="⬅ Kembali", command=self.create_main_menu, style='Blue.TButton').pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AntrianBengkelApp(root)
    root.mainloop()