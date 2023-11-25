print("""
*******************************
Kullanıcı Girişi Programı
*******************************
""")

sys_kullanıcı_adı = "radon"
sys_parola = "12345"

giriş_hakkı = 3
while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola:
        print("Kullanıcı Adı Hatalı.")
        giriş_hakkı -=1
        print("giriş hakkı sayınız:",giriş_hakkı)
    elif kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola:
        print("parola Hatalı.")
        giriş_hakkı -= 1
        print("giriş hakkı sayınız:", giriş_hakkı)
    elif kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola:
        print("Kullanıcı Adı ve Parola Hatalı.")
        giriş_hakkı -= 1
        print("giriş hakkı sayınız:", giriş_hakkı)
    else:
        print("Giriş yapıldı")
        break
    if giriş_hakkı == 0:
        print("Giriş Hakkınız bitti.")
        a = input("Şifrenizi veya Kullanıcı adınızı mı unuttunuz? (evet/hayır):")
        if a == "evet":
            print("mail gönderiliyor.....")
            b = input("Lütfen kullanıcı adı mı yoksa parola mı değiştireceğinizi seçiniz:")
            if b == "kullanıcı adı":
                sys_kullanıcı_adı = input("Yeni Kullanıcı Adınızı girin:")
            elif b == "parola":
                sys_parola = input("Yeni Parolanızı girin:")
            else:
                print("Lütfen Geçerli işlem seçin")

        else:
            print("Çıkılıyor....")
            break