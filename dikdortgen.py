#dik. alanı:u*g     çevre:(u+g)*2

def alan (u,g):
    a=u*g
    return a

def cevre (u,g):
    c=(u+g)*2
    return c

u=int (input("dikdörtgenin uzun kenarını giriniz: "))
g=int (input("dikdörtgenin kısa kenarını giriniz: "))

print("dikdörtgenin alanı: ",alan(u,g))
print("dikdörtgenin çevresi: ",cevre(u,g))
   