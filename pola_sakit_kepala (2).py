def pola_sakit_kepala(panjang, lebar):
    panjang = abs(panjang)
    lebar = abs(lebar)

    if panjang != lebar:
        print("panjnag dan lebar sama tak boleh beda")
        return
    if panjang % 2 == 0:
        print("panjang dan lebar harus -")
        return
    bingung = panjang // 2

    for b in range(panjang):
        for a in range(lebar):
            num = (abs(b - bingung ) - (a - bingung))
        if a == lebar - 1:
            print(num, end="")
print("no 1. (pola 7,7)")
pola_sakit_kepala(7, 7)
print()
print("no 2. (Pola 4, 4)")
pola_sakit_kepala(4, 4)
print()
print("no 3. (Pola -15, 15)")
pola_sakit_kepala(-15, 15)