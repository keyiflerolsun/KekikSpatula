from KekikSpatula import Ezan

vakit = Ezan("Çanakkale")

print(vakit.veri)
"""
json verisi döndürür

{'kaynak': 'sabah.com.tr', 'veri': [{'il': 'Canakkale', 'imsak': '06:37', 'gunes': '08:05', 'ogle': '13:07', 'ikindi': '15:36', 'aksam': '17:58', 'yatsi': '19:21'}]}
"""

print(vakit.nesne.ogle)
"""
json verisini python nesnesine dönüştürür.

13:07
"""


print(vakit.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "sabah.com.tr",
  "veri": [
    {
      "il": "Canakkale",
      "imsak": "06:37",
      "gunes": "08:05",
      "ogle": "13:07",
      "ikindi": "15:36",
      "aksam": "17:58",
      "yatsi": "19:21"
    }
  ]
}
"""

print(vakit.tablo())
"""
tabulate verisi döndürür.

+-----------+---------+---------+--------+----------+---------+---------+
| il        | imsak   | gunes   | ogle   | ikindi   | aksam   | yatsi   |
|-----------+---------+---------+--------+----------+---------+---------|
| Canakkale | 06:37   | 08:05   | 13:07  | 15:36    | 17:58   | 19:21   |
+-----------+---------+---------+--------+----------+---------+---------+
"""

print(vakit.anahtarlar)
"""
kullanılan anahtar listesini döndürür.

['il', 'imsak', 'gunes', 'ogle', 'ikindi', 'aksam', 'yatsi']
"""