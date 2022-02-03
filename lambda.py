# fungsi lambda adalah membuat fungsi jadi satu baris 
# fungsi itu seperti ini 
print("# hasil dari function")
def penjumlahan (x,y):
    hasil = x**2 + y**3
    print (hasil)
penjumlahan(4,6)

# dijadikan satu baris
print("# hasil dari lamda")
hasil=(lambda x,y: x**2 + y**3)(4,6)
print (hasil)