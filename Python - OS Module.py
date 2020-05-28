# OS Module : Dosya işlemlerini yapmamızı sağlayan modüldür.

import os

print(os.name)                                      # İşletim sisteminin ismini gösterir.
print(os.getcwd())                                  # Dizinin yolunu gösterir.
os.chdir("C:\\")                                    # Dizinin yolunu değiştirir.
os.chdir("..")                                      # Dizinin 1 üst dizinine götürür.
os.chdir("../..")                                   # Dizinin 2 üst dizinine götürür.
os.mkdir("NewDirectory")                            # Yeni dizin oluşturur.
os.rename("NewDirectory,YeniDizin")                 # Dizin adını değiştirir
os.rmdir("YeniDizin")                               # Dizin siler.
os.makedirs("NewDirectory/DifferentDirectory")      # İç içe dizin oluşturur.
os.removedirs("NewDirectory/DifferentDirectory")    # İç içe olan dizinleri siler.

print(os.listdir("C:\\"))                           # Etkin klasörleri listeler.
for keep in os.listdir("C:\\"):                     # Listeleme için filtre uygulama
    if  keep.endswith(".png"):
        print(keep)

print(os.stat("project.py"))
print(os.stat("project.py").st_size / 1024)                             # Dosyanın Kb cinsinden büyüklüğünü hesaplar.
print(datetime.datetime.fromtimestamp(os.stat("project.py").st_ctime))  # Oluşturulma tarihini gösterir.
print(datetime.datetime.fromtimestamp(os.stat("project.py").st_atime))  # Son etkileşim tarihini gösterir.
print(datetime.datetime.fromtimestamp(os.stat("project.py").st_mtime))  # Son değişiklik tarihini gösterir.
os.system("notepad.exe")                                                # Uygulama açar.
print(os.path.abspath("project.py"))                                    # Dizinin ismini gösterir
print(os.path.dirname("project.py"))
print(os.path.exists("project.py"))                                     # Belirtilen dosyanın var olup olmadığına bakar
print(os.path.isdir("project.py"))                                      # Belirtilen ifadenin dizin olup olmadığını kontrol eder.
print(os.path.isfile("project.py"))                                     # Belirtilen ifadenin dosya olup olmadığını kontrol eder.
print(os.path.join("C:\\","Directory"))                                 # Dizinleri birleştirir.
print(os.path.split("C:\\Directory"))                                   # Dizinleri ayırır.
