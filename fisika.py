print ("==============================================================")
print ("\tPROGRAM MENGHITUNG KECEPATAN JARAK DAN WAKTU")
print ("==============================================================")

print("\npilih menu yang mau kita hitung")
print("[1]. kecepatan","\n[2]. jarak","\n[3]. waktu ")
jawab = "y"
while jawab == "y":
    print ()
    menu = input("masukan menu yang mau di hitung : ")

    if menu ==str(1) or menu.lower() =="kecepatan":
        waktu = float(input('masukan waktu (Jam): '))
        jarak = float(input('masukan jarak (Km): '))
        kecepatan = jarak/waktu
        print ("========================================================")
        print ("kecepatan yang anda tempuh adalah ",kecepatan,"Km/Jam")
        print ("========================================================")
    else:
        if menu == str(2) or menu.lower() == "jarak":
            waktu = float(input('masukan waktu (Jam): '))
            kecepatan = float(input('masukan kecepatan (Km/Jam): '))
            jarak = kecepatan*waktu
            print ("=====================================================")
            print ("jarak yang anda tempuh adalah ",jarak,"Km")
            print ("=====================================================")

        else:
            if menu == str(3) or menu.lower() == "waktu":
                kecepatan = float(input('masukan kecepatan (Km/Jam): '))
                jarak = float(input('masukan jarak (Km): '))
                waktu = jarak/waktu
                print ("==================================================")
                print ("waktu yang anda tempuh adalah ",waktu,"Jam")
                print ("==================================================")
            else:
                print ("masukan menu yang ada !!!")
    
    
    jawab=input(" Mau menghitung lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")

    






