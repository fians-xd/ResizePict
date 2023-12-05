import os
import time
import sys
from PIL import Image

# Warna
h  = ('\x1b[0;32m') # hijau gelap
ht = ('\x1b[32;1m') # hijau terang
b  = ('\x1b[0;36m') # biru gelap
bt = ('\x1b[36;1m') # biru terang
m  = ('\x1b[31;1m') # merah
p  = ('\x1b[37;1m') # putih
h  = ('\x1b[30;1m') # hitam
k  = ('\x1b[33;1m') # oren
kt = ('\x1b[1;33m') # kuning terang

b  = ('\x1b[0;34m') # biru tua
u  = ('\x1b[0;35m') # ungu
n  = ('\x1b[0;0m') # normal

# Logo
speed = 0.0005
___logo___ = (f"""
{k} _______                       __                                  _______   __
{k}/       \                     /  |                                /       \ /  |
{u}$$$$$$$  {k}|  ______    _______ {u}$${k}/  ________   ______              {u}$$$$$$$  {k}|{u}$${k}/   _______
{u}$$ {k}|__{u}$$ {k}| /      \  /       |/  |/        | /      \    ______   {u}$$ {k}|__{u}$$ {k}|/  | /       |
{u}$$    {u}$${k}< /{u}$$$$$$  {k}|/{u}$$$$$$${k}/ {u}$$ {k}|{u}$$$$$$$${k}/ /{u}$$$$$$  {k}|  /      |  {u}$$    $${k}/ {u}$$ {k}|/{u}$$$$$$${k}/
{u}$$$$$$$  {k}|{u}$$    $$ {k}|{u}$$      {k}\ {u}$$ {k}|  /  {u}$${k}/  {u}$$    $$ {k}|  {u}$$$$$${k}/   {u}$$$$$$${k}/  {u}$$ {k}|{u}$$ {k}|
{u}$$ {k}|  {u}$$ {k}|{u}$$$$$$$${k}/  {u}$$$$$$  {k}|{u}$$ {k}| /{u}$$$${k}/__ {u}$$$$$$$${k}/             {u}$$ {k}|      {u}$$ {k}|{u}$$ {k}\_____
{u}$$ {k}|  {u}$$ {k}|{u}$$       {k}|/     {u}$${k}/ {u}$$ {k}|/{u}$$      {k}|{u}$$       {k}|            {u}$$ {k}|      {u}$$ {k}|{u}$$       {k}|
{u}$${k}/   {u}$${k}/  {u}$$$$$$${k}/ {u}$$$$$$${k}/  {u}$${k}/ {u}$$$$$$$${k}/  {u}$$$$$$${k}/             {u}$${k}/       {u}$${k}/  {u}$$$$$$${k}/{n}
     {h};                                                                          ;
 {h}('>-'                                                                          '-<')
{h}//-\ㄏ                   {k}↤↤↤↤↤{ht}   𝓪𝕌тн 𝐘𝓐ᶰ-𝓧ᵈ {k}  ↦↦↦↦↦{h}                            ㄟ/-\＼
{h}(\_/)                                                                            (\_/)
 {h}~ ~{b}▂▃▅▆▓▒░{k}(っ◔◡◔)っ{m}♥ {ht}𝓈𝒸𝓇𝒾𝓅𝓉 𝓊𝓃𝓉𝓊𝓀 𝓂𝑒𝓃𝑔𝓊𝒷𝒶𝒽 𝓊𝓀𝓊𝓇𝒶𝓃 𝒻♡𝓉♡          {m}♥{k}ԅ(≖‿≖ԅ) {b}░▒▓▆▅▃▂▁{h}~ ~{n}
""")

# Teks Berjalan
def berjalan_teks(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

# Fungsi untuk meresize gambar
def resize_image(image_path, width, height, output_folder, output_filename):
    try:
        # Buka gambar
        image = Image.open(image_path)
        
        # Resize gambar dengan menjaga proporsi aspek
        image = image.resize((width, height), Image.ANTIALIAS)
        
        # Path untuk menyimpan gambar hasil
        output_path = os.path.join(output_folder, output_filename)
        
        # Simpan gambar dengan kualitas yang baik
        image.save(output_path, "JPEG", quality=96)
        
        print(f"{h}\nGambar berhasil diresize dan disimpan sebagai '{output_filename}' di folder '{output_folder}'")
    except IOError:
        print(f"{m}\nGagal membuka atau menyimpan gambar.!!")

# Fungsi untuk mengonversi satuan pengukuran menjadi piksel
def convert_to_pixels(measurement, unit):
    if unit == "pixel":
        return int(measurement)
    elif unit == "centimeter":
        return int(measurement * 37.795275591)  # 1 cm = 37.795275591 piksel
    elif unit == "milimeter":
        return int(measurement * 3.7795275591)  # 1 mm = 3.7795275591 piksel
    else:
        return None

# Input gambar
os.system('clear')
berjalan_teks(___logo___)
image_path = input(f"{ht}\nMasukkan path gambar{k}:{n} ")

# Pilihan satuan pengukuran
unit_options = ["pixel", "centimeter", "milimeter"]

# Tampilkan pilihan satuan pengukuran
print(f"{ht}\nPilih satuan pengukuran.!")
for i, option in enumerate(unit_options, start=1):
    print(f"{k}{i}{m}. {ht}{option}")

# Input pilihan satuan pengukuran
unit_choice = input(f"{ht}\nMasukkan pilihan satuan pengukuran{k}:{n} ")

# Validasi pilihan satuan pengukuran
if unit_choice.isdigit() and 1 <= int(unit_choice) <= len(unit_options):
    unit = unit_options[int(unit_choice) - 1]

    # Input ukuran tinggi dan lebar
    width = float((input(f"{ht}\nMasukkan lebar gambar{k}:{n} ")))
    height = float((input(f"{ht}Masukkan tinggi gambar{k}:{n} ")))

    # Input nama file hasil
    output_filename = input(f"{ht}\nMasukkan nama file hasil{k}:{n} ")

    # Input folder untuk menyimpan hasil
    output_folder = "hasil"

    # Membuat folder jika belum ada
    os.makedirs(output_folder, exist_ok=True)

    # Konversi ukuran tinggi dan lebar ke piksel jika diperlukan
    width_in_pixels = convert_to_pixels(width, unit)
    height_in_pixels = convert_to_pixels(height, unit)

    # Jika konversi gagal, tampilkan pesan kesalahan
    if width_in_pixels is None or height_in_pixels is None:
        print(f"{u}\nSatuan pengukuran tidak valid.!!")
    else:
        # Panggil fungsi resize_image
        resize_image(image_path, width_in_pixels, height_in_pixels, output_folder, output_filename)
else:
    print(f"{m}\nPilihan satuan pengukuran tidak valid.!!")
