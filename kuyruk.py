# diziler-listeler/bölüm sonu alıştırma

liste=[]
while True:
    tc=int(input("TC Giriniz: "))
    if tc in liste:      #tc listenin içinde mevcut mu?
        i=liste.index(tc)    # bu tc li kişinin listedeki indexi nedir?
        print("Muayene sırası: ",i+1)  #i 0dan başladığı için i+1 yaptık
    elif tc==0:           # giriş ekranına sıfır yazıldığında 
        print(list[0])    # ilk hasta muayeneye girdi ve pop ile onu silip sıradan çıkardık.
        liste.pop(0)
    else:
        liste.append(tc)    #yeni hasta kaydı
        print(tc," TC Numaralı hasta sıraya alındı.")

    