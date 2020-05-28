# SET LIST : Diğer listelerden farkı döngü haricinde elemanlarına ulaşılmamasıdır.

list1 = {1, 2, 3, 4, 5} # Sets listesi oluşturduk.

for keep1 in list1: # Döngü yardımı ile elemanlarına ulaştık.
    print(keep1)

#  SET FUNCTIONS
list1.add(6)            # Veri eklemeyi sağlar.
list1.update([7,8,9])   # Toplu veri eklemeyi sağlar.
list1.remove(1)         # Belirtilen veriyi siler.
list1.discard(2)        # Belirtilen veriyi siler.
list1.pop()             # Sıralı olmadığı için rastgele bir veri siler.
list1.clear()           # Tüm verileri siler.