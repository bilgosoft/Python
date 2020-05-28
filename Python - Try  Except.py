# Try - Except : Programımda hata çıkabileceğini düşündüğüm zaman kullandığım yapıdır.

try: # Hatanın olacağını düşündüğüm kod satırlarımı içine yazdığım bloğumdur.
    n1 = float(input("1. Sayıyı Giriniz : "))
    n2 = float(input("2. Sayıyı Giriniz : "))
    print("TOPLAM : ", n1 / n2)

except ZeroDivisionError: # Hata olduğu zaman çalışacak kod bloğumdur.
    print("Bölen 0 Olamaz")

except Exception as Error: # Hata olduğu zaman çalışacak kod bloğumdur. (İstediğimiz kadar hata bloğu yazabiliriz.)
    print("Hatalı Kullanım")

else: # Hata bloklarım çalışmaz ise çalışacak bloğumdur.
    print("Program Hatasız Çalıştı") 

finally: # Programımda hata olsada olmasada çalışacak bloğumdur.
    print("Program Hatalı / Hatasız Çalıştı")