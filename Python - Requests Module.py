# REQUESTS : Site ile bağlantı oluşturur.

import requests

# 1. Yöntem

url = "https://www.bilgosoft.com/"
bilgoSoft = requests.get(url)       # Sayfa ile bağlantı kurar.
bilgoSoft.status_code               # Sitenin verilerini çekip çekemeyeceğimizi söyler.
bilgoSoft.content                   # Sayfa kaynağına ulaştırır.

# 2. Yöntem (Bağlantı kurulamaz ise yapılacak yöntem)

# browser = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
# url = "https://www.bilgosoft.com/"
# bilgoSoft = requests.get(url, browser)    # Sayfa ile bağlantı kurar.
# bilgoSoft.status_code                     # Sitenin verilerini çekip çekemeyeceğimizi söyler.
# bilgoSoft.content                         # Sayfa kaynağına ulaştırır.