print ('|=====MUH.PARIF=====|')
print ('|======D0221044=====|')
print ('|===INFORMATIKA.C===|')
print()

print ("SELAMAT DATANG DI ATM SAYA\n")
print ("Pilih option :\n")
print ('1. cek uang saya')
print ('2. ambil uang saya')
print ('3. tabung uang saya')
print ()

while True:
    
    option = int (input ('silahkan pilih option :'))
    if option==1:
        print ('uang kamu berjumlah Rp. 4.200.000')
    elif option==2:
        print ('uang kamu berjumlah Rp. 4.200.000, mau ambil berapa pak/bu?')
        print ('1. Rp. 2.000.000')
        print ('2. Rp. 3.000.000')
        uang_kamu = 4200000
        option2=int(input("option :"))
        if option2==1:
            hasil = uang_kamu-2000000
            print ('uang kamu sekarang berjumlah :', hasil)
        elif option2==2:
            hasil2 = uang_kamu-3000000
            print ('uang kamu sekarang berjumlah :', hasil2)
        else:
            print ('keyword anda salah !!!')

    elif option==3:
        uang_kamu = 4200000
        print ('uang berjumlah Rp. 4.200.000, mau nabung berapa pak/bu ?')
        option3=int(input('masukan jumlah uang :'))
        hasil3 = uang_kamu + option3
        print ('jumlah uang kamu sekarang adalah ', hasil3)
    else:
        print ('keyword anda salah , mohon coba lagi!!!')
        break
