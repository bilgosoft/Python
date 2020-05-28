# Math Module : Matematiksel işlemleri yapmamızı sağlayan modüldür.

from math import *

print(ceil(5.1))                                      # Yukarı yuvarlar.
print(floor(5.1))                                     # Aşağı yuvarlar.
print(abs(5))                                         # Tam sayı olarak mutlak değeri hesaplar.
print(fabs(5))                                        # Ondalıklı sayı olarak mutlak değeri hesaplar.
print(factorial(5))                                   # Faktoriyel hesaplar
print(45%14)                                          # Pozitif sayılarda tam sayı sonuçlu mod alma işlemini yapar
print(fmod(45,-14))                                   # Pozitif ve negatif sayılarda ondalıklı sayı sonuçlu mod alma işlemini yapar
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))  # Toplama işlemini yapar.
print(fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])) # Toplama işlemini yapar. Sum dan daha kesin sonuç döndürür.
print(gcd(50,4))                                      # Belirtilen değerler için EBOB hesaplar.
print(pi)                                             # Pi değerini barındırır.
print(pow(2,3))                                       # 1. değerin 2. değer ile kuvvetini hesaplar.
print(sqrt(2))                                        # Belirtilen değerin karesini hesaplar.
print(sin(2))                                         # Belirtilen değerin sinisüni hesaplar.
print(cos(2))                                         # Belirtilen değerin cosinüsünü hesaplar.
print(tan(2))                                         # Belirtilen değerin tanjantını hesaplar.