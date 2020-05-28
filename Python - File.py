# File Operations

# 1. Yöntem : Her dosya açtıktan sonra kapatılması gerekir.

# open() : Dosya açma fonksiyonudur.
file = open("C:\\text2.txt","w", encoding='utf-8')
file.close()

# 2. Yöntem : Dosyayı kapatmak gerekmez.
with open("C:\\text2.txt","w", encoding='utf-8') as file:
    file.write("Hello World")

# w : (Write) yazma komutudur. Dosyayı konumda oluşturur.
file = open("C:\\text2.txt","w", encoding='utf-8')
file.write("Hello World")

# a : (Append) ekleme komutudur. Dosya konumda yoksa oluşturur.
file = open("C:\\text2.txt","a", encoding='utf-8')
file.write("\nBilgo Soft")

# x : (Create) oluşturma komutudur. Dosya konumda varsa hata verir.
file = open("C:\\text3.txt","x", encoding='utf-8')

# r : (Read) okuma komutudur. Dosya konumda yoksa hata verir.
file = open("C:\\text2.txt","r", encoding='utf-8')
print(file.read())        # Tüm içeriği okur.
print(file.read(50))      # İçeriğin ilk 50 karakterini okur.
print(file.readline())    # 1 satır okur.
print(file.readlines())   # Listeye çevirerek okur
print(file.tell())        # Cursor yerini bildirir.
file.seek(0);             # Cursor yönlendirir.

# close() : Dosya kapama fonksiyonnudur.
file.close()