#stringi listeye dönüştürme

kelime="btkakademi"
L=[]
L=list(kelime)
print(L)


#belirli elemanları silme

L.remove("a")  #tek seferde tek a siler diğerleri için tekrar yazmak gerekiyor.
print(L)

L.pop(1)
print(L)        #belirli bir indexteki elemanı silmek için

L.clear()
print(L)        #hepsini silmek için