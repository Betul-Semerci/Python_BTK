#index:0'dan başlar
isim="BTK AKADEMİ"
print(isim[7])

#iki stringi birleştirme
x= "B"
y= "T"
z= "K"
print(x+y+z)
L=x+y+z
print(L)
print(L[1])

#string bölme
s="python"
print(s[:])
print(s[3:])
print(s[:2])
print(s[2:4])
print(s[1::2])  #1den başla 2 2 atla
print(s[1:6:3]) # 1den başla,6ya kadar git,3er 3er atla
print(s[::-1])  #stringi ters çevirir


#karakter değiştirme
s="python"
s2=s[:3]+"t"+s[4:]
print(s2)


#string güncelleme/değiştirme
adres= "Selçuklu-KONYA"
adres2= "Meram"+adres[8:]          # 1. yöntem
print (adres2)

adres=adres.replace("Selçuklu","Meram")  # 2. yöntem
print(adres)

# silme
""" yazi="python"
print(yazi[:-2]) """

yazi="python"
for a in range(1,6):
    print(yazi[:-a])


# karakter sayısı öğrenme
cumle="merhaba nasılsınız?"
print(len(cumle))

print(cumle.count("ı"))   #ı'dan kaç tane var


