""" class araba (marka):
    model=marka
    def metot(self):
        self.marka="mercedes" """


""" class hayvan (cins):
    tur=cins
    def metot (self):
        self.cins="balıklar"
 """


""" class araba():
    pass

#nesne oluşturma
otomobil=araba()
kamyon=araba()
 """

class araba ():                          #sınıf
    def __init__(self,model,marka,renk): #metot
        self.model=model
        self.marka=marka
        self.renk=renk
    def aracBilgisi(self):               #metot    
        print("Markası ",self.marka)
        print("Modeli ",self.model)
        print("Rengi ",self.renk)

taksi=araba(2020,"fiat","yeşil")         #nesne
taksi.aracBilgisi()
print("---------------")
kamyon=araba(2012,"Man","Beyaz")
kamyon.aracBilgisi()

""" taksi=araba(2020,"fiat","yeşil")
print(taksi.model)
print(taksi.renk)

taksi.model=20222   
print(taksi.model)

kamyon=araba(2012,"Man","Beyaz")
print(kamyon.renk)
 """