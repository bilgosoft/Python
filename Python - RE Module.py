# RE(Regular Expression) Module : Metin içerisinde istediğimiz formattaki metinleri yakalayabilmemize imkan tanır.

import re

text = "Bilgo Soft"

print(re.findall(" ",text))             # Beliritlen ifade var ise liste içinde hepsini getirir.
print(len(re.findall(" ",text)))        # Belirtilen ifadeden kaç tane olduğunu gösterir.
print(re.split(" ",text))               # Belirtilen ifadeyi her bulduğunda metni parçalar.
print(re.sub(" ","-",text))             # Belirtilen ifade ile belirtile ifadeyi değiştirir.
print(re.search("Bilgo", text))         # Belirtilen ifadenin adresini gösterir.
print(re.search("Bilgo", text).span())  # Belirtilen ifadenin hangi indeksler arasında olduğunu gösterir.
print(re.search("Bilgo", text).start()) # Belirtilen ifadenin başlangıç indeksini gösterir.
print(re.search("Bilgo", text).end())   # Belirtilen ifadenin bitiş indeksini gösterir.
print(re.search("Bilgo", text).group()) # Belirtilen ifadeyi gösterir.
print(re.search("Bilgo", text).string)  # Belirtilen ifadenin nerede arandığını gösterir.
