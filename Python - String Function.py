# STRING FUNCTIONS : Metinsel ifadeler üzerinde çeşitli işlemler yapmamızı sağlayan yapıdır.

text = "Hello World"
text = len(text)                      # Belirtilen ifadenin karakter sayısını hesaplar.
text = text.capitalize()              # İlk karakteri büyük harfe çevirir.
text = text.casefold()                # Tüm karakteri küçük harfe çevirir.
text = text.center(50,"-")            # Metni belirtilen sayıda hizalar.
text = text.rjust(50,"-")             # Metni belirtilen sayıda sağdan hizalar.
text = text.ljust(50,"-")             # Metni belirtilen sayıda soldan hizalar.
text = text.count(" ")                # Belirtilen ifadeden metin içinde kaç adet olduğunu sayar. Exa : text.count(" ",0,5)
text = text.find(",")                 # Belirtilen ifadeden metin içinde hangi index de olduğuna bakar. Exa : text.find(",",0,5)
text = text.startswith("hELLO")       # Metnin ilk ifadesi belirtilen ifade ile mi başlıyor?
text = text.endswith("hELLO")         # Metnin son ifadesi belirtilen ifade ile mi başlıyor?
text = text.upper()                   # Tüm karakterleri büyük harf yapar.
text = text.lower()                   # Tüm karakterleri küçük harf yapar.
text = text.title()                   # Her kelimenin ilk karakterini büyük harf yapar.
text = text.strip()                   # Baştaki ve sondaki boşlukları siler.
text = text.rstrip()                  # Baştaki boşlukları siler.
text = text.lstrip()                  # Sondaki boşlukları siler.
text = text.split(",")                # İfade içinde belirtilen ifade var ise o ifadeyi silerek asıl ifadeyi parçalar.
text = "-".join(text)                 # Her karakter arasına belirtilen ifadeyi ekler.
text = text.replace("hELLO","Hello")  # İfade değiştirmeyi sağlar.
text = text.expandtabs(1)             # /t ifadesini görünce parantez içinde belirtilen sayı kadar boşluk koyar.
text = text.partition(",")            # Belirtilen ifadeyi metinde ortaya alarak 3 elemanlı liste yapar.
text = text.splitlines()              # /n ifadesini görünce öncesinde ve sonrasında olan ifadeleri listeye çevirir.
text = text.swapcase()                # Büyük karakterleri küçük, küçük karekterleri büyük yapar.
text = text.isalpha()                 # Tüm ifadenin " " içinde alfabetik karakter olup olmadığını kontrol eder.
text = text.isdigit()                 # Tüm ifadenin " " içinde numaratik karakter olup olmadığını kontrol eder.
text = text.islower()                 # Tüm ifadenin " " içinde küçük ve numaratik karakter olup olmadığını kontrol eder.
text = text.isupper()                 # Tüm ifadenin " " içinde büyük ve numaratik karakter olup olmadığını kontrol eder.
text = text.isspace()                 # Tüm ifadenin " " içinde sadece boşluk karakteri olup olmadığını kontrol eder.
text = text.istitle()                 # Tüm ifadenin " " içindeki ifadelerin ilk karakterleri büyük olup olmadığını kontrol eder.
print("A","B","C",sep="-")            # Her ifadenin arasına belirtilen ifadeyi yazar.
print("A","B","C",end="\n")           # İfadenin sonuna belirtilen ifadeyi yazar.