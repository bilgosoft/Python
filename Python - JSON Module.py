# JSON Module : Farklı diller arasında veri iletişimi sağlayan bir modüldür.

import json

# JSON DATA TO DICTIONARY
json_Data = '{1 : "Bilgo", 2 : "Soft"}' # Json data oluşturduk.
dictData = json.loads(json_Data)        # Json datayı dictionary yapısına çevirdik.
print(dictData)                         # Dictionary yapıyı ekrana yazdırdık.
print(dictData[1])                      # Dictionary yapıdan istediğimiz değere ulaştık.

# DICTIONARY TO JSON DATA
Dictionary_Data = {1 : "Bilgo", 2 : "Soft"}
jsonData = json.dumps(Dictionary_Data)  # Json datayı dictionary yapısına çevirdik.
print(jsonData)                         # Dictionary yapıyı ekrana yazdırdık.         