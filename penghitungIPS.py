def hitung_ips():
    jumlah = int(input("Jumlah mata kuliah: "))
    total = 0

    for i in range(jumlah):
        nilai = input("Nilai (A/B/C/D): ").upper()

        if nilai == "A":
            total += 4
        elif nilai == "B":
            total += 3
        elif nilai == "C":
            total += 2
        elif nilai == "D":
            total += 1

    ips = total / jumlah
    print("IPS:", round(ips,2))

hitung_ips()
