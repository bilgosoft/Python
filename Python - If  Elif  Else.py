# IF - ELIF - ELSE : Koşul yapılarından yani bir sonucumuzu belirli bir şarta göre kontrol etmemizi sağlayan yapılardır.

# 1. If kullanımını anlamak için örnek
number = 10

# If : Koşul yapımda çalışan ilk bloğumdur. Eğer parantezler içine yazdığım şartım sağlanıyorsa if bloğumun içine girer.
if (number < 10): 
    print("Sayı 10' dan küçüktür.")

# Elif : Koşul yapımda eğer if bloğum çalışmaz ise elif bloğumun parantazlerimin şartını sorgular eğer koşulum sağlanır ise elif bloğumun içine girer.
elif (number > 10):
    print("Sayı 10' dan küçüktür.")

# Else : Eğer if ve elif bloklarım çalışmaz ise mutlaka çalışacak bloğumdur.
else:
    print("Sayı 10' dan küçüktür.")


# 2. İç içe if kullanımı
gender = input("Cinsiyet Giriniz (E / K): ")

if (gender == "E"):
    birtOfYear = input("Doğum Yılınızı Giriniz : ")
    if(2020 - birtOfYear == 20):
        print("Askere gidebilirsiniz.")
    else:
        print("Askere Gidemezsiniz")

elif (gender == "K"):
    print("Askere Gidemezsiniz")

else:
    print("Hatalı Giriş")
