# Functions : Bir kodu bir defa yazıp daha sonra istediğimi her yerde kullanabilmemizi sağlayan yapıdır.

# Geriye Değer Döndürmeyen Parametresiz Fonksiyon
def Func1():                            
    print("First Function !")
Func1()

# Geriye Değer Döndürmeyen Parametreli Fonksiyon
def Func2(Language):                    
    print(f"First Function - For {Language}")
Func2("Python")

# Geriye Değer Döndürmeyen Parametreli Fonksiyon
def Func3(Name):                        
    name = input("İsminizi Giriniz : ")
    print(f"Hello {name}!")
Func3(Name)

# Geriye Değer Döndüren Parametresiz Fonksiyon
def Func4():                            
    return 2 + 2
print(Func4())

# Geriye Değer Döndüren Parametreli Fonksiyon
def Func5(n1, n2):                      
    return n1 + n2
print(Func5(1,2))

# Geriye Değer Döndüren Sınırsız Parametreli Fonksiyon
def Func6(*params):                     
    return sum(params)
print(Func6(1,2,3,4,5,6,7,8,9,10))

# İç İçe Fonksiyon Tanımlama
def Func7():                           
    name = "Timuçin"
    def Func8():
        print("Hello " + name)
    Func8()
Func7()

# Map Function : Fonksiyonda yaptığımız işlemi liste içine aktarmamızı sağlayan fonksşyondur.
def Func9(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = list(map(Func9, numbers))
print(numbers)

# Filter Function : Eğer fonksiyonum içindeki işlem true değer döndürüyor ise filter fonksiyonum listemin içine true dönen değerleri ekliyor.
def Func10(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = list(filter(Func10, numbers))
print(numbers)