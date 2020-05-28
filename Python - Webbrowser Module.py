# Webbworser : Belirtilen internet sayfasını açmayı sağlayan modüldür.

import webbrowser as web

url = "www.bilgosoft.com" # Bağlanılacak site adresi
new = 0 # 0 ise aynı, 1 ise farklı pencerede, 2 ise aynı pencerede farklı sekmede açılır. Default : 0
autoraise = True # Site ne durumda olursa olsun gider. Default : True

web.open(url, new, autoraise) # open : Web sayfamızı açan kod.
web.open_new(url) # Sadece url alır. Açılan sayfa mümkünse yeni pencerede değil ise yeni sekmede açılır.
web.open_new_tab(url) # Sayfayı yeni sekmede açar.

