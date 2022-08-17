from KekikSpatula import UcuzUcak

def test_ucak():
  ucak = UcuzUcak()

  print(ucak.veri)
  """
  json verisi döndürür

  {'kaynak': 'bilet.ucuzaucak.net', 'veri': [{'bilet': 'İstanbul - Oslo - Brüksel - İstanbul Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '471 TL', 'tarih': 'Eylül', 'paylasim': 'Dün', 'link': 'https://bilet.ucuzaucak.net/f/istanbul-oslo-bruksel-istanbul-ucak-bileti--15ftiQ'}, {'bilet': 'Kayseri Viyana Uçak Bileti', 'yon': 'Tek Yön', 'fiyat': '160 TL', 'tarih': 'Temmuz, Haziran', 'paylasim': 'Dün', 'link': 'https://bilet.ucuzaucak.net/f/kayseri-viyana-ucak-bileti--15ftiP'}, {'bilet': 'İstanbul Telaviv Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '547 TL', 'tarih': 'Mayıs, Haziran', 'paylasim': 'Dün', 'link': 'https://bilet.ucuzaucak.net/f/istanbul-telaviv-ucak-bileti--15ftiO'}, {'bilet': 'Adana - Dusseldorf Uçak Bileti', 'yon': 'Tek Yön', 'fiyat': '160 TL', 'tarih': 'Haziran', 'paylasim': 'Dün', 'link': 'https://bilet.ucuzaucak.net/f/adana-dusseldorf-ucak-bileti--15ftiN'}, {'bilet': 'İstanbul Saraybosna Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '518 TL', 'tarih': 'Ağustos, Temmuz, Haziran, Mayıs', 'paylasim': 'Dün', 'link': 'https://bilet.ucuzaucak.net/f/istanbul-saraybosna-ucak-bileti--15ftiM'}, {'bilet': 'İstanbul-Amsterdam / Brüksel-İstanbul Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '347 TL', 'tarih': 'Eylül, Ekim', 'paylasim': 'Bu hafta', 'link': 'https://bilet.ucuzaucak.net/f/istanbul-amsterdam-bruksel-istanbul-ucak-bileti--15ftiL'}, {'bilet': 'İstanbul - Üsküp Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '500 TL', 'tarih': 'Ağustos, Temmuz, Haziran', 'paylasim': 'Bu hafta', 'link': 'https://bilet.ucuzaucak.net/f/istanbul-uskup-ucak-bileti--15ftiK'}, {'bilet': 'Ankara Kiev Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '477 TL', 'tarih': 'Ağustos, Eylül, Temmuz', 'paylasim': 'Bu hafta', 'link': 'https://bilet.ucuzaucak.net/f/ankara-kiev-ucak-bileti--15ftiJ'}, {'bilet': 'Konya Amsterdam Uçak Bileti', 'yon': 'Tek Yön', 'fiyat': '141 TL', 'tarih': 'Temmuz, Nisan, Haziran', 'paylasim': 'Bu hafta', 'link': 'https://bilet.ucuzaucak.net/f/konya-amsterdam-ucak-bileti--15ftiI'}, {'bilet': 'İstanbul - Milano Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '527 TL', 'tarih': 'Mayıs, Haziran', 'paylasim': 'Bu hafta', 'link': 'https://bilet.ucuzaucak.net/f/istanbul-milano-ucak-bileti--15ftiH'}, {'bilet': 'İstanbul Oslo Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '434 TL', 'tarih': 'Nisan, Eylül, Mayıs', 'paylasim': 'Bu hafta', 'link': 'https://bilet.ucuzaucak.net/f/istanbul-oslo-ucak-bileti--15ftiG'}, {'bilet': 'Brüksel - İstanbul Uçak Bileti', 'yon': 'Tek Yön', 'fiyat': '95 TL', 'tarih': 'Eylül, Ağustos', 'paylasim': 'Bu hafta', 'link': 'https://bilet.ucuzaucak.net/f/bruksel-istanbul-ucak-bileti--15ftiF'}, {'bilet': 'İstanbul Lviv Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat': '471 TL', 'tarih': 'Ekim, Nisan', 'paylasim': 'Bu hafta', 'link': 'https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15ftiE'}, {'bilet': 'İstanbul Diyarbakır Uçak Bileti', 'yon': 'Gidiş Dönüş', 'fiyat
  """

  for bilet in ucak.nesne:
    print(bilet.fiyat)
  """
  json verisini python nesnesine dönüştürür.

  471 TL
  160 TL
  547 TL
  160 TL
  518 TL
  347 TL
  500 TL
  477 TL
  141 TL
  527 TL
  434 TL
  95 TL
  471 TL
  200 TL
  200 TL
  """


  print(ucak.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

  {
    "kaynak": "bilet.ucuzaucak.net",
    "veri": [
      {
        "bilet": "İstanbul - Oslo - Brüksel - İstanbul Uçak Bileti",
        "yon": "Gidiş Dönüş",
        "fiyat": "471 TL",
        "tarih": "Eylül",
        "paylasim": "Dün",
        "link": "https://bilet.ucuzaucak.net/f/istanbul-oslo-bruksel-istanbul-ucak-bileti--15ftiQ"
      },
      {
        "bilet": "Kayseri Viyana Uçak Bileti",
        "yon": "Tek Yön",
        "fiyat": "160 TL",
  """

  print(ucak.tablo())
  """
  tabulate verisi döndürür.

  +---------------------------------------------------------+-------------------------+---------+----------------------------------------------------------------+------------+-----------------------------------------------------------------------------------------+
  | bilet                                                   | yon                     | fiyat   | tarih                                                          | paylasim   | link                                                                                    |
  |---------------------------------------------------------+-------------------------+---------+----------------------------------------------------------------+------------+-----------------------------------------------------------------------------------------|
  | İstanbul - Oslo - Brüksel - İstanbul Uçak Bileti        | Gidiş Dönüş             | 471 TL  | Eylül                                                          | Dün        | https://bilet.ucuzaucak.net/f/istanbul-oslo-bruksel-istanbul-ucak-bileti--15ftiQ        |
  | Kayseri Viyana Uçak Bileti                              | Tek Yön                 | 160 TL  | Temmuz, Haziran                                                | Dün        | https://bilet.ucuzaucak.net/f/kayseri-viyana-ucak-bileti--15ftiP                        |
  | İstanbul Telaviv Uçak Bileti                            | Gidiş Dönüş             | 547 TL  | Mayıs, Haziran                                                 | Dün        | https://bilet.ucuzaucak.net/f/istanbul-telaviv-ucak-bileti--15ftiO                      |
  | Adana - Dusseldorf Uçak Bileti                          | Tek Yön                 | 160 TL  | Haziran                                                        | Dün        | https://bilet.ucuzaucak.net/f/adana-dusseldorf-ucak-bileti--15ftiN                      |
  | İstanbul Saraybosna Uçak Bileti                         | Gidiş Dönüş             | 518 TL  | Ağustos, Temmuz, Haziran, Mayıs                                | Dün        | https://bilet.ucuzaucak.net/f/istanbul-saraybosna-ucak-bileti--15ftiM                   |
  | İstanbul-Amsterdam / Brüksel-İstanbul Uçak Bileti       | Gidiş Dönüş             | 347 TL  | Eylül, Ekim                                                    | Bu hafta   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam-bruksel-istanbul-ucak-bileti--15ftiL   |
  | İstanbul - Üsküp Uçak Bileti                            | Gidiş Dönüş             | 500 TL  | Ağustos, Temmuz, Haziran                                       | Bu hafta   | https://bilet.ucuzaucak.net/f/istanbul-uskup-ucak-bileti--15ftiK                        |
  | Ankara Kiev Uçak Bileti                                 | Gidiş Dönüş             | 477 TL  | Ağustos, Eylül, Temmuz                                         | Bu hafta   | https://bilet.ucuzaucak.net/f/ankara-kiev-ucak-bileti--15ftiJ                           |
  | Konya Amsterdam Uçak Bileti                             | Tek Yön                 | 141 TL  | Temmuz, Nisan, Haziran                                         | Bu hafta   | https://bilet.ucuzaucak.net/f/konya-amsterdam-ucak-bileti--15ftiI                       |
  | İstanbul - Milano Uçak Bileti                           | Gidiş Dönüş             | 527 TL  | Mayıs, Haziran                                                 | Bu hafta   | https://bilet.ucuzaucak.net/f/istanbul-milano-ucak-bileti--15ftiH                       |
  | İstanbul Oslo Uçak Bileti                               | Gidiş Dönüş             | 434 TL  | Nisan, Eylül, Mayıs                                            | Bu hafta   | https://bilet.ucuzaucak.net/f/istanbul-oslo-ucak-bileti--15ftiG                         |
  | Brüksel - İstanbul Uçak Bileti                          | Tek Yön                 | 95 TL   | Eylül, Ağustos                                                 | Bu hafta   | https://bilet.ucuzaucak.net/f/bruksel-istanbul-ucak-bileti--15ftiF                      |
  | İstanbul Lviv Uçak Bileti                               | Gidiş Dönüş             | 471 TL  | Ekim, Nisan                                                    | Bu hafta   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15ftiE                         |
  | İstanbul Diyarbakır Uçak Bileti                         | Gidiş Dönüş             | 200 TL  | Mart                                                           | Bu hafta   | https://bilet.ucuzaucak.net/f/istanbul-diyarbakir-ucak-bileti--15ftiD                   |
  | İstanbul Ordu Uçak Bileti                               | Gidiş Dönüş             | 200 TL  | Mart                                                           | Bu hafta   | https://bilet.ucuzaucak.net/f/istanbul-ordu-ucak-bileti--15ftiC                         |
  | İstanbul Van Uçak Bileti                                | Gidiş Dönüş             | 200 TL  | Mart, Şubat                                                    | Bu hafta   | https://bilet.ucuzaucak.net/f/istanbul-van-ucak-bileti--15ftiB                          |
  | İstanbul Nevşehir Uçak Bileti                           | Gidiş Dönüş             | 200 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-nevsehir-ucak-bileti--15ftiA                     |
  | İstanbul Trabzon Uçak Bileti                            | Gidiş Dönüş             | 200 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-trabzon-ucak-bileti--15fti9                      |
  | İstanbul Adana Uçak Bileti                              | Gidiş Dönüş             | 200 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-adana-ucak-bileti--15fti8                        |
  | İstanbul Gaziantep Uçak Bileti                          | Gidiş Dönüş             | 200 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-gaziantep-ucak-bileti--15fti7                    |
  | İstanbul Mardin Uçak Bileti                             | Gidiş Dönüş             | 200 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-mardin-ucak-bileti--15fti6                       |
  | İstanbul - Hatay Uçak Bileti                            | Gidiş Dönüş             | 200 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-hatay-ucak-bileti--15fti5                        |
  | Adana - Köln Uçak Bileti                                | Gidiş Dönüş             | 656 TL  | Haziran, Mayıs                                                 | Çok oldu   | https://bilet.ucuzaucak.net/f/adana-koln-ucak-bileti--15fti4                            |
  | İstanbul Odessa Uçak Bileti                             | Gidiş Dönüş             | 410 TL  | Ocak, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-odessa-ucak-bileti--15fti2                       |
  | İstanbul Lviv Uçak Bileti                               | Gidiş Dönüş             | 365 TL  | Ocak, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15fti1                         |
  | İstanbul - Saraybosna Uçak Bileti                       | Gidiş Dönüş             | 499 TL  | Nisan, Mayıs                                                   | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-saraybosna-ucak-bileti--15fti0                   |
  | İstanbul Lviv Uçak Bileti                               | Gidiş Dönüş             | 355 TL  | Nisan, Mayıs, Mart                                             | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15fthz                         |
  | İstanbul Lviv Uçak Bileti                               | Gidiş Dönüş             | 577 TL  | Nisan, Mayıs                                                   | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15fthy                         |
  | İstanbul - Moskova Uçak Bileti                          | Gidiş Dönüş             | 588 TL  | Ağustos                                                        | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-moskova-ucak-bileti--15fthx                      |
  | İstanbul - Amsterdam / Eindhoven - İstanbul Uçak Bileti | Gidiş Dönüş             | 483 TL  | Mayıs, Eylül                                                   | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam-eindhoven-istanbul-ucak-bileti--15fthw |
  | Brüksel - İstanbul Uçak Bileti                          | Tek Yön                 | 95 TL   | Nisan, Mayıs, Ağustos                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/bruksel-istanbul-ucak-bileti--15fthv                      |
  | Dalaman - Tel Aviv Uçak Bileti                          | Gidiş Dönüş             | 436 TL  | Haziran, Mayıs                                                 | Çok oldu   | https://bilet.ucuzaucak.net/f/dalaman-tel-aviv-ucak-bileti--15fthu                      |
  | Adana - Dusseldorf Uçak Bileti                          | Tek Yön                 | 161 TL  | Haziran, Mayıs, Temmuz                                         | Çok oldu   | https://bilet.ucuzaucak.net/f/adana-dusseldorf-ucak-bileti--15ftht                      |
  | Konya - Kopenhag Uçak Bileti                            | Gidiş Dönüş             | 434 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/konya-kopenhag-ucak-bileti--15fths                        |
  | İstanbul - Amsterdam / Eindhoven - İstanbul Uçak Bileti | Gidiş Dönüş             | 474 TL  | Haziran, Mayıs                                                 | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam-eindhoven-istanbul-ucak-bileti--15fthr |
  | İstanbul Zaporijya Uçak Bileti                          | Gidiş Dönüş             | 468 TL  | Temmuz, Ağustos, Haziran, Mayıs                                | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-zaporijya-ucak-bileti--15fthq                    |
  | İstanbul-Paris/ Brüksel-İstanbul Uçak Bileti            | Gidiş Dönüş             | 350 TL  | Mayıs                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-paris-bruksel-istanbul-ucak-bileti--15fthp       |
  | İstanbul - Lviv Uçak Bileti                             | Gidiş Dönüş             | 486 TL  | Mart, Eylül, Temmuz, Ağustos, Haziran, Mayıs, Nisan            | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15ftho                         |
  | İstanbul-Amsterdam / Brüksel-İstanbul Uçak Bileti       | Gidiş Dönüş             | 350 TL  | Haziran, Mayıs, Nisan                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam-bruksel-istanbul-ucak-bileti--15fthn   |
  | İstanbul Madrid/ Barselona-İstanbul Uçak Bileti         | Gidiş Dönüş             | 548 TL  | Mayıs, Nisan                                                   | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-madrid-barselona-istanbul-ucak-bileti--15fthm    |
  | İstanbul Brüksel Uçak Bileti                            | Gidiş Dönüş             | 345 TL  | Mayıs, Nisan, Eylül, Temmuz, Ağustos, Haziran                  | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-bruksel-ucak-bileti--15fthl                      |
  | Ankara Kiev Uçak Bileti                                 | Gidiş Dönüş             | 333 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/ankara-kiev-ucak-bileti--15fthk                           |
  | İstanbul Amsterdam Uçak Bileti                          | Gidiş Dönüş             | 436 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam-ucak-bileti--15fthj                    |
  | İstanbul Brüksel Uçak Bileti                            | Gidiş Dönüş             | 188 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-bruksel-ucak-bileti--15fthi                      |
  | İstanbul Basel Uçak Bileti                              | Gidiş Dönüş             | 350 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-basel-ucak-bileti--15fthh                        |
  | İstanbul Bükreş Uçak Bileti                             | Gidiş Dönüş             | 369 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-bukres-ucak-bileti--15fthg                       |
  | İstanbul Milano Uçak Bileti                             | Gidiş Dönüş             | 375 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-milano-ucak-bileti--15fthf                       |
  | İstanbul Prag Uçak Bileti                               | Gidiş Dönüş             | 375 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-prag-ucak-bileti--15fthe                         |
  | İstanbul Madrid Uçak Bileti                             | Gidiş Dönüş             | 411 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-madrid-ucak-bileti--15fthd                       |
  | İstanbul Lviv Uçak Bileti                               | Gidiş Dönüş             | 323 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15fthc                         |
  | Ankara Kiev Uçak Bileti                                 | Gidiş Dönüş             | 418 TL  | Aralık, Mart, Kasım, Ocak, Şubat                               | Çok oldu   | https://bilet.ucuzaucak.net/f/ankara-kiev-ucak-bileti--15fthb                           |
  | İstanbul Lviv Uçak Bileti                               | Gidiş Dönüş             | 416 TL  | Ocak, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15ftha                         |
  | İstanbul Amsterdam Uçak Bileti                          | Gidiş Dönüş             | 521 TL  | Ocak, Aralık, Şubat, Mart, Kasım                               | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam-ucak-bileti--15fthZ                    |
  | İstanbul Lübliyana Uçak Bileti                          | Gidiş Dönüş             | 470 TL  | Eylül, Ocak, Aralık, Şubat, Mart, Kasım, Temmuz, Ağustos, Ekim | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lubliyana-ucak-bileti--15fthY                    |
  | İstanbul Zagreb Uçak Bileti                             | Gidiş Dönüş             | 462 TL  | Eylül, Ocak, Aralık, Şubat, Mart, Kasım, Temmuz, Ağustos, Ekim | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-zagreb-ucak-bileti--15fthX                       |
  | Nürnberg İzmir Uçak Bileti                              | Tek Yön                 | 208 TL  | Temmuz                                                         | Çok oldu   | https://bilet.ucuzaucak.net/f/nurnberg-izmir-ucak-bileti--15fthW                        |
  | Berlin İzmir Uçak Bileti                                | Tek Yön                 | 130 TL  | Temmuz                                                         | Çok oldu   | https://bilet.ucuzaucak.net/f/berlin-izmir-ucak-bileti--15fthV                          |
  | İstanbul Amsterdam Uçak Bileti                          | Gidiş Dönüş             | 512 TL  | Ocak, Aralık, Şubat, Mart, Kasım                               | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam-ucak-bileti--15fthU                    |
  | İstanbul Lviv Uçak Bileti                               | Gidiş Dönüş             | 410 TL  | Ocak, Aralık, Şubat                                            | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15fthT                         |
  | Antalya Londra Uçak Bileti                              | Gidiş Dönüş             | 276 TL  | Ocak, Aralık                                                   | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-londra-ucak-bileti--15fthS                        |
  | Antalya Londra Uçak Bileti                              | Gidiş Dönüş             | 369 TL  | Eylül                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-londra-ucak-bileti--15fthR                        |
  | Antalya Manchester Uçak Bileti                          | Gidiş Dönüş             | 402 TL  | Ocak                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-manchester-ucak-bileti--15fthO                    |
  | İzmir Londra Uçak Bileti                                | Tek Yön                 | 164 TL  | Temmuz                                                         | Çok oldu   | https://bilet.ucuzaucak.net/f/izmir-londra-ucak-bileti--15fthN                          |
  | İstanbul Zaporijya Uçak Bileti                          | Gidiş Dönüş             | 411 TL  | Mart, Ocak, Kasım, Aralık, Şubat                               | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-zaporijya-ucak-bileti--15fthM                    |
  | İstanbul Kharkiv Uçak Bileti                            | Gidiş Dönüş             | 410 TL  | Mart, Ocak, Kasım, Aralık, Şubat                               | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-kharkiv-ucak-bileti--15fthL                      |
  | Ankara Kiev Uçak Bileti                                 | Gidiş Dönüş             | 413 TL  | Ocak, Kasım, Aralık, Şubat                                     | Çok oldu   | https://bilet.ucuzaucak.net/f/ankara-kiev-ucak-bileti--15fthK                           |
  | İstanbul Lviv Uçak Bileti                               | Gidiş Dönüş             | 412 TL  | Ocak, Kasım, Aralık, Şubat                                     | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-lviv-ucak-bileti--15fthJ                         |
  | İstanbul - Konya                                        | Gidiş Dönüş Uçak Bileti | 130 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-konya--15fthI                                    |
  | İstanbul - Amsterdam                                    | Gidiş Dönüş Uçak Bileti | 460 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam--15fthH                                |
  | İstanbul - Nevşehir                                     | Gidiş Dönüş Uçak Bileti | 162 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-nevsehir--15fthG                                 |
  | Ankara - Bursa                                          | Gidiş Dönüş Uçak Bileti | 130 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/ankara-bursa--15fthF                                      |
  | İstanbul - Denizli                                      | Gidiş Dönüş Uçak Bileti | 130 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-denizli--15fthE                                  |
  | İstanbul - İzmir                                        | Gidiş Dönüş Uçak Bileti | 130 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-izmir--15fthD                                    |
  | Ankara - Bakü                                           | Gidiş Dönüş Uçak Bileti | 383 TL  | Mayıs, Nisan                                                   | Çok oldu   | https://bilet.ucuzaucak.net/f/ankara-baku--15fthC                                       |
  | İstanbul - Tiflis                                       | Gidiş Dönüş Uçak Bileti | 198 TL  | Mayıs, Nisan                                                   | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-tiflis--15fthB                                   |
  | Helsinki - İstanbul                                     | Tek Yön Uçak Bileti     | 126 TL  | Eylül, Ağustos, Ekim                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/helsinki-istanbul--15fthA                                 |
  | İstanbul- Dusseldorf / Köln - İstanbul                  | Gidiş Dönüş Uçak Bileti | 392 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-dusseldorf-koln-istanbul--15fth9                 |
  | İstanbul - Eindhoven                                    | Gidiş Dönüş Uçak Bileti | 358 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-eindhoven--15fth8                                |
  | İstanbul - Brüksel                                      | Gidiş Dönüş Uçak Bileti | 389 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-bruksel--15fth7                                  |
  | Ankara - Stockholm                                      | Gidiş Dönüş Uçak Bileti | 471 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/ankara-stockholm--15fth6                                  |
  | İstanbul - Barcelona                                    | Gidiş Dönüş Uçak Bileti | 559 TL  | Ekim, Mayıs, Nisan                                             | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-barcelona--15fth5                                |
  | Dalaman - Viyana                                        | Gidiş Dönüş Uçak Bileti | 133 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/dalaman-viyana--15fth4                                    |
  | Bodrum - Viyana                                         | Gidiş Dönüş Uçak Bileti | 133 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/bodrum-viyana--15fth3                                     |
  | Antalya - Viyana                                        | Gidiş Dönüş Uçak Bileti | 133 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-viyana--15fth2                                    |
  | İstanbul - Tiflis                                       | Gidiş Dönüş Uçak Bileti | 585 TL  | Mayıs, Haziran, Nisan                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-tiflis--15fth1                                   |
  | İstanbul - Bakü                                         | Gidiş Dönüş Uçak Bileti | 674 TL  | Mayıs, Haziran, Nisan                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-baku--15fth0                                     |
  | İstanbul - Kuveyt                                       | Gidiş Dönüş Uçak Bileti | 380 TL  | Temmuz, Ağustos, Mayıs, Haziran, Nisan                         | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-kuveyt--15ftgz                                   |
  | İstanbul - Köln                                         | Gidiş Dönüş Uçak Bileti | 436 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-koln--15ftgy                                     |
  | İstanbul - Zaporijya                                    | Gidiş Dönüş Uçak Bileti | 372 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-zaporijya--15ftgx                                |
  | İstanbul - Prag                                         | Gidiş Dönüş Uçak Bileti | 423 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-prag--15ftgw                                     |
  | Münih -Antalya                                          | Tek Yön Uçak Bileti     | 79 TL   | Ekim                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/munih-antalya--15ftgv                                     |
  | Frankfurt - Kayseri                                     | Tek Yön Uçak Bileti     | 66 TL   | Ekim                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/frankfurt-kayseri--15ftgu                                 |
  | Frankfurt - Alanya                                      | Tek Yön Uçak Bileti     | 39 TL   | Ekim                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/frankfurt-alanya--15ftgt                                  |
  | İstanbul - Venedik                                      | Gidiş Dönüş Uçak Bileti | 449 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-venedik--15ftgs                                  |
  | Antalya - Münih                                         | Gidiş Dönüş Uçak Bileti | 358 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-munih--15ftgr                                     |
  | İstanbul - Bologna                                      | Gidiş Dönüş Uçak Bileti | 405 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-bologna--15ftgq                                  |
  | Bodrum - Viyana                                         | Gidiş Dönüş Uçak Bileti | 66 TL   | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/bodrum-viyana--15ftgp                                     |
  | Antalya-Viyana                                          | Gidiş Dönüş Uçak Bileti | 66 TL   | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-viyana--15ftgo                                    |
  | Dalaman - Viyana                                        | Gidiş Dönüş Uçak Bileti | 66 TL   | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/dalaman-viyana--15ftgn                                    |
  | Antalya-Köln-Roma-Viyana-Antalya                        | Gidiş Dönüş Uçak Bileti | 480 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-koln-roma-viyana-antalya--15ftgm                  |
  | İst- Roma- Viyana-İst                                   | Gidiş Dönüş Uçak Bileti | 530 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/ist-roma-viyana-ist--15ftgl                               |
  | Antalya - Hannover                                      | Gidiş Dönüş Uçak Bileti | 401 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-hannover--15ftgk                                  |
  | Antalya - Münih                                         | Gidiş Dönüş Uçak Bileti | 368 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-munih--15ftgj                                     |
  | İstanbul - Kopenhag                                     | Gidiş Dönüş Uçak Bileti | 422 TL  | Mayıs                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-kopenhag--15ftgi                                 |
  | İstanbul - Berlin                                       | Gidiş Dönüş Uçak Bileti | 442 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-berlin--15ftgh                                   |
  | Dalaman - Viyana                                        | Gidiş Dönüş Uçak Bileti | 172 TL  | Nisan, Mayıs                                                   | Çok oldu   | https://bilet.ucuzaucak.net/f/dalaman-viyana--15ftgg                                    |
  | İzmir - Atina                                           | Gidiş Dönüş Uçak Bileti | 434 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/izmir-atina--15ftgf                                       |
  | İstanbul - Tiran                                        | Gidiş Dönüş Uçak Bileti | 447 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-tiran--15ftge                                    |
  | İstanbul - Amsterdam                                    | Gidiş Dönüş Uçak Bileti | 440 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam--15ftgd                                |
  | Bodrum - Viyana                                         | Gidiş Dönüş Uçak Bileti | 172 TL  | Mayıs                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/bodrum-viyana--15ftgc                                     |
  | İstanbul - Berlin                                       | Gidiş Dönüş Uçak Bileti | 442 TL  | Şubat, Mart                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-berlin--15ftgb                                   |
  | İstanbul - Cenevre                                      | Gidiş Dönüş Uçak Bileti | 437 TL  | Mayıs                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-cenevre--15ftga                                  |
  | İstanbul - Tiflis                                       | Gidiş Dönüş Uçak Bileti | 459 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-tiflis--15ftgZ                                   |
  | 3 Şehirli Avrupa Turu                                   | Gidiş Dönüş Uçak Bileti | 471 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/3-sehirli-avrupa-turu--15ftgY                             |
  | Ankara - Kiev                                           | Gidiş Dönüş Uçak Bileti | 458 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/ankara-kiev--15ftgX                                       |
  | İstanbul - Saraybosna                                   | Gidiş Dönüş Uçak Bileti | 469 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-saraybosna--15ftgW                               |
  | İstanbul - Amsterdam                                    | Gidiş Dönüş Uçak Bileti | 441 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-amsterdam--15ftgV                                |
  | İstanbul - Üsküp                                        | Gidiş Dönüş Uçak Bileti | 391 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-uskup--15ftgU                                    |
  | İstanbul - Bükreş                                       | Gidiş Dönüş Uçak Bileti | 405 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-bukres--15ftgT                                   |
  | İstanbul - Milano                                       | Gidiş Dönüş Uçak Bileti | 411 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-milano--15ftgS                                   |
  | İstanbul - Bologna                                      | Gidiş Dönüş Uçak Bileti | 405 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-bologna--15ftgR                                  |
  | Bodrum - Viyana                                         | Gidiş Dönüş Uçak Bileti | 236 TL  | Mayıs                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/bodrum-viyana--15ftgQ                                     |
  | Dalaman - Bratislava                                    | Gidiş Dönüş Uçak Bileti | 309 TL  | Haziran                                                        | Çok oldu   | https://bilet.ucuzaucak.net/f/dalaman-bratislava--15ftgP                                |
  | Antalya - Viyana                                        | Gidiş Dönüş Uçak Bileti | 173 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/antalya-viyana--15ftgO                                    |
  | İstanbul-Budapeşte / Prag-İstanbul                      | Gidiş Dönüş Uçak bileti | 431 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-budapeste-prag-istanbul--15ftgN                  |
  | İstanbul - Münih - Köln - İstanbul                      | Gidiş Dönüş Uçak Bileti | 383 TL  | Mart                                                           | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-munih-koln-istanbul--15ftgM                      |
  | İstanbul - Venedik                                      | Gidiş Dönüş Uçak Bileti | 447 TL  | Mart, Şubat                                                    | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-venedik--15ftgL                                  |
  | İstanbul - Münih                                        | Gidiş Dönüş Uçak Bileti | 569 TL  | Mayıs                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-munih--15ftgK                                    |
  | İstanbul - Samsun                                       | Gidiş Dönüş Uçak bileti | 200 TL  | Nisan                                                          | Çok oldu   | https://bilet.ucuzaucak.net/f/istanbul-samsun--15ftgJ                                   |
  +---------------------------------------------------------+-------------------------+---------+----------------------------------------------------------------+------------+-----------------------------------------------------------------------------------------+
  """

  print(ucak.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['bilet', 'yon', 'fiyat', 'tarih', 'paylasim', 'link']
  """