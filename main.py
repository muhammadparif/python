nim = 11
gaji_pokok = 1000000
gaji_lemburperjam = 5000
gaji_lembur = nim * gaji_lemburperjam
gaji_kotor = gaji_pokok + gaji_lembur
pajak = 10/100 
gaji_bersih = gaji_kotor - pajak
print ("gaji bersih = ", gaji_bersih)