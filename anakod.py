import os

# ----- KİŞİ REHBERİ -----
DOSYA = "reehbr.txt"

def oku(dosya=DOSYA):
    if not os.path.exists(dosya):
        return []
    with open(dosya, "r", encoding="utf-8") as f:
        return f.readlines()

def yaz(liste, dosya=DOSYA):
    with open(dosya, "w", encoding="utf-8") as f:
        f.writelines(liste)

def kisi_ekle():
    isim = input("İsim: ")
    tel = input("Telefon: ")
    with open(DOSYA, "a", encoding="utf-8") as f:
        f.write(f"{isim},{tel}\n")
    print("Kişi eklendi.")

def kisi_sil():
    isim = input("Silinecek isim: ")
    liste = oku()
    yeni = [s for s in liste if not s.startswith(isim + ",")]
    yaz(yeni)
    print("İşlem tamamlandı.")

def kisi_duzelt():
    isim = input("Düzeltilecek isim: ")
    liste = oku()
    yeni = []

    for s in liste:
        ad, tel = s.strip().split(",")
        if ad == isim:
            ad = input("Yeni isim (boş=aynı): ") or ad
            tel = input("Yeni tel (boş=aynı): ") or tel
            yeni.append(f"{ad},{tel}\n")
        else:
            yeni.append(s)

    yaz(yeni)
    print("İşlem tamamlandı.")

def rehberi_listele():
    liste = oku()
    if not liste:
        print("Rehber boş.")
    for s in liste:
        ad, tel = s.strip().split(",")
        print(ad, ":", tel)

# ----- POKEMON EKLEYİCİ -----
POKEMON_DOSYA = "pokemon.txt"

def pokemon_ekle():
    isim = input("Pokemon adı: ")
    tur = input("Türü: ")
    seviye = input("Seviye: ")
    with open(POKEMON_DOSYA, "a", encoding="utf-8") as f:
        f.write(f"{isim},{tur},{seviye}\n")
    print("Pokemon eklendi.")

def pokemon_sil():
    isim = input("Silinecek Pokemon adı: ")
    liste = oku(POKEMON_DOSYA)
    yeni = [s for s in liste if not s.startswith(isim + ",")]
    yaz(yeni, POKEMON_DOSYA)
    print("İşlem tamamlandı.")

def pokemon_duzelt():
    isim = input("Düzeltilecek Pokemon adı: ")
    liste = oku(POKEMON_DOSYA)
    yeni = []

    for s in liste:
        ad, tur, seviye = s.strip().split(",")
        if ad == isim:
            ad = input("Yeni isim (boş=aynı): ") or ad
            tur = input("Yeni tür (boş=aynı): ") or tur
            seviye = input("Yeni seviye (boş=aynı): ") or seviye
            yeni.append(f"{ad},{tur},{seviye}\n")
        else:
            yeni.append(s)

    yaz(yeni, POKEMON_DOSYA)
    print("İşlem tamamlandı.")

def pokemon_listele():
    liste = oku(POKEMON_DOSYA)
    if not liste:
        print("Hiç Pokemon yok.")
    for s in liste:
        ad, tur, seviye = s.strip().split(",")
        print(f"{ad} | Tür: {tur} | Seviye: {seviye}")

# ----- ANA MENÜ -----
while True:
    print("""
╔═════════════════════╗
║ 1- Kişi Ekle        ║
║ 2- Kişi Sil         ║
║ 3- Kişi Listele     ║
║ 4- Kişi Düzelt      ║
║ 5- Pokemon Ekle     ║
║ 6- Pokemon Sil      ║
║ 7- Pokemon Listele  ║
║ 8- Pokemon Düzelt   ║
║ 9- Çıkış            ║
╚═════════════════════╝
""")
    secim = input("Seçim: ")

    if secim == "1":
        kisi_ekle()
    elif secim == "2":
        kisi_sil()
    elif secim == "3":
        rehberi_listele()
    elif secim == "4":
        kisi_duzelt()
    elif secim == "5":
        pokemon_ekle()
    elif secim == "6":
        pokemon_sil()
    elif secim == "7":
        pokemon_listele()
    elif secim == "8":
        pokemon_duzelt()
    else:
        break

