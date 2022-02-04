def persegi():
    sisi=int(input("masukan sisi : "))
    luas = sisi*sisi
    print ("jadi luas persegi adalah",luas)
def persegi_panjang():
    panjang = int(input("masukan panjang : "))
    lebar = int(input("masukan lebar : "))
    luas = panjang*lebar
    print ("jadi luas persegi panjang adalah ",luas)
def segitiga():
    alas = int(input("masukan alas : "))
    tinggi = int(input("masukan tinggi : "))
    luas = alas*tinggi/2
    print ("jadi luas segitiga adalah ",luas)
def lingkaran():
    jari= int(input("masukan jari-jari : "))
    phi = 3.14
    luas = phi * jari**2
    print ("jadi luas luas lingkaran adalah ",luas)
def menu():
    jawab = "y"
    i = 0
    while jawab=="y":
        print ("=======menghitung luas bangun datar========")
        print()
        print("PILIH MENU : ")
        print ("[1] persegi")
        print ("[2] persegi panjang")
        print ("[3] segitiga")
        print ("[4] lingkaran")
        print ()
        pilih = int(input("masukan menu yang anda pilih >> "))

        if pilih == 1:
            persegi()
        else:
            if pilih == 2:
                persegi_panjang()
            elif pilih == 3:
                segitiga()
            else:
                if pilih == 4:
                    lingkaran()
                else:
                    print("masukan menu yang ada !!!")
        jawab = input("mau lanjut hitung y/n ? ")
        i+=1
    print ("anda mengulang sebanyak, ",i,"kali")
menu()
