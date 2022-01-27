print ("==============================================================")
print ("\tPROGRAM MENGHITUNG VOLUME DAN LUAS PERMUKAAN BOLA")
print ("==============================================================")

def volume_bola(jari_jari, phi):
    
    rumus = 4/3*phi*jari_jari**3
    return rumus
v= volume_bola(7,22/7)
print ("volume bola adalah ",v)

def luas_bola(r,phie):
    luas = 4 * phie*r**2
    return luas
l=luas_bola(9,3.14)
print ("luas permukaan bola adalah ", l)

