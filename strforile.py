a=""
s=0
indis=int(input("İndex no giriniz: "))
for d in "btkakademi":
    if s==indis:
        a=d
    s+=1
print(a)

#listeye çevirme

cumle="okulu_çok_seviyorum"
cumle=cumle.split("_")
print(cumle)

metin="1256 7892 4567 1576"
metin=metin.split(" ")
print(metin)