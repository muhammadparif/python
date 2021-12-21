# gaji_bulanan = 5_000_000
# pajak = 2.5 / 100
# alpa = int(input("masukan jumlah tanpa keterangan :"))

# if alpa > 5 :
#     potongan = 25_000 * alpa
#     gaji_bersih = gaji_bulanan - potongan- pajak
#     print ("gaji seorang karyawan perbulan : Rp. ", gaji_bulanan)
#     print ("gaji bersih karyawan           : Rp. ", gaji_bersih)
#     print ("pajak                          : ", pajak)
# else:
#     gaji_bersih = gaji_bulanan - pajak
#     print("gaji bersih : Rp. ", gaji_bersih)


# tes seleksi lab rpl
while True:

    logika = input ("logika anda bagus/kurang ? ")
    mental = input ("mental anda bagus/kurang ? ")

    if logika == "bagus":
        print ("anda masuk ketegori")
        if mental == "bagus":
            print ("anda lolos seleksi lab rpl tapi masih ada tahap selanjutnya")
        else :
            print ("walaupun mental anda kurang tapi kamu lolos karena logika kamu bagus dan tunggu tahapan selanjutnya")

    elif logika == "kurang":
        print ("jika mental anda bagus masih ada harapan untuk lolos")
        if mental == "kurang" or mental == "kurang sekali":
            print ("anda tidak lolos")
        else:
            print ("walaupun logika anda kurang tapi kamu lolos karena mental kamu bagus dan tunggu tahapan selanjutnya")
    else :
        print ("maaf anda kurang beruntung")
        break
# totalBelanja = int (input("masukan total belanja : "))
# kodeHari = int (input ("masukan kode hari : "))

# if kodeHari == 1 :
#     diskon = totalBelanja * 1/100
# elif kodeHari == 2 :
#     diskon = totalBelanja * 2/100
# elif kodeHari ==  3:
#     diskon = totalBelanja * 3/100
# elif kodeHari == 4 :
#     diskon = totalBelanja * 4/100
# elif kodeHari == 5 :
#     diskon = totalBelanja * 5/100
# elif kodeHari == 6 :
#     diskon = totalBelanja * 6/100
# elif kodeHari == 7 :
#     diskon = totalBelanja * 7/100 
# else :
#     print ("kode hari anda salah ! ")

# bayar = (totalBelanja - diskon)
# print ("diskon hari ini ", kodeHari,"%","\njumlah diskon : ", diskon, "\njumlah yang harus di bayar : ", bayar)