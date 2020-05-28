# Yazdığımız modülü barındıracak sayfaya kodlarımızı yazıyoruz. (Proje İsmi : modul.py)
n1 = 5

def WriteModule():
    print("Bilgo Soft")

# Yazdığımız modülü kullanacağımız sayfaya aşağıdaki kodları yazıyoruz.
import modul

print(modul.n1)
modul.WriteModule()