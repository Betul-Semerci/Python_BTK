#range(): belirli aralıktaki sayıları göstermek için

""" sayi=[1,2,3,4,5,6]
for i in range (len(sayi)):
   if i>3:
     break
   print(i)
 """

# break: belirtilen yerde dur
# continue: belirtilen yeri atla ve devam et

""" for i in range(5,11):
    if i==8:
        continue
    print(i) """

# 1den 30a kadar olan tek sayıları yazdır.

""" 
for i in range(1,31):
    if i%2 ==0:
     print(i) """
""" i=0
while i<10:
    print("MERHABA")
    i+=1 """

""" 
x=1
print("Çıkış için sıfıra bas")
while (x!=0):
    x= int(input("Sayı giriniz: "))
    print("Sayının karesi= ",x*x)
print("Güle güle")
 """

# while True: sonsuz döngü
while True:
    a=int(input("Sayı giriniz: "))
    if (a==4):
        break
    else:
        print(a)
