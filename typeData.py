# nilai = 12
# hobi = "ngoding"
# nilai1 = 12.2
# status_pernikahan = False

# print (type(nilai))
# print (type(hobi))
# print (type(nilai1))
# print (type(status_pernikahan))

mk = input("masukan matkul yang UAS : ")
mk = mk.lower()

if mk == "DDP" :
    print ("tetap menyerah dan jangan semangat wkwkwk")
    if mk == "PSTI":
        print ("satu materi lagi baru kita UAS")
    else:
        if mk == "pendidikan pancasila" or mk == "PKN":
            print ("satu materi lagi baru kita final")
        else :
            print ("masukan mk dengan benar")
else:
    print ("masukan mk dengan benar")
    