from KekikSpatula import Kripto

def test_kripto():
  kline = Kripto("BTCUSDT", "1m")

  print(kline.veri)
  """
  json verisi döndürür

  {"kaynak": "api.binance.com","veri": [{ "acilis_zamani": 1640896080000, "acilis": "47646.74000000", "en_yuksek": "47646.95000000", "en_dusuk": "47600.66000000", "kapanis": "47600.67000000", "hacim": "3.51270000", "kapanis_zamani": 1640896139999, "teklif_varlik_hacmi": "167291.60083120", "islem_sayisi": 218, "satin_alma_temel_varlik_hacmi": "0.33201000", "satın_alma_teklifi_varlik_hacmi": "15811.35691650"}]}
  """

  print(kline.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

  {
    "kaynak": "api.binance.com",
    "veri": [
      {
        "acilis_zamani": 1640896080000,
        "acilis": "47646.74000000",
        "en_yuksek": "47646.95000000",
        "en_dusuk": "47600.66000000",
        "kapanis": "47600.67000000",
        "hacim": "3.51270000",
        "kapanis_zamani": 1640896139999,
        "teklif_varlik_hacmi": "167291.60083120",
        "islem_sayisi": 218,
        "satin_alma_temel_varlik_hacmi": "0.33201000",
        "satın_alma_teklifi_varlik_hacmi": "15811.35691650"
      },
      ...
    ]
  }
  """

  print(kline.tablo())
  """
  tabulate verisi döndürür.

  +-----------------+----------+-------------+------------+-----------+-----------+------------------+-----------------------+----------------+---------------------------------+-----------------------------------+
  |   acilis_zamani |   acilis |   en_yuksek |   en_dusuk |   kapanis |     hacim |   kapanis_zamani |   teklif_varlik_hacmi |   islem_sayisi |   satin_alma_temel_varlik_hacmi |   satın_alma_teklifi_varlik_hacmi |
  |-----------------+----------+-------------+------------+-----------+-----------+------------------+-----------------------+----------------+---------------------------------+-----------------------------------|
  |   1640866260000 |  47438.4 |     47440.9 |    47420   |   47420   |  13.2102  |    1640866319999 |      626528           |            564 |                         5.88422 |                  279060           |
  |   1640866320000 |  47420   |     47442.1 |    47420   |   47438.5 |  15.6916  |    1640866379999 |      744316           |            634 |                         4.82995 |                  229104           |
  +-----------------+----------+-------------+------------+-----------+-----------+------------------+-----------------------+----------------+---------------------------------+-----------------------------------+
  """