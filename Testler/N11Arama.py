from KekikSpatula import N11Arama

n11 = N11Arama("araba", 2)

print(n11.veri)
"""
json verisi döndürür

{'kaynak': 'n11.com', 'veri': [{'baslik': 'Maverick MV12810 Ion SC 1:18 RTR Uzaktan Kumandalı Araba', 'resim': 'https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/maverick-mv12810-ion-sc-118-rtr-uzaktan-kumandali-araba__1375401488493495.png', 'urun_linki': 'https://www.n11.com/urun/maverick-mv12810-ion-sc-118-rtr-uzaktan-kumandali-araba-2083803?magaza=starhobbyelektronik', 'urun_fiyatlari': {'eski_fiyati': None, 'yeni_fiyati': '1.424,22 TL', 'sepet_fiyati': '1.404,22 TL'}, 'urun_yıldız': 0.0, 'magaza_ismi': 'StarHobbyElektronik', 'magaza_linki': 'https://www.n11.com/magaza/starhobbyelektronik', 'magaza_puan_yuzdesi': '%100'}, ... ]}
"""

print(n11.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "n11.com",
  "veri": [
    {
      "baslik": "Maverick MV12810 Ion SC 1:18 RTR Uzaktan Kumandalı Araba",
      "resim": "https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/maverick-mv12810-ion-sc-118-rtr-uzaktan-kumandali-araba__1375401488493495.png",
      "urun_linki": "https://www.n11.com/urun/maverick-mv12810-ion-sc-118-rtr-uzaktan-kumandali-araba-2083803?magaza=starhobbyelektronik",
      "urun_fiyatlari": {
        "eski_fiyati": null,
        "yeni_fiyati": "1.424,22 TL",
        "sepet_fiyati": "1.404,22 TL"
      },
      "urun_yıldız": 0.0,
      "magaza_ismi": "StarHobbyElektronik",
      "magaza_linki": "https://www.n11.com/magaza/starhobbyelektronik",
      "magaza_puan_yuzdesi": "%100"
    },
    {
      "baslik": "Maverick MV12616 STRADA TC 1/10 RTR Uzaktan Kumandalı Araba",
      "resim": "https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/maverick-mv12616-strada-tc-110-rtr-uzaktan-kumandali-araba__1180095144512360.jpg",
      "urun_linki": "https://www.n11.com/urun/maverick-mv12616-strada-tc-110-rtr-uzaktan-kumandali-araba-2083834?magaza=starhobbyelektronik",        
      "urun_fiyatlari": {
        "eski_fiyati": null,
        "yeni_fiyati": "2.724,85 TL",
        "sepet_fiyati": "2.704,85 TL"
      },
      "urun_yıldız": 0.0,
      "magaza_ismi": "StarHobbyElektronik",
      "magaza_linki": "https://www.n11.com/magaza/starhobbyelektronik",
      "magaza_puan_yuzdesi": "%100"
    },
    {
      "baslik": "Hpi Racing RS4 Sport 3 Flux Ford GT Heritage Edition 1:10 RC Uzaktan Kumandalı Araba",
      "resim": "https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/hpi-racing-rs4-sport-3-flux-ford-gt-heritage-edition-110-rc-uzaktan-kumandali-araba__0190571906428214.jpg",
      "urun_linki": "https://www.n11.com/urun/hpi-racing-rs4-sport-3-flux-ford-gt-heritage-edition-110-rc-uzaktan-kumandali-araba-2083723?magaza=starhobbyelektronik",
      "urun_fiyatlari": {
        "eski_fiyati": null,
        "yeni_fiyati": "5.740,08 TL",
        "sepet_fiyati": "5.720,08 TL"
      },
      "urun_yıldız": 0.0,
      "magaza_ismi": "StarHobbyElektronik",
      "magaza_linki": "https://www.n11.com/magaza/starhobbyelektronik",
      "magaza_puan_yuzdesi": "%100"
    },
    {
      "baslik": "Hpi RS4 Sport 3 Drift Worthouse James Dean Nissan S15 Uzaktan Kumandalı Araba",
      "resim": "https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/hpi-rs4-sport-3-drift-worthouse-james-dean-nissan-s15-uzaktan-kumandali-araba__0241332329238047.jpg",
      "urun_linki": "https://www.n11.com/urun/hpi-rs4-sport-3-drift-worthouse-james-dean-nissan-s15-uzaktan-kumandali-araba-2083733?magaza=starhobbyelektronik",
      "urun_fiyatlari": {
        "eski_fiyati": null,
        "yeni_fiyati": "5.287,51 TL",
        "sepet_fiyati": "5.267,51 TL"
      },
      "urun_yıldız": 0.0,
      "magaza_ismi": "StarHobbyElektronik",
      "magaza_linki": "https://www.n11.com/magaza/starhobbyelektronik",
      "magaza_puan_yuzdesi": "%100"
    },
    {
      "baslik": "Wei Ya Toys Işıklı Müzikli Uzaktan Kumandalı Spor Araba Çok Renkli",
      "resim": "https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/wei-ya-toys-isikli-muzikli-uzaktan-kumandali-spor-araba-cok-renkli__1278638233819207.jpg",
      "urun_linki": "https://www.n11.com/urun/wei-ya-toys-isikli-muzikli-uzaktan-kumandali-spor-araba-cok-renkli-1965384?magaza=oyuncakbiziz",       
      "urun_fiyatlari": {
        "eski_fiyati": "576,03 TL",
        "yeni_fiyati": "525,94 TL",
        "sepet_fiyati": "505,94 TL"
      },
      "urun_yıldız": 0.0,
      "magaza_ismi": "Oyuncakbiziz",
      "magaza_linki": "https://www.n11.com/magaza/oyuncakbiziz",
      "magaza_puan_yuzdesi": "%100"
    },
    {
      "baslik": "Wei Ya Toys Işıklı Müzikli Uzaktan Kumandalı Spor Araba",
      "resim": "https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/wei-ya-toys-isikli-muzikli-uzaktan-kumandali-spor-araba__1558590714429230.png",
      "urun_linki": "https://www.n11.com/urun/wei-ya-toys-isikli-muzikli-uzaktan-kumandali-spor-araba-1965353?magaza=oyuncakbiziz",
      "urun_fiyatlari": {
        "eski_fiyati": "375,94 TL",
        "yeni_fiyati": "343,25 TL",
        "sepet_fiyati": "323,25 TL"
      },
      "urun_yıldız": 0.0,
      "magaza_ismi": "Oyuncakbiziz",
      "magaza_linki": "https://www.n11.com/magaza/oyuncakbiziz",
      "magaza_puan_yuzdesi": "%100"
    },
    {
      "baslik": "Hpi 115118 Crawler King RTR 4WD Rock Crawler Ford F150 SVT Uzaktan Kumandalı Araba",
      "resim": "https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/hpi-115118-crawler-king-rtr-4wd-rock-crawler-ford-f150-svt-uzaktan-kumandali-araba__0101702660650650.jpg",
      "urun_linki": "https://www.n11.com/urun/hpi-115118-crawler-king-rtr-4wd-rock-crawler-ford-f150-svt-uzaktan-kumandali-araba-2083795?magaza=starhobbyelektronik",
      "urun_fiyatlari": {
        "eski_fiyati": null,
        "yeni_fiyati": "4.721,35 TL",
        "sepet_fiyati": "4.701,35 TL"
      },
      "urun_yıldız": 0.0,
      "magaza_ismi": "StarHobbyElektronik",
      "magaza_linki": "https://www.n11.com/magaza/starhobbyelektronik",
      "magaza_puan_yuzdesi": "%100"
    },
    {
      "baslik": "Maverick MV12805 ION RX 1:18 Rtr Electric Uzaktan Kumandalı Rally Araba",
      "resim": "https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/maverick-mv12805-ion-rx-118-rtr-electric-uzaktan-kumandali-rally-araba__1461355753170960.jpg",
      "urun_linki": "https://www.n11.com/urun/maverick-mv12805-ion-rx-118-rtr-electric-uzaktan-kumandali-rally-araba-1927379?magaza=starhobbyelektronik",
      "urun_fiyatlari": {
        "eski_fiyati": null,
        "yeni_fiyati": "1.424,22 TL",
        "sepet_fiyati": "1.404,22 TL"
      },
      "urun_yıldız": 5.0,
      "magaza_ismi": "StarHobbyElektronik",
      "magaza_linki": "https://www.n11.com/magaza/starhobbyelektronik",
      "magaza_puan_yuzdesi": "%100"
    },
    ...
  ]
}
"""

print(n11.tablo())

"""
tabulate verisi döndürür.

+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------+---------------------+------------------------------------------------+-----------------------+
| baslik                                                                               | resim                                                                                                                                                                      | urun_linki                                                                                                                                      | urun_fiyatlari                                                                        |   urun_yıldız | magaza_ismi         | magaza_linki                                   | magaza_puan_yuzdesi   |
|--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------+---------------------+------------------------------------------------+-----------------------|
| Maverick MV12810 Ion SC 1:18 RTR Uzaktan Kumandalı Araba                             | https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/maverick-mv12810-ion-sc-118-rtr-uzaktan-kumandali-araba__1375401488493495.png                             | https://www.n11.com/urun/maverick-mv12810-ion-sc-118-rtr-uzaktan-kumandali-araba-2083803?magaza=starhobbyelektronik                             | {'eski_fiyati': None, 'yeni_fiyati': '1.424,22 TL', 'sepet_fiyati': '1.404,22 TL'}    |             0 | StarHobbyElektronik | https://www.n11.com/magaza/starhobbyelektronik | %100                  |
| Maverick MV12616 STRADA TC 1/10 RTR Uzaktan Kumandalı Araba                          | https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/maverick-mv12616-strada-tc-110-rtr-uzaktan-kumandali-araba__1180095144512360.jpg                          | https://www.n11.com/urun/maverick-mv12616-strada-tc-110-rtr-uzaktan-kumandali-araba-2083834?magaza=starhobbyelektronik                          | {'eski_fiyati': None, 'yeni_fiyati': '2.724,85 TL', 'sepet_fiyati': '2.704,85 TL'}    |             0 | StarHobbyElektronik | https://www.n11.com/magaza/starhobbyelektronik | %100                  |
| Hpi Racing RS4 Sport 3 Flux Ford GT Heritage Edition 1:10 RC Uzaktan Kumandalı Araba | https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/hpi-racing-rs4-sport-3-flux-ford-gt-heritage-edition-110-rc-uzaktan-kumandali-araba__0190571906428214.jpg | https://www.n11.com/urun/hpi-racing-rs4-sport-3-flux-ford-gt-heritage-edition-110-rc-uzaktan-kumandali-araba-2083723?magaza=starhobbyelektronik | {'eski_fiyati': None, 'yeni_fiyati': '5.740,08 TL', 'sepet_fiyati': '5.720,08 TL'}    |             0 | StarHobbyElektronik | https://www.n11.com/magaza/starhobbyelektronik | %100                  |
| Hpi RS4 Sport 3 Drift Worthouse James Dean Nissan S15 Uzaktan Kumandalı Araba        | https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/hpi-rs4-sport-3-drift-worthouse-james-dean-nissan-s15-uzaktan-kumandali-araba__0241332329238047.jpg       | https://www.n11.com/urun/hpi-rs4-sport-3-drift-worthouse-james-dean-nissan-s15-uzaktan-kumandali-araba-2083733?magaza=starhobbyelektronik       | {'eski_fiyati': None, 'yeni_fiyati': '5.287,51 TL', 'sepet_fiyati': '5.267,51 TL'}    |             0 | StarHobbyElektronik | https://www.n11.com/magaza/starhobbyelektronik | %100                  |
| Wei Ya Toys Işıklı Müzikli Uzaktan Kumandalı Spor Araba Çok Renkli                   | https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/wei-ya-toys-isikli-muzikli-uzaktan-kumandali-spor-araba-cok-renkli__1278638233819207.jpg                  | https://www.n11.com/urun/wei-ya-toys-isikli-muzikli-uzaktan-kumandali-spor-araba-cok-renkli-1965384?magaza=oyuncakbiziz                         | {'eski_fiyati': '576,03 TL', 'yeni_fiyati': '525,94 TL', 'sepet_fiyati': '505,94 TL'} |             0 | Oyuncakbiziz        | https://www.n11.com/magaza/oyuncakbiziz        | %100                  |
| Wei Ya Toys Işıklı Müzikli Uzaktan Kumandalı Spor Araba                              | https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/wei-ya-toys-isikli-muzikli-uzaktan-kumandali-spor-araba__1558590714429230.png                             | https://www.n11.com/urun/wei-ya-toys-isikli-muzikli-uzaktan-kumandali-spor-araba-1965353?magaza=oyuncakbiziz                                    | {'eski_fiyati': '375,94 TL', 'yeni_fiyati': '343,25 TL', 'sepet_fiyati': '323,25 TL'} |             0 | Oyuncakbiziz        | https://www.n11.com/magaza/oyuncakbiziz        | %100                  |
| Hpi 115118 Crawler King RTR 4WD Rock Crawler Ford F150 SVT Uzaktan Kumandalı Araba   | https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/hpi-115118-crawler-king-rtr-4wd-rock-crawler-ford-f150-svt-uzaktan-kumandali-araba__0101702660650650.jpg  | https://www.n11.com/urun/hpi-115118-crawler-king-rtr-4wd-rock-crawler-ford-f150-svt-uzaktan-kumandali-araba-2083795?magaza=starhobbyelektronik  | {'eski_fiyati': None, 'yeni_fiyati': '4.721,35 TL', 'sepet_fiyati': '4.701,35 TL'}    |             0 | StarHobbyElektronik | https://www.n11.com/magaza/starhobbyelektronik | %100                  |
| Maverick MV12805 ION RX 1:18 Rtr Electric Uzaktan Kumandalı Rally Araba              | https://n11scdn.akamaized.net/a1/140/kitap-muzik-film-oyun/araba/maverick-mv12805-ion-rx-118-rtr-electric-uzaktan-kumandali-rally-araba__1461355753170960.jpg              | https://www.n11.com/urun/maverick-mv12805-ion-rx-118-rtr-electric-uzaktan-kumandali-rally-araba-1927379?magaza=starhobbyelektronik              | {'eski_fiyati': None, 'yeni_fiyati': '1.424,22 TL', 'sepet_fiyati': '1.404,22 TL'}    |             5 | StarHobbyElektronik | https://www.n11.com/magaza/starhobbyelektronik | %100                  |
| ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------+---------------------+------------------------------------------------+-----------------------+
"""