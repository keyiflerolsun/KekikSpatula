from KekikSpatula import Doviz

def test_doviz():
  doviz = Doviz()

  print(doviz.veri)
  """
  json verisi döndürür

  {'kaynak': 'altinkaynak.com', 'veri': [{'birim': 'USD', 'alis': 7.965, 'satis': 7.995}, {'birim': 'EUR', 'alis': 9.45, 'satis': 9.49}, {'birim': 'CHF', 'alis': 8.681, 'satis': 8.793}, {'birim': 'GBP', 'alis': 10.543, 'satis': 10.7}, {'birim': 'DKK', 'alis': 1.2566, 'satis': 1.2805}, {'birim': 'SEK', 'alis': 0.9242, 'satis': 0.9389}, {'birim': 'NOK', 'alis': 0.8837, 'satis': 0.9014}, {'birim': 'JPY', 'alis': 0.0752, 'satis': 0.0769}, {'birim': 'SAR', 'alis': 2.098, 'satis': 2.14}, {'birim': 'AUD', 'alis': 5.777, 'satis': 5.887}, {'birim': 'CAD', 'alis': 6.08, 'satis': 6.177}, {'birim': 'RUB', 'alis': 0.0977, 'satis': 0.1089}, {'birim': 'AZN', 'alis': 3.7648, 'satis': 4.86}, {'birim': 'CNY', 'alis': 1.0563, 'satis': 1.2429}, {'birim': 'RON', 'alis': 1.493, 'satis': 2.0159}, {'birim': 'AED', 'alis': 1.8964, 'satis': 2.2254}, {'birim': 'BGN', 'alis': 4.003, 'satis': 4.9498}, {'birim': 'KWD', 'alis': 23.4681, 'satis': 26.3077}]}
  """

  for urun in doviz.nesne:
    print(urun.birim)
  """
  json verisini python nesnesine dönüştürür.

  USD
  EUR
  CHF
  GBP
  DKK
  SEK
  NOK
  JPY
  SAR
  AUD
  CAD
  RUB
  AZN
  CNY
  RON
  AED
  BGN
  KWD
  """


  print(doviz.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

  {
    "kaynak": "altinkaynak.com",
    "veri": [
      {
        "birim": "USD",
        "alis": 7.965,
        "satis": 7.995
      },
      {
        "birim": "EUR",
        "alis": 9.45,
        "satis": 9.49
      },
      {
        "birim": "CHF",
        "alis": 8.681,
        "satis": 8.793
      },
      {
        "birim": "GBP",
        "alis": 10.543,
        "satis": 10.7
      },
      {
        "birim": "DKK",
        "alis": 1.2566,
        "satis": 1.2805
      },
      {
        "birim": "SEK",
        "alis": 0.9242,
        "satis": 0.9389
      },
      {
        "birim": "NOK",
        "alis": 0.8837,
        "satis": 0.9014
      },
      {
        "birim": "JPY",
        "alis": 0.0752,
        "satis": 0.0769
      },
      {
        "birim": "SAR",
        "alis": 2.098,
        "satis": 2.14
      },
      {
        "birim": "AUD",
        "alis": 5.777,
        "satis": 5.887
      },
      {
        "birim": "CAD",
        "alis": 6.08,
        "satis": 6.177
      },
      {
        "birim": "RUB",
        "alis": 0.0977,
        "satis": 0.1089
      },
      {
        "birim": "AZN",
        "alis": 3.7648,
        "satis": 4.86
      },
      {
        "birim": "CNY",
        "alis": 1.0563,
        "satis": 1.2429
      },
      {
        "birim": "RON",
        "alis": 1.493,
        "satis": 2.0159
      },
      {
        "birim": "AED",
        "alis": 1.8964,
        "satis": 2.2254
      },
      {
        "birim": "BGN",
        "alis": 4.003,
        "satis": 4.9498
      },
      {
        "birim": "KWD",
        "alis": 23.4681,
        "satis": 26.3077
      }
    ]
  }
  """

  print(doviz.tablo())
  """
  tabulate verisi döndürür.

  +---------+---------+---------+
  | birim   |    alis |   satis |
  |---------+---------+---------|
  | USD     |  7.965  |  7.995  |
  | EUR     |  9.45   |  9.49   |
  | CHF     |  8.681  |  8.793  |
  | GBP     | 10.543  | 10.7    |
  | DKK     |  1.2566 |  1.2805 |
  | SEK     |  0.9242 |  0.9389 |
  | NOK     |  0.8837 |  0.9014 |
  | JPY     |  0.0752 |  0.0769 |
  | SAR     |  2.098  |  2.14   |
  | AUD     |  5.777  |  5.887  |
  | CAD     |  6.08   |  6.177  |
  | RUB     |  0.0977 |  0.1089 |
  | AZN     |  3.7648 |  4.86   |
  | CNY     |  1.0563 |  1.2429 |
  | RON     |  1.493  |  2.0159 |
  | AED     |  1.8964 |  2.2254 |
  | BGN     |  4.003  |  4.9498 |
  | KWD     | 23.4681 | 26.3077 |
  +---------+---------+---------+
  """

  print(doviz.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['birim', 'alis', 'satis']
  """