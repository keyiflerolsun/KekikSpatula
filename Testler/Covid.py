from KekikSpatula import Covid

covid = Covid()

print(covid.veri)
"""
json verisi döndürür

{'kaynak': 'saglik.gov.tr', 'veri': [{'tarih': '25.11.2020', 'gunluk_test': '164.547', 'gunluk_vaka': '6.814', 'gunluk_vefat': '168', 'gunluk_iyilesen': '3.911', 'toplam_test': '17.733.520', 'toplam_vaka': '467.730', 'toplam_vefat': '12.840', 'toplam_iyilesen': '385.480', 'toplam_yogun_bakim': '', 'toplam_entube': '', 'hastalarda_zaturre_oran': '3,4', 'agir_hasta_sayisi': '4.641', 'yatak_doluluk_orani': '54,7', 'eriskin_yogun_bakim_doluluk_orani': '71,3', 'ventilator_doluluk_orani': '39,2', 'ortalama_filyasyon_suresi': '', 'ortalama_temasli_tespit_suresi': '11', 'filyasyon_orani': '99,8'}]}
"""

print(covid.nesne.gunluk_vefat)
"""
json verisini python nesnesine dönüştürür.

168
"""


print(covid.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "saglik.gov.tr",
  "veri": [
    {
      "tarih": "25.11.2020",
      "gunluk_test": "164.547",
      "gunluk_vaka": "6.814",
      "gunluk_vefat": "168",
      "gunluk_iyilesen": "3.911",
      "toplam_test": "17.733.520",
      "toplam_vaka": "467.730",
      "toplam_vefat": "12.840",
      "toplam_iyilesen": "385.480",
      "toplam_yogun_bakim": "",
      "toplam_entube": "",
      "hastalarda_zaturre_oran": "3,4",
      "agir_hasta_sayisi": "4.641",
      "yatak_doluluk_orani": "54,7",
      "eriskin_yogun_bakim_doluluk_orani": "71,3",
      "ventilator_doluluk_orani": "39,2",
      "ortalama_filyasyon_suresi": "",
      "ortalama_temasli_tespit_suresi": "11",
      "filyasyon_orani": "99,8"
    }
  ]
}
"""

print(covid.tablo())
"""
tabulate verisi döndürür.

+------------+---------------+---------------+----------------+-------------------+---------------+---------------+----------------+-------------------+----------------------+-----------------+---------------------------+---------------------+-----------------------+-------------------------------------+----------------------------+-----------------------------+----------------------------------+-------------------+
| tarih      |   gunluk_test |   gunluk_vaka |   gunluk_vefat |   gunluk_iyilesen | toplam_test   |   toplam_vaka |   toplam_vefat |   toplam_iyilesen | toplam_yogun_bakim   | toplam_entube   | hastalarda_zaturre_oran   |   agir_hasta_sayisi | yatak_doluluk_orani   | eriskin_yogun_bakim_doluluk_orani   | ventilator_doluluk_orani   | ortalama_filyasyon_suresi   |   ortalama_temasli_tespit_suresi | filyasyon_orani   |
|------------+---------------+---------------+----------------+-------------------+---------------+---------------+----------------+-------------------+----------------------+-----------------+---------------------------+---------------------+-----------------------+-------------------------------------+----------------------------+-----------------------------+----------------------------------+-------------------|
| 25.11.2020 |       164.547 |         6.814 |            168 |             3.911 | 17.733.520    |        467.73 |          12.84 |            385.48 |                      |                 | 3,4                       |               4.641 | 54,7                  | 71,3                                | 39,2                       |                             |                               11 | 99,8              |
+------------+---------------+---------------+----------------+-------------------+---------------+---------------+----------------+-------------------+----------------------+-----------------+---------------------------+---------------------+-----------------------+-------------------------------------+----------------------------+-----------------------------+----------------------------------+-------------------+
"""

print(covid.anahtarlar)
"""
kullanılan anahtar listesini döndürür.

['tarih', 'gunluk_test', 'gunluk_vaka', 'gunluk_vefat', 'gunluk_iyilesen', 'toplam_test', 'toplam_vaka', 'toplam_vefat', 'toplam_iyilesen', 'toplam_yogun_bakim', 'toplam_entube', 'hastalarda_zaturre_oran', 'agir_hasta_sayisi', 'yatak_doluluk_orani', 'eriskin_yogun_bakim_doluluk_orani', 'ventilator_doluluk_orani', 'ortalama_filyasyon_suresi', 'ortalama_temasli_tespit_suresi', 'filyasyon_orani']
"""