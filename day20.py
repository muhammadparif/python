# Membuat Tuple
hari = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jum\'at', 'Sabtu', 'Minggu')

# Mengambil panjang tuple hari
print("Jumlah hari : ",  len(hari))

def main():
    #nesteed tuple

    tuple1 = ("aku","hobi","ngoding")
    tuple2 = ("bahasa","pemrograman","python")
    hasil = (tuple1,tuple2)
    print (hasil)
    print (hasil[0][2])
    
main()
