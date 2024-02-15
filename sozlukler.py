""" mevsim= {'kış':1,'ilkbahar':2,'yaz':3,'sonbahar':4}
#dictionary:sözlük demek
tc=dict([('talat,1234'),('alp,4567'),('semih,7890')])
 """
mevsim= {'kış':1,'ilkbahar':2,'yaz':3,'sonbahar':4}
print(mevsim.get('yaz','yok'))   #get: getir anlamında
print(mevsim.get('ilk','yok'))   #aradığımız yoksa 'yok yazacak
print(mevsim.pop('kış'))         #pop: seçileni sil
print(mevsim)
print(mevsim.keys())
print(mevsim.values())


