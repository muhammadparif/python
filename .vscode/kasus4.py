"""hitung total hutang seseorang selama setahun
1. jika hutangnya 5jt atau diatas 5jt maka akan dikenai bunga 10%/bulan
2. hutang dibawah 5jt berbunga 5%/bulan
3. jika yg berhutang itu pns bunganya ditambah 5%/bulan"""

hutang = int(input ("masukan hutang : Rp. "))
pekerjaan = input ("pekerjaan pns y/n: ")

if hutang >= 5000000:
    if pekerjaan.lower()=="y":
        hutang_sebulan = (10/100+5/100)*hutang
    else:
        hutang_sebulan = (10/100)*hutang

else :
    if hutang <= 5000000 and pekerjaan.lower() == "y":
        hutang_sebulan = (5/100+5/100)*hutang
    else:
        hutang_sebulan = (5/100)*hutang

thutang_setahun = (hutang - hutang_sebulan)*12
print ("total gaji setahun adalah Rp. ", thutang_setahun)

        
        