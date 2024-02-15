L=[12,23,45,68,72,95]
deger=int(input("sayı giriniz: "))
if deger in L:
    indis=L.index(deger)
    print("aranan ",indis,"indis değerinde bulundu")
else:
    print("aranan değer bulunamadı!")
    