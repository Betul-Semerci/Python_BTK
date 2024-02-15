#sıralı sayı içerisinde en ortadaki sayı. 
#sıralı sayı çift ise en ortadaki iki sayıyı topla ve 2ye böl.
L=[]
for i in range(0,6):
    sayi=int(input("Sayı giriniz: "))
    L.append(sayi)
L.sort()
# print(L[2])    #ortadaki sayı 2 index nolu sayı
print(int((L[2]+L[3])/2))

