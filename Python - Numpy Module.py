# Numpy Module : Bilimsel hesaplamaları kolaylıkla yapmamızı sağlayan modüldür.

import numpy as np 

# TEK BOYUTLU DİZİ (VECTOR)
print(np.array([1,3,5,7,9]))                    # Tek boyutlu liste oluşturma.
print(np.array([1,3,5,7,9], dtype="float32"))   # Tek boyutlu liste oluşturma.
print(np.array([1,3,5,7,9][0]))                 # Belirtilen elemana erişim sapğlar.
print(np.arange(1,10))                          # 1' den 10 a kadar sayılarla liste oluşturur.
print(np.arange(1,10,2))                        # 1' den 10 a kadar sayılarla 2 artışlı liste oluşturur.
print(np.zeros(10))                             # 10 tane 0 olan liste oluşturur.
print(np.ones(10))                              # 10 tane 1 olan liste oluşturur.
print(np.linspace(1,10,5))                      # Belirtilen adetde Belirtilen değerler arasında dizi oluşturur.
print(np.random.normal(20,1,(3,4)))
print(np.random.randint(1,10,5))

# ÇOK BOYUTLU DİZİ (MATRIX)
print(np.ones((3,5)))                           # 3 satır 5 sutünluk dizi oluşturduk.
print(np.full((3,5), 2))                        # 3 satır 5 sutünluk 2 sayısı ile dizi oluşturduk.

# NUMPY FUNCTIONS
print(np.array([1,3,5,7,9]).ndim)               # Boyut sayısını gösterir.
print(np.array([1,3,5,7,9]).shape)              # Boyut bilgisini gösterir.
print(np.array([1,3,5,7,9]).size)               # Toplam eleman sayısını gösterir.
print(np.array([1,3,5,7,9]).dtype)              # Veri tipini gösterir.
print(np.arange(1,10).reshape((3,3)))           # Tek boyutlu diziden çok boyutlu diziye dönüştürüyoruz.
list1 = np.array([1,2,3])
list2 = np.array([4,5,6])
print(np.concatenate([list1,list2]))            # Tek boyutlu dizileri birleştirmek.
list3 = np.array([[1,2,3],[4,5,6]])
print(np.concatenate([list3,list3]))            # Çok boyutlu dizileri satır bazında birleştirmek.
print(np.concatenate([list3,list3], axis=1))    # Çok boyutlu dizileri sütun bazında birleştirmek.
print(np.split(list1,[1,2]))                    # Diziyi parçalar.
print(np.sort(list1))                           # ASC standartında sıralar.
list4 = np.array([1,3,5,7,9])
print(list4 > 5)                               # Koşul döndürüyoruz.
print(list4[list4 > 5])                        # Fancy Index ile elemanlara ulaşıp koşul değerlendirdik.
print(list4 - 1)                               # Tüm elemanlardan 1 çıkardık.