# Random : Rastgele sayı üretmemizi sağlayan modüldür.

import random

print(random.random())              # 0.0 - 1.0 arası ondalıklı sayı üretir.
print(random.uniform(1,100))        # Belirtilen değerler arası ondalıklı sayı üretir.
print(random.randint(1,100))        # Belirtilen değerler arası tam sayı üretir.
print(random.randrange(1,10))       # Belirtilen değerler arası sayı üretir.
numbers = [1,2,3,4,5]
print(random.choice(numbers))       # Liste içinden rastgele eleman seçer.
print(random.sample(numbers, 3))    # Liste içinden rastgele sayı getirir.