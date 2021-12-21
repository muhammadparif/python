kenalan = [
    "randi",
    "irfan",
    "danu",
    "masdar",
    "anri",
]
#menampilkan isi list index no 3

print ("nama index yg ke 3 adalah ", kenalan[3])
for x in kenalan:
    print(x)
print (len(kenalan))

# mengubah data di dalam list

kenalan[1] = "parif"

print (tuple(kenalan))

#menambahkan data di akhir list

kenalan.append("irfan")
print(kenalan)
# menambahkan data dengan ketentuan kita 

kenalan.insert(0, "rio")
print(kenalan)
#menghapus item 

kenalan.remove("rio")
print(kenalan)
# menghapus item dengan index

del kenalan[0]
print(kenalan)
# mengurutkan nilai list dari kecil sampai besar

a = [2,3,5,1,4,]
a.sort()
print ("dari kecil ke besar ")
print(a)
# mengurutkan nilai besar ke kecil

a.reverse()
print("dari besar ke kecil")
print(a)


