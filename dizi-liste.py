#dizi:aynı türden elemanlardan oluşan objelerdir.
#liste:aynı türden olmak zorunda değil.
liste=["alp","semerci",32568935,"baba","okul"]
print(liste[-1])
print(liste.index("alp"))


#liste dilimleme
print(liste[2:3])
print(liste[::-1])
print(liste[::2])

# eleman ekleme
liste.append("anne")
print(liste)
liste.insert(1,"arslan")
print(liste)

""" 
L=[]
for i in range(0,5):
    sayi=int(input("sayı giriniz: "))
    L.append(sayi)
    print(L) """
""" for i in range(0,5):
    print("L[",i,"]",L[i]) """


#iki listeyi birleştirme
L1=[1,2,3,4,5]
L2=[6,7,8,9,10]
L3=L1+L2
print(L3)       # 1. yöntem

L1.extend(L2)   # 2. yöntem: L2'yi L1'e at demek
print(L1)

#listeyi ters çevirme
a=[1,2,3,4,5,6,7,8]
print(a[::-1])
print(a)        #bu yöntem sadece ters görmeye yarar. listenin içeriğini değiştirmez.

a.reverse()
print(a)        # bu yöntem listenin içeriğini kalıcı olarak ters çevirir.


#en küçük-en büyük değeri bulma
x=[]
topla=0
for i in range(0,5):
    sayi=int(input("sayı giriniz: "))
    x.append(sayi)
    topla+=sayi
print("en küçük ve en büyük sayıların toplamı ",max(x)+min(x))
print("aritmetik ortalama: ",topla/len(x))




