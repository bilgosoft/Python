# LIST : Birden fazla elemanı bellek üzerinde tek bir yapıda tutmamızı sağlayan kutucuklar olarak düşünebiliriz.
list1 = [1, 1.5, "ABC", True]
list2 = ["Hello World For Python"]

# LISTE FUNCTIONS
print(list1)			        # Listenin tüm elemanlarına erişim sağlar.
print(list1[0])                 # Listenin belirtilen elemanlarına erişim sağlar.
print(list1 + list2)            # Listeleri tek liste içinde erişim sağlar.
print(list1 , list2)            # Listeleri tek liste içinde 2 liste olarak erişim sağlar.
list3 = zip(list1, list2)       # İndeks numaralarına göre birleştirme yapar.
list2 = list1.copy()            # Var olan listeyi başka bir listeye kopyalar
list2 = list1.extend(list2)     # Var olan listeyi başka bir listenin sonuna kopyalar
list1 = len(list1)              # Liste içindeki eleman sayısına erişim sağlar.
list1 = min(list1)              # Listenin minumum değerine erişim sağlar.
list1 = max(list1)              # Listenin maksimum değerine erişim sağlar.
list1 = list1[0:]               # Listenin belirtilen indeksinden son indeksine kadar erişim sağlar.
list1 = list1[0:3]              # Listenin belirtilen indeksinden belirtilen indeksine kadar erişim sağlar.
list1[0] = 0                    # Listenin belirtilen indeksteki elemanı ile belirtilen veriyi ile günceller.
list1.append(8)                 # Listenin sonuna belirtilen veriyi ekler.
list1.insert(6,7)               # Belirtilen indeksdeki veriyi sağa kaydırarak belirtilen veriyi ekler.
list1.insert(-1,7)              # Listenin son indeksindeki veriyi sağa kaydırarak belirtilen veriyi ekler.
list1.pop()                     # Listenin son elemanını siler.
list1.pop(1)                    # Listenin belirtilen indeksindeki elemanını siler.
list1 = list1.index(1)          # Belirtilen ifadenin listenin kaçıncı indeksinde olduğunu bulur.
list1.remove(8)                 # Listenin belirtilen elemanını siler.
list1.sort()                    # Listeyi küçükten büyüğe sıralar.
list1.reverse()                 # Listeyi ters çevirir.
list1 = list1.count(1)          # Belirtilen ifadenin listede kaç adet olduğunu sayar.
list1.clear()                   # Listenin elemanlarını siler.
list1 = 2 in list1              # Liste içinde belirtilen ifadenin olup olmadığını kontrol eder.
del list1                       # Listeyi siler.
del list1[0]                    # Listenin belirtilen indeksindeki değeri siler.