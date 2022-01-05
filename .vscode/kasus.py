'''tentukan jumlah harga saka semen jika harga 1 sak semen itu 50000, jika membeli minimal 100 sak itu dapat potongan 2.5%, jika dia membeli diatas 200 sak semen maka dia memdapatkan diskon 10% lain dari pada itu tidak dapat potongan.'''


harga_satu_saksemen = 50000
sak = int (input('masukan jumlah sak yang anda beli : '))

if sak >= 100:
	potongan = (sak * harga_satu_saksemen)* 2.5/100
	bayar = (harga_satu_saksemen * sak)-potongan
	print('anda dapat potongan seharga, Rp. ', potongan)
else:
	if sak >=200:
		diskon = (sak * harga_satu_saksemen) *10/100
		bayar = (sak * harga_satu_saksemen)-diskon
	else:
		bayar = sak * harga_satu_saksemen
		print('anda tidak dapat potongan ')

				
print ('anda harus membayar seharga, Rp. ', bayar)