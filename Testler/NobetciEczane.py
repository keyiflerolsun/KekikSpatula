from KekikSpatula import NobetciEczane

eczane = NobetciEczane("Çanakkale", "Merkez")

print(eczane.veri)
"""
json verisi döndürür

{'kaynak': 'eczaneler.gen.tr', 'veri': [{'ad': 'Derya Eczanesi', 'mahalle': None, 'adres': 'İsmetpaşa Mahallesi, Hasan Mevsuf Sokak, No:50/A Merkez / Çanakkale', 'tarif': 'Emniyet Müdürlüğünden Eski Otagara Çıkan Sokak', 'telefon': '0 (286) 814-25-51'}, {'ad': 'Ege Eczanesi', 'mahalle': None, 'adres': 'Cevatpaşa Mahallesi, İkinci Çanakçılar Sokak, Yıldız Apt. No:21 Merkez / Çanakkale', 'tarif': 'Eski Vergi Dairesi Arka Sokağı', 'telefon': '0 (286) 212-45-65'}, {'ad': 'Evcim Eczanesi', 'mahalle': None, 'adres': 'Mehmet Akif Ersoy Yeni Devlet Hastanesi karşısı Merkez / Çanakkale', 'tarif': None, 'telefon': '0 (286) 213-80-39'}]}
"""

for eczane_nesnesi in eczane.nesne:
    print(eczane_nesnesi.ad)
"""
json verisini python nesnesine dönüştürür.

Derya Eczanesi
Ege Eczanesi
Evcim Eczanesi
"""


print(eczane.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "eczaneler.gen.tr",
  "veri": [
    {
      "ad": "Derya Eczanesi",
      "mahalle": null,
      "adres": "İsmetpaşa Mahallesi, Hasan Mevsuf Sokak, No:50/A Merkez / Çanakkale",
      "tarif": "Emniyet Müdürlüğünden Eski Otagara Çıkan Sokak",
      "telefon": "0 (286) 814-25-51"
    },
    {
      "ad": "Ege Eczanesi",
      "mahalle": null,
      "adres": "Cevatpaşa Mahallesi, İkinci Çanakçılar Sokak, Yıldız Apt. No:21 Merkez / Çanakkale",
      "tarif": "Eski Vergi Dairesi Arka Sokağı",
      "telefon": "0 (286) 212-45-65"
    },
    {
      "ad": "Evcim Eczanesi",
      "mahalle": null,
      "adres": "Mehmet Akif Ersoy Yeni Devlet Hastanesi karşısı Merkez / Çanakkale",
      "tarif": null,
      "telefon": "0 (286) 213-80-39"
    }
  ]
}
"""

print(eczane.tablo())
"""
tabulate verisi döndürür.

+----------------+-----------+------------------------------------------------------------------------------------+------------------------------------------------+-------------------+
| ad             | mahalle   | adres                                                                              | tarif                                          | telefon           |
|----------------+-----------+------------------------------------------------------------------------------------+------------------------------------------------+-------------------|
| Derya Eczanesi |           | İsmetpaşa Mahallesi, Hasan Mevsuf Sokak, No:50/A Merkez / Çanakkale                | Emniyet Müdürlüğünden Eski Otagara Çıkan Sokak | 0 (286) 814-25-51 |
| Ege Eczanesi   |           | Cevatpaşa Mahallesi, İkinci Çanakçılar Sokak, Yıldız Apt. No:21 Merkez / Çanakkale | Eski Vergi Dairesi Arka Sokağı                 | 0 (286) 212-45-65 |
| Evcim Eczanesi |           | Mehmet Akif Ersoy Yeni Devlet Hastanesi karşısı Merkez / Çanakkale                 |                                                | 0 (286) 213-80-39 |
+----------------+-----------+------------------------------------------------------------------------------------+------------------------------------------------+-------------------+
"""

print(eczane.anahtarlar)
"""
kullanılan anahtar listesini döndürür.

['ad', 'mahalle', 'adres', 'tarif', 'telefon']
"""