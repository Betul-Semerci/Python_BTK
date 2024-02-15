# ==,!=,is

sifre="1234"
kullanici="betül"

k_giris=input("Kullanıcı adı giriniz: ")

if k_giris==kullanici:
    s_giris=input("Şifre giriniz: ")
    if s_giris==sifre:
        print("Hoşgeldiniz")
    else:
        print("Şifre hatalı!!")
else:
    print("Kullanıcı adı hatalı!!")
    