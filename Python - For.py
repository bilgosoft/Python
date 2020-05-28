# FOR : Bir işlemi belirttiğimi kadar tekrarlanmasını istediğimiz zaman kullandığımız yapıdır.

# 1. Örnek : Ekrana 1' den 10' a kadar olan sayıları yazdılarım.
# for : Döngümü başlatmam için yazdım
# keep : içine değer atayabileceğim bir değişken ismi yazıyorum.(keep opsiyoneldir. Farklı isim kullanabilirsiniz.)
# in : Kelime anlamı içinde olan in, döngümün neyin içinde döneceğini belirler.
# range : aralığımı belirtmem için yazdığım fonksiyonumdur.
# Parantez içindeki 1. parametrem başlangıç değerimdir.
# Parantez içindeki 2. parametrem bitiş değerimdir. En son yazılacak değerin 1 fazlasını parametre olarak girmeliyim.
# Parantez içindeki 3. parametrem artış değerimdir. Yazmadığım zaman default parametrem 1 olarak algılanır.
for keep in range(1, 11, 1):
    print(keep)

# 2. Örnek : Ekrana 1 ile 10 arasındaki tek sayıları yazdıralım.
for keep in range(1, 10, 2):
    print(keep)

# 3. Örnek : Ekrana 10' dan 1 e kadar yazdıralım.
for keep in range(10, 0, -1):
    print(keep)

# 4. Örnek : "Hello World" ifadesinin karakterlerini alt alta yazdıralım.
for keep in "Hello World": # Döngü ifademin içinde döneceğinden dolayı range fonksiyonumu kullanmama gerek kalmıyor.
    print(keep)

# 5. Örnek : Ekrana liste içindeki elemanları yazdıralım.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for keep in list1: # Döngüm liste içinde döneceğinden dolayı range fonksiyonumu kullanmama gerek kalmıyor.
    print(keep)