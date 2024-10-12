import pyzipper
import os
import sys
import time
import socket
import requests
from datetime import datetime
from termcolor import colored


def loading_animation():
    animation = "|/-\\"
    for i in range(50):  # Jumlah iterasi
        time.sleep(0.1)  # Simulasi waktu proses
        sys.stdout.write(f"\rLoading {animation[i % len(animation)]}")
        sys.stdout.flush()


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        return response.text
    except requests.RequestException:
        return "Tidak dapat mengambil IP publik, pastikan Anda memiliki koneksi internet."


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")  # Format jam:menit:detik


def extract_zip(zip_file, wordlist_file):
    try:
        with open(wordlist_file, 'rb') as wordlist:
            for word in wordlist:
                password = word.strip()
                try:
                    with pyzipper.AESZipFile(zip_file, 'r') as zf:
                        zf.extractall(pwd=password)
                        print(f"[SUCCESS] Password ditemukan: {password.decode('utf-8')}")
                        return True
                except (RuntimeError, pyzipper.BadZipFile, pyzipper.LargeZipFile):
                    pass
                except Exception as e:
                    print(f"Error: {e} - Password yang dicoba: {password.decode('utf-8')}")
    except FileNotFoundError:
        print("[ERROR] File ZIP atau wordlist tidak ditemukan.")
    except pyzipper.BadZipFile:
        print("[ERROR] File ZIP rusak atau tidak valid.")
    print("[FAILED] Tidak ada password yang cocok.")
    return False


# Tampilan
os.system('clear')
loading_animation()
print("\nLoading complete!")
time.sleep(3)
os.system('clear')

# Banner
banner = '''██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
                                          
                                          
                                          
CREATED BY : ANDRAX404 メ GALIRUS OFFICIAL 
Copyright ©️ by : Andrax メ LuzyXploit
                                          
                                          
                                          
██╗   ██╗██╗██████╗                       
██║   ██║██║██╔══██╗                      
██║   ██║██║██████╔╝                      
╚██╗ ██╔╝██║██╔═══╝                       
 ╚████╔╝ ██║██║                           
  ╚═══╝  ╚═╝╚═╝                           
'''

colors = ['red']
for i, line in enumerate(banner.splitlines()):
    print(colored(line, colors[i % len(colors)]))

# Informasi
print(colored("(•)", 'cyan'), colored(' author           : ANDRAX 404 メ Galirus Official', 'green'))
print(colored("(•)", 'cyan'), colored(' tanggal Create   : minggu/6/10/2024', 'green'))
print(colored("(•)", 'cyan'), colored(f' waktu hari ini   : {get_time()}', 'green'))
print(colored("(•)", 'cyan'), colored(f' IP lu nyet       : {get_public_ip()}', 'green'))
print(colored("(•)", 'cyan'), colored(' doakan semoga bisa berkembang dan sehat selalu pengembang sc', 'green'))

# Input
zip_file = input("Masukkan lokasi file ZIP (contoh: /sdcard/Download/file.zip): ")
wordlist_file = input("Masukkan lokasi wordlist (contoh: /sdcard/Download/wordlist.txt): ")

# Memanggil fungsi brute force
extract_zip(zip_file, wordlist_file)