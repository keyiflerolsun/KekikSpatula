from KekikSpatula import Covid

def test_covid():
  covid = Covid()

  print(covid.ulke("tr"))
  """
  istediğiniz ülkenin covid verisini döndürür

  {'ulke': 'Turkey', 'ulke_bayragi': 'https://disease.sh/assets/img/flags/tr.png', 'ulke_nufusu': 85687258, 'aktif_hasta': 285742, 'vaka_sayisi': 9333223, 'bugunki_vaka_sayisi': 0, 'olum_sayisi': 81733, 'bugunki_olum_sayisi': 0, 'iyilesen_sayisi': 8965748, 'bugunki_iyilesen_sayisi': 0, 'ulke_harita_konum': '39,35'}
  """

  print(covid.veri)
  """
  json verisi döndürür

  [{'ulke': 'Russia', 'ulke_bayragi': 'https://disease.sh/assets/img/flags/ru.png', 'ulke_nufusu': 146027482, 'aktif_hasta': 816589, 'vaka_sayisi': 10415230, 'bugunki_vaka_sayisi': 23210, 'olum_sayisi': 305155, 'bugunki_olum_sayisi': 937, 'iyilesen_sayisi': 9293486, 'bugunki_iyilesen_sayisi': 33715, 'ulke_harita_konum': '60,100'}, ....]
  """

  for veri in covid.nesne:
    print(veri.ulke)
  """
  json verisini python nesnesine dönüştürür.

  Russia
  Poland
  Hungary
  Ukraine
  Georgia
  """

  print(covid.tablo())
  """
  tabulate verisi döndürür.

  +----------------------------------+-------------------------------------------------+---------------+---------------+---------------+-----------------------+---------------+-----------------------+-------------------+---------------------------+---------------------+
  | ulke                             | ulke_bayragi                                    |   ulke_nufusu |   aktif_hasta |   vaka_sayisi |   bugunki_vaka_sayisi |   olum_sayisi |   bugunki_olum_sayisi |   iyilesen_sayisi |   bugunki_iyilesen_sayisi | ulke_harita_konum   |
  |----------------------------------+-------------------------------------------------+---------------+---------------+---------------+-----------------------+---------------+-----------------------+-------------------+---------------------------+---------------------|
  | Russia                           | https://disease.sh/assets/img/flags/ru.png      |     146027482 |        816589 |      10415230 |                 23210 |        305155 |                   937 |           9293486 |                     33715 | 60,100              |
  | USA                              | https://disease.sh/assets/img/flags/us.png      |     333887143 |      11653835 |      53621092 |                176460 |        839130 |                   520 |          41128127 |                     43309 | 38,-97              |
  | Hungary                          | https://disease.sh/assets/img/flags/hu.png      |       9623883 |        118633 |       1245319 |                  7989 |         38743 |                   436 |           1087943 |                     16171 | 47,20               |
  | France                           | https://disease.sh/assets/img/flags/fr.png      |      65488200 |       1158604 |       9146451 |                 30383 |        122898 |                   256 |           7864949 |                     58923 | 46,2                |
  | Germany                          | https://disease.sh/assets/img/flags/de.png      |      84182131 |        760564 |       7028368 |                 18734 |        111304 |                   223 |           6156500 |                     43000 | 51,9                |
  | Vietnam                          | https://disease.sh/assets/img/flags/vn.png      |      98639835 |        375513 |       1666545 |                 14872 |         31418 |                   204 |           1259614 |                     11374 | 21,105.8            |
  | Turkey                           | https://disease.sh/assets/img/flags/tr.png      |      85687258 |        285742 |       9333223 |                 26099 |         81733 |                   157 |           8965748 |                     22024 | 39,35               |
  | UK                               | https://disease.sh/assets/img/flags/gb.png      |      68415982 |       2100619 |      12209991 |                 98515 |        148003 |                   143 |           9961369 |                         0 | 54,-2               |
  | Italy                            | https://disease.sh/assets/img/flags/it.png      |      60329655 |        537504 |       5678112 |                 30810 |        136753 |                   142 |           5003855 |                      9992 | 42.8333,12.8333     |
  | Ukraine                          | https://disease.sh/assets/img/flags/ua.png      |      43343098 |        119278 |       3646988 |                  1864 |         94971 |                   133 |           3432739 |                      4527 | 49,32               |
  | Brazil                           | https://disease.sh/assets/img/flags/br.png      |     214804667 |        213383 |      22246276 |                  6840 |        618575 |                    91 |          21414318 |                         0 | -10,-55             |
  | ....                                                                                                                                                                                                                                                                     |
  +----------------------------------+-------------------------------------------------+---------------+---------------+---------------+-----------------------+---------------+-----------------------+-------------------+---------------------------+---------------------+
  """