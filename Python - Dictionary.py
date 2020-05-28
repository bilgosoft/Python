# DICTIONARY LIST : KEY - VALUE şeklinde çalışır. Veriye ulaşmak için o verirnin anahtarına ihtiyacımız vardır.

#  I. YÖNTEM
list = { 34 : "İstanbul", "İstanbul" : 34}

# II. YÖNTEM
list = \
    {
        34 : "İstanbul",
        "İstanbul" : 34
    }

print(list[34], list["İstanbul"])

user = \
    {
        1 : {
    "Name" : "Ali",
    "Surname" : "YILDIRIM",
    "Age" : 42
              },
        2 : {
    "Name": "Ayşe",
    "Surname": "KARA",
    "Age": 28
             }
    }

print(user[1])
print(user[2]["Name"])