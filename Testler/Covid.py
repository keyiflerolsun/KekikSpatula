from KekikSpatula import Covid

covid = Covid()

print(covid.dunya_geneli)
"""
json verisi döndürür

{'kaynak': 'corona.cbddo.gov.tr', 'veri': {'vaka_sayisi': 280768392, 'olum_sayisi': 5404329, 'iyilesen_sayisi': 131473367}}
"""

print(covid.veri)
"""
json verisi döndürür

{'kaynak': 'interaktif.trthaber.com', 'veri': [{'ulke': 'USA', 'ulke_bayragi': 'https://disease.sh/assets/img/flags/us.png', 'ulke_nufusu': 333881850, 'aktif_hasta': 11450157, 'vaka_sayisi': 53357090, 'bugunki_vaka_sayisi': 75822, 'olum_sayisi': 838123, 'bugunki_olum_sayisi': 109, 'iyilesen_sayisi': 41068810, 'bugunki_iyilesen_sayisi': 17552, 'ulke_harita_konum': '38,-97'}, ... ]}
"""

for tek in covid.nesne:
  print(tek.ulke)
"""
json verisini python nesnesine dönüştürür.

USA
India
Brazil
UK
Russia
Turkey
France
Germany
...
"""

print(covid.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  'kaynak': 'interaktif.trthaber.com',
  'veri' : [
    {
      "ulke": "USA",
      "ulke_bayragi": "https://disease.sh/assets/img/flags/us.png",
      "ulke_nufusu": 333881850,
      "aktif_hasta": 11448173,
      "vaka_sayisi": 53349101,
      "bugunki_vaka_sayisi": 71811,
      "olum_sayisi": 838094,
      "bugunki_olum_sayisi": 91,
      "iyilesen_sayisi": 41062834,
      "bugunki_iyilesen_sayisi": 16030,
      "ulke_harita_konum": "38,-97"
    },
    ...
  ]
}
"""

print(covid.tablo())
"""
tabulate verisi döndürür.

+----------+-----------------------------------------  -+---------------+---------------+---------------+-----------------------+---------------+-----------------------+-------------------+---------------------------+---------------------+
| ulke     | ulke_bayragi                               |   ulke_nufusu |   aktif_hasta |   vaka_sayisi |   bugunki_vaka_sayisi |   olum_sayisi |   bugunki_olum_sayisi |   iyilesen_sayisi |   bugunki_iyilesen_sayisi | ulke_harita_konum   |
|----------+------------------------------------- ------+---------------+---------------+---------------+------------------ ----+---------------+-----------------------+-------------------+---------------------------+-------------------- |
| USA      | https://disease.sh/assets/img/flags/us.png |     333881850 |      11450157 |      53357090 |                 75822 |        838123 |                   109 |          41068810 |                     17552 | 38,-97              |
| India    | https://disease.sh/assets/img/flags/in.png |    1400124431 |         81728 |      34799241 |                  5908 |        480018 |                    21 |          34237495 |                      7141 | 20,77               |
| Brazil   | https://disease.sh/assets/img/flags/br.png |     214800545 |        206634 |      22239436 |                     0 |        618484 |                     0 |          21414318 |                         0 | -10,-55             |
| UK       | https://disease.sh/assets/img/flags/gb.png |      68415009 |       2100619 |      12209991 |                 98515 |        148003 |                   143 |           9961369 |                         0 | 54,-2               |
| Russia   | https://disease.sh/assets/img/flags/ru.png |     146027312 |        816589 |      10415230 |                 23210 |        305155 |                   937 |           9293486 |                     33715 | 60,100              |
| Turkey   | https://disease.sh/assets/img/flags/tr.png |      85684780 |        285742 |       9333223 |                 26099 |         81733 |                   157 |           8965748 |                     22024 | 39,35               |
| France   | https://disease.sh/assets/img/flags/fr.png |      65487807 |       1187496 |       9116068 |                     0 |        122642 |                     0 |           7805930 |                         0 | 46,2                |
| Germany  | https://disease.sh/assets/img/flags/de.png |      84181401 |        759217 |       7027008 |                 17374 |        111291 |                   210 |           6156500 |                     43000 | 51,9                |
| ....                                                                                                                                                                                                                                        |
+----------+-----------------------------------------  -+---------------+---------------+---------------+-----------------------+---------------+-----------------------+-------------------+---------------------------+---------------------+
"""

print(covid.anahtarlar)
"""
kullanılan anahtar listesini döndürür.

['ulke', 'ulke_bayragi', 'ulke_nufusu', 'aktif_hasta', 'vaka_sayisi', 'bugunki_vaka_sayisi', 'olum_sayisi', 'bugunki_olum_sayisi', 'iyilesen_sayisi', 'bugunki_iyilesen_sayisi', 'ulke_harita_konum']
"""