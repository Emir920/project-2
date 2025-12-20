import os

DOSYA = "rehber.txt"

def kisi_ekle():
    isim = input("İsim: ")
    telefon = input("Telefon: ")

    with open(DOSYA, "a", encoding="utf-8") as f:
        f.write(isim + "," + telefon + "\n")

    print("Kişi eklendi.")

def kisi_sil():
    if not os.path.exists(DOSYA):
        print("Rehber boş.")
        return

    isim = input("Silinecek isim: ")
    yeni_liste = []

    with open(DOSYA, "r", encoding="utf-8") as f:
        for satir in f:
            if not satir.startswith(isim + ","):
                yeni_liste.append(satir)

    with open(DOSYA, "w", encoding="utf-8") as f:
        f.writelines(yeni_liste)

    print("Kişi silindi (varsa).")

def rehberi_listele():
    if not os.path.exists(DOSYA):
        print("Rehber boş.")
        return

    with open(DOSYA, "r", encoding="utf-8") as f:
        print("\n--- REHBER ---")
        for satir in f:
            isim, telefon = satir.strip().split(",")
            print(isim, ":", telefon)

def menu():
    print("""
1 - Kişi Ekle
2 - Kişi Sil
3 - Rehberi Listele
4 - Çıkış
""")

while True:
    menu()
    secim = input("Seçim: ")

    if secim == "1":
        kisi_ekle()
    elif secim == "2":
        kisi_sil()
    elif secim == "3":
        rehberi_listele()
    elif secim == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Hatalı seçim!")
