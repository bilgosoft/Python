# While : Bir işlemi belirttiğimiz kadar tekrarlanmasını istediğimiz zaman kullandığımız yapıdır.

# 1. Örnek : Ekrana "Hello World" yazan kısır(sonsuz) döngüyü oluşturalım.
while (True):
    print("Hello World")

# 2. Örnek : Ekrana 1' den 10' a kadar yazdıralım
number = 1 # For döngümdeki range kavramım olmadığı için bir başlangıç değişkeni oluşturmak zorundayım.
while (number <= 10): # Yukarıda başlangıç değişkeni oluşturduğum için parantez içine nereye kadar döngümün döneceğini yani bitiş değerimi belirtiyorum.
    print(number) # Döngüm her döndüğünde ekrana sayımı basması için print fonksiyonumu kullanıyorum.
    number += 1 # Döngüm her döndüğünde sayımı 1 arttırıyorum.

# 3. Örnek : Ekrana 10' dan 1' e kadar yazdıralım.
number = 10
while (number >= 1):
    print(number)
    number -= 1

# 4. Örnek : Ekrana 1' den 100' e kadar olan tek sayıları yazdıralım.
# 1. Yöntem
number = 1
while (number <= 100):
    print(number)
    number += 2

# 2. Yöntem
number = 1
while (number <= 100):
    if (number % 2 == 1):
        print(number)
        number += 1


