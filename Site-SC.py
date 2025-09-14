import os
import time
import pyfiglet
import validators
from colorama import Fore
from tqdm import tqdm
from urllib.parse import urlparse

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
m = Fore.MAGENTA

def validate_url(url):
    if not validators.url(url):
        print(r + f"Hatalı URL: {url}")
        return False
    return True

def download_site(site):
    print(g + f"'{site}' sitesini indiriliyor...")
    try:
        for _ in tqdm(range(10), desc="İndiriliyor", colour="green"):
            time.sleep(0.2)
        os.system(f"wget -q -mk http://{site.strip()}")
        print(g + f"Klasör '{site}' olarak kaydedildi")
    except Exception as e:
        print(r + f"İndirme sırasında hata oluştu: {e}")

def main():
    os.system("clear")
    logo = pyfiglet.figlet_format("Site Script")
    print(r + "\n" + logo)
    print(b + "\n")
    
    site = input(m + "Site Adresini Girin (Çıkış için 'q'): " + r)
    
    if site.lower() == 'q':
        return
    
    if site.startswith("https://"):
        site = site.replace("https://", "")
    elif site.startswith("http://"):
        site = site.replace("http://", "")

    if validate_url("http://" + site):
        download_site(site)
    else:
        print(r + "Geçersiz adres.")

if __name__ == "__main__":
    main()