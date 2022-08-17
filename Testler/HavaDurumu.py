from KekikSpatula import HavaDurumu

def test_hava():
  hava = HavaDurumu("Mardin", "Nusaybin")

  print(hava.veri)
  """
  json verisi döndürür

  {'kaynak': 'google.com', 'veri': [{'gun': 'Perşembe 00:12', 'yer': 'Mardin Nusaybin', 'derece': 'Parçalı bulutlu 11°C'}]}
  """

  print(hava.nesne.derece)
  """
  json verisini python nesnesine dönüştürür.

  Parçalı bulutlu 11°C
  """


  print(hava.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

  {
    "kaynak": "google.com",
    "veri": [
      {
        "gun": "Perşembe 00:12",
        "yer": "Mardin Nusaybin",
        "derece": "Parçalı bulutlu 11°C"
      }
    ]
  }
  """

  print(hava.tablo())
  """
  tabulate verisi döndürür.

  +----------------+-----------------+----------------------+
  | gun            | yer             | derece               |
  |----------------+-----------------+----------------------|
  | Perşembe 00:12 | Mardin Nusaybin | Parçalı bulutlu 11°C |
  +----------------+-----------------+----------------------+
  """

  print(hava.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['gun', 'yer', 'derece']
  """