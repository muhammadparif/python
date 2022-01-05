harga_tanah_permeter = 300000
luas_tanah = int(input('masukan luas tanah : '))
harga_jual = harga_tanah_permeter * luas_tanah 

if harga_jual >= 100000000 :
	print ('anda di kenakan pajak 3%')
	potongan = harga_jual* 3/100
else:
	if harga_jual >= 50000000 :
		print ('anda di kenakan pajak 5%')
		potongan = harga_jual*5/100
	else:
		print('anda dikenakan pajak 1%')
		potongan = harga_jual*1/100

gaji_bersih = harga_jual - potongan		
print ('kamu harus membayar sebesar, Rp. ', gaji_bersih)