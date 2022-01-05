'''Begini 1. Pembuatan Sim Jika umurnya lebih dari 17 tahun Boleh Membuat Sim 
2. Jika Boleh Membuat Sim Maka di kenakan pajak 7.5 % Dengan Harga Motor
3. Jika Umurnya Sudah 80 tahun Sudah Tidak Di Perbolehkan Berkendara'''

umur = int(input("masukan umur : "))
harga_motor = int(input("masukan harga motor : Rp. "))
pajak = 7.5 /100
if umur >= 17 and umur < 80 and harga_motor >=15000000 and harga_motor <= 50000000:
	bayar_pajak = harga_motor * pajak
	print ('anda boleh membuat sim tapi anda harus membayar pajak sebesar, Rp. ', bayar_pajak)

else : 
	if umur >= 80 :
		print('anda tidak di perbolehkan berkendara')
	else :
		print ('kamu masih anak2')