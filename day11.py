''' menampilkan bilangan ganjil dan genap dibawah 100 dengan menggunakan
percabnagan dan perulangan for '''

# percabangan
bilangan = int(input ("masukan bilangan : "))

if bilangan  %2 == 0 and bilangan <= 100 :
    print (bilangan , "adalah bilangan genap ")
else :
    print (bilangan , "adalah bilangan ganjil")
print ()
# perulangan
print ("bilangan genap")
for item in range(2, 100+1,2):
    print (item)
print("bilangan ganjil")
for i in range (1, 100,2):
    print (i)



