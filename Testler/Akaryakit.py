from KekikSpatula import Akaryakit

def test_akaryakit():
  akaryakit = Akaryakit()

  print(akaryakit.veri)
  """
  json verisi döndürür

  {'kaynak': 'finans.haberler.com', 'son_guncellenme': '26.11.2020 02:08', 'veri': [{'cinsi': 'Kurşunsuz 95 -- ₺/lt', 'fiyati': '4,85 TL'}, {'cinsi': 'Kurşunsuz 95(Excellium95) -- ₺/lt', 'fiyati': '6,99 TL'}, {'cinsi': 'Gazyağı -- ₺/lt', 'fiyati': '5,23 TL'}, {'cinsi': 'Motorin(Eurodiesel) -- ₺/lt', 'fiyati': '6,27 TL'}, {'cinsi': 'Motorin(Excellium Eurodiesel) -- ₺/lt', 'fiyati': '6,31 TL'}, {'cinsi': 'Kalorifer Yakıtı -- ₺/Kg', 'fiyati': '4,66 TL'}, {'cinsi': 'Fuel Oil -- ₺/Kg', 'fiyati': '4,35 TL'}]}
  """

  for urun in akaryakit.nesne:
    print(urun.fiyati)
  """
  json verisini python nesnesine dönüştürür.

  4,85 TL
  6,99 TL
  5,23 TL
  6,27 TL
  6,31 TL
  4,66 TL
  4,35 TL
  """


  print(akaryakit.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

  {
    "kaynak": "finans.haberler.com",
    "son_guncellenme": "26.11.2020 02:08",
    "veri": [
      {
        "cinsi": "Kurşunsuz 95 -- ₺/lt",
        "fiyati": "4,85 TL"
      },
      {
        "cinsi": "Kurşunsuz 95(Excellium95) -- ₺/lt",
        "fiyati": "6,99 TL"
      },
      {
        "cinsi": "Gazyağı -- ₺/lt",
        "fiyati": "5,23 TL"
      },
      {
        "cinsi": "Motorin(Eurodiesel) -- ₺/lt",
        "fiyati": "6,27 TL"
      },
      {
        "cinsi": "Motorin(Excellium Eurodiesel) -- ₺/lt",
        "fiyati": "6,31 TL"
      },
      {
        "cinsi": "Kalorifer Yakıtı -- ₺/Kg",
        "fiyati": "4,66 TL"
      },
      {
        "cinsi": "Fuel Oil -- ₺/Kg",
        "fiyati": "4,35 TL"
      }
    ]
  }
  """

  print(akaryakit.tablo())
  """
  tabulate verisi döndürür.

  +---------------------------------------+----------+
  | cinsi                                 | fiyati   |
  |---------------------------------------+----------|
  | Kurşunsuz 95 -- ₺/lt                  | 4,85 TL  |
  | Kurşunsuz 95(Excellium95) -- ₺/lt     | 6,99 TL  |
  | Gazyağı -- ₺/lt                       | 5,23 TL  |
  | Motorin(Eurodiesel) -- ₺/lt           | 6,27 TL  |
  | Motorin(Excellium Eurodiesel) -- ₺/lt | 6,31 TL  |
  | Kalorifer Yakıtı -- ₺/Kg              | 4,66 TL  |
  | Fuel Oil -- ₺/Kg                      | 4,35 TL  |
  +---------------------------------------+----------+
  """

  print(akaryakit.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['cinsi', 'fiyati']
  """