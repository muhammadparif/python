"""Diketahui gaji seorang pejabat = 5jt
Hitung gaji bersih seorang pejabat sesuai golongannya
1. Golongan pertama dikenai pajak 20%
2. Golongan Kedua dikenai pajak 15%
3. Golongan ketiga dikenai pajak 10%"""

gaji_pejabat = 5_000_000
gol = input("masukan golongan : ")
gol.lower()
if gol == "pertama":
    pajak = 20/100
else:
    if gol == "dua":
        pajak = 15/100
    else:
        if gol == "tiga":
            pajak = 10/100
        else:
            print ("masukan golongan dengan benar")

potongan = gaji_pejabat*pajak
gaji_bersih = gaji_pejabat-potongan
print ("gaji bersih anda Rp. ", gaji_bersih)