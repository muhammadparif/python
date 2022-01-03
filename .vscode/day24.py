def luas_persegi_panjang(pjg, lebar):
    print ("menghitung luas persegi panjang")
    luas = pjg * lebar
    return luas

i = 0 
while i <= 5:
    x = luas_persegi_panjang(i, 3)
    print (x)
    i += 1