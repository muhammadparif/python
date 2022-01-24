def jam_ke_menit(menit):
	print('convert jam ke menit'.center(50,'='))
	jam =int(input('masukan jam : '))
	hasil = jam * menit
	return hasil

def jam_ke_detik(detik):
	print('convert jam ke detik'.center(50,'='))
	jam = int(input('masukan jam : '))
	hasil = jam*detik
	return hasil

def menit_ke_detik(detik):
	print('convert menit ke detik'.center(50,'='))
	menit =int(input('masukan menit : '))
	hasil = menit*detik
	return hasil
	
def menit_ke_jam(jam):
	print('convert menit ke jam'.center(50,'='))
	menit =int(input('masukan menit : '))
	hasil = menit*jam
	return hasil
	
def detik_ke_menit(menit):
	print('convert detik ke menit'.center(50,'='))
	detik =int(input('masukan detik : '))
	hasil = detik*menit
	return hasil

	
def detik_ke_jam(jam):
	print('convert detik ke jam'.center(50,'='))
	detik =int(input('masukan detik : '))
	hasil = detik*jam
	return hasil
c=detik_ke_jam(1/3600)
print(c,'jam\n')
b=detik_ke_menit(1/60)
print(b, 'menit\n')
a=menit_ke_jam(1/60)
print(a,'jam\n')
d=menit_ke_detik(60)
print(d,'detik\n')
e=jam_ke_menit(60)
print(e, 'menit\n')
f=jam_ke_detik(3600)
print(f, 'detik')