# Beautifulsoap Module : HTML verilerini çekmek için kullanılan modüldür.

from bs4 import BeautifulSoup 

soup = BeautifulSoup(bilgoSoft.content, "html.parser")  # Kaynak kodları soup' a gömüyoruz.
soup.prettify()                                         # Kodları console ekranında düzenler.
soup.title                                              # Title içeriğini alır.
soup.title.name                                         # Etiket ismini alır.
soup.title.string                                       # Metni alır.
soup.head                                               # Head içeriğini alır.
soup.body                                               # Body içeriğini alır. 
soup.h1                                                 # İlk h1 etiketini alır.
soup.find("h1")                                         # İlk h1 etiketini alır.
soup.find_all("h1")                                     # Bütün h1 etiketlerini alır.
soup.find_all("div")[0].ul.find_all("li")               # Bütün div etiketlerinden belirtilen ifadeyi alır.
soup.div.findCildren()                                  # Div' in tüm alt elemanlarını alır.
soup.div.findNextSibling()                              # İlk div' den sonraki div' i alır.
soup.div.findPreviousSibling()                          # Div' den önceki div' e gider.