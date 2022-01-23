mtk = int(input("masukan nilai mtk : "))
bindo = int(input("masukan nilai b.indonesia : "))
binggi = int(input("masukan nilai b.inggris : "))
rata2 = (mtk+bindo+binggi)/3
minat = int(input("masukan minat anda 1/2/3 :"))


if rata2 < 70:
    print("anda tidak lulus karena nilai anda ", round(rata2))
else:
    if rata2 == 70:
        if minat == 1:
            print ("teknik elektro")
        else:
            if minat == 2:
                print("teknik mesin")
            else:
                print("pariwisata")
    else:
        print ("anda bebas memilih bidang yang anda suka karena nilai anda ",round(rata2))