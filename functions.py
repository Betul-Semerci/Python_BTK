""" 
def topla():
    print("Toplama:iki veya daha fazla sayının toplanmasıdır.")
    print("Örneğin; ",5,"+",7,"=",13)

topla() """


""" def selamlama(isim="Betül"):
    print("Sayın ",isim,"Restoranımıza hoşgeldiniz.")

while True:                     
    isim=input("Adınızı giriniz: ")
    if (isim=="dur"):
       break
    
selamlama() """


# return: döndürme
# lambda: fonksiyonu tek satırda yazmamızı sağlar.
""" def elveda ():
    print("Görüşmek üzere..") """
elveda= lambda:print("Görüşmek üzere..")
elveda()


# global ve yerel değişkenler
#fonk.nun dışında çağırdığımızda gelmez, yukarıda global olduğunu belirtmeliyiz.
def topla ():
    #global a
    #global b
    a=5
    b=6
    return(a+b)

# pass yada return yazarsak şimdilik pas geç,hata verme anlamında.
def carpma ():
    #pass
    return

print(topla())
#print(a)       
#print(b)
print(carpma)
