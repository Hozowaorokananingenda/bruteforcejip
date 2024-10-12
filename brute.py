import itertools
import string
import pyzipper
from Crypto.Hash import SHA256
import pyzipper
import os
import sys
from termcolor import colored
import time
import socket
from datetime import datetime
import socket
from datetime import datetime
from termcolor import colored

os.system('clear')

# Meminta input nama dari pengguna
nama = input("Masukkan nama Anda: ")


def loading_animation():
    animation = "|/-\\"
    for i in range(50):  # Jumlah iterasi
        time.sleep(0.1)  # Simulasi waktu proses
        sys.stdout.write(f"\rLoading {animation[i % len(animation)]}")
        sys.stdout.flush()

loading_animation()
print("\nLoading complete!")

time.sleep(3)
os.system('clear')
print(f" (•) YAEMIKO CHAN :  🥰{nama}🥰 YOKOSOSENSEI!!!.")
time.sleep(3)

print("")
print("")

print(f" (•) YAEMIKO CHAN :  🥰{nama}🥰 今日はいいですか??")
time.sleep(3)

print("")
print("")

kabar = input("Kabar mu brek?🗿:  ")

print("")
print("")

print(f" (•) {nama} :  {kabar} Yaemiko sayang 😄")
time.sleep(3)

print("")
print("")

print(f" (•) YAEMIKO : baiklah {nama}! Selamat Memakai Tools crack zip by andrax & ofga 😄.")
time.sleep(5)

print("")
print("")

print(f" (•) {nama} :  Baiklah Yaemiko Sayang 🥰.")
time.sleep(3)
print("")

    








#BAGIAN MESIN UNTUK BANNER !!!

os.system('clear')

banner = '''
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*    COPYRIGHT BY
      ^$$$B  $$$$/     $$$$$$$$$$$$   d$$R"   © OFGA  メ ANDRAX404
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""


'''
colors = ['red', 'white']

# Print each line of the banner in a different color
for i, line in enumerate(banner.splitlines()):
    print(colored(line, colors[i % len(colors)]))
    











#BAGIAN MESIN UNTUK AUTHOR ANIJG

import requests  # Mengimpor modul requests untuk mendapatkan IP publik
from datetime import datetime  # Mengimpor datetime untuk mendapatkan waktu
from termcolor import colored  # Mengimpor colored untuk mencetak teks berwarna

def get_public_ip():
    # Mendapatkan alamat IP publik
    response = requests.get('https://api.ipify.org')
    public_ip = response.text
    return public_ip

# Mendapatkan waktu real-time
def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")  # Format jam:menit:detik

if __name__ == "__main__":
    # Output
    print(colored("(•)", 'cyan'), colored(' author           : ANDRAX 404 メ Ofga ', 'green'))
    print(colored("(•)", 'cyan'), colored(' tanggal Create   : minggu/6/10/2024', 'green'))
    print(colored("(•)", 'cyan'), colored(f' waktu hari ini   : {get_time()}', 'green'))  # Waktu real-time
    print(colored("(•)", 'cyan'), colored(f' IP lu nyet       : {get_public_ip()}', 'green'))  # IP publik
    print(colored("(•)", 'cyan'), colored(' doakan semoga bisa berkembang dan sehat selalu pengembang sc', 'green'))
    

time.sleep(5)











#MESIN EKSEKUSI UNTUK BRUTE FORCE BY ANDRAX404 メ OFGA DDOS

def brute_force_zip(zip_file_path, max_length=4):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789@#$&_-+*~•©®"  # Karakter yang digunakan
    try:
        with pyzipper.AESZipFile(zip_file_path, 'r') as zf:
            for length in range(1, max_length + 1):
                for attempt in itertools.product(characters, repeat=length):
                    password = ''.join(attempt)
                    try:
                        zf.pwd = password.encode('utf-8')
                        zf.testzip()  # Memeriksa password
                        print(f'[+] EZZ PW DEK 🚮☠️ = {password}')
                        return password
                    except (RuntimeError, pyzipper.BadZipFile):
                        print(f'[-] Password salah🤬😡: {password}')
    except FileNotFoundError:
        print(f'[-] File tidak ditemukan😕: {zip_file_path}')
    except Exception as e:
        print(f'[-] YANG BENER MASUKIN NYA😭: {str(e)}')

    print('[-] Password tidak ditemukan')

print("")
print("")

# Meminta pengguna untuk memasukkan jalur file ZIP
zip_file = input("MASUKKAN DIREKTORI FILE UNTUK DI CRACK 🚮  =   ")  
brute_force_zip(zip_file, max_length=4)