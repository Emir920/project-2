import os

DOSYA = "rehber.txt"

def oku():
    if not os.path.exists(DOSYA):
        return []
    with open(DOSYA, "r", encoding="utf-8") as f:
        return f.readlines()

def yaz(liste):
    with open(DOSYA, "w", encoding="utf-8") as f:
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
    for s in oku():
        ad, tel = s.strip().split(",")
        print(ad, ":", tel)

while True:
    print("""
1-Ekle
2-Sil
3-Listele
4-Düzelt
5-Çıkış
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
        break
    else:
        print("Hatalı seçim")
