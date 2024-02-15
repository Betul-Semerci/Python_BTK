gun=input("Türkçe gün adı : ")

tr_en={'Pazartesi':'Monday','Salı':'Tuesday','Çarşamba':'Wednesday','Perşembe':'Thursday','Cuma':'Friday','Cumartesi':'Saturday','Pazar':'Sunday'}
print("İngilizcesi: ",end="")
print(tr_en.get(gun,"Bu kelime sözlükte yok!"))


