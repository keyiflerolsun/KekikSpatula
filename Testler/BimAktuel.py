from KekikSpatula import BimAktuel

def test_bim():
  bim = BimAktuel()

  print(bim.veri)
  """
  json verisi döndürür

  {'kaynak': 'bim.com.tr', 'tarih': '27 Kasım Cuma', 'veri': [{'urun_baslik': 'HP Pavilion Gaming Laptop', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/hp-pavilion-gaming-laptop/kral.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/653_buyuk_543X467_hp-laptop.jpg', 'urun_fiyat': '6.999,00₺'}, {'urun_baslik': 'Termal Mest', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/termal-mest/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_termal%20mest.jpg', 'urun_fiyat': '21,90₺'}, {'urun_baslik': 'İnci Süslemeli Kadın Bere', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/inci-suslemeli-kadin-bere/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_bere.jpg', 'urun_fiyat': '11,90₺'}, {'urun_baslik': 'Çocuk Atkı Bere  Eldiven Takımı 3’lü', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/cocuk-atki-bere-eldiven-takimi-3-lu/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_atkı%20eldiven%20takim.jpg', 'urun_fiyat': '19,90₺'}, {'urun_baslik': 'Kışlık Çocuk Panduf', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/kislik-cocuk-panduf/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_kislik%20panduf.jpg', 'urun_fiyat': '16,90₺'}, {'urun_baslik': 'Çocuk Bot', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/cocuk-bot/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_cocuk%20bot%20.jpg', 'urun_fiyat': '29,90₺'}, {'urun_baslik': 'Kadın-Erkek Bot', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/kadin-erkek-bot/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_bot%20erkek%20kadin.jpg', 'urun_fiyat': '36,90₺'}, {'urun_baslik': 'Peluş Erkek Kulaklık', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/pelus-erkek-kulaklik/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_pelus%20kulaklık.jpg', 'urun_fiyat': '6,95₺'}]}
  """

  for urun in bim.nesne:
    print(urun.urun_baslik)
  """
  json verisini python nesnesine dönüştürür.

  HP Pavilion Gaming Laptop
  Termal Mest
  İnci Süslemeli Kadın Bere
  Çocuk Atkı Bere  Eldiven Takımı 3’lü
  Kışlık Çocuk Panduf
  Çocuk Bot
  Kadın-Erkek Bot
  Peluş Erkek Kulaklık
  """


  print(bim.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

  {
    "kaynak": "bim.com.tr",
    "tarih": "27 Kasım Cuma",
    "veri": [
      {
        "urun_baslik": "HP Pavilion Gaming Laptop",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/hp-pavilion-gaming-laptop/kral.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/653_buyuk_543X467_hp-laptop.jpg",
        "urun_fiyat": "6.999,00₺"
      },
      {
        "urun_baslik": "Termal Mest",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/termal-mest/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_termal%20mest.jpg",
        "urun_fiyat": "21,90₺"
      },
      {
        "urun_baslik": "İnci Süslemeli Kadın Bere",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/inci-suslemeli-kadin-bere/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_bere.jpg",
        "urun_fiyat": "11,90₺"
      },
      {
        "urun_baslik": "Çocuk Atkı Bere  Eldiven Takımı 3’lü",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/cocuk-atki-bere-eldiven-takimi-3-lu/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_atkı%20eldiven%20takim.jpg",
        "urun_fiyat": "19,90₺"
      },
      {
        "urun_baslik": "Kışlık Çocuk Panduf",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/kislik-cocuk-panduf/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_kislik%20panduf.jpg",
        "urun_fiyat": "16,90₺"
      },
      {
        "urun_baslik": "Çocuk Bot",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/cocuk-bot/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_cocuk%20bot%20.jpg",
        "urun_fiyat": "29,90₺"
      },
      {
        "urun_baslik": "Kadın-Erkek Bot",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/kadin-erkek-bot/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_bot%20erkek%20kadin.jpg",
        "urun_fiyat": "36,90₺"
      },
      {
        "urun_baslik": "Peluş Erkek Kulaklık",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/pelus-erkek-kulaklik/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_pelus%20kulaklık.jpg",
        "urun_fiyat": "6,95₺"
      }
    ]
  }
  """

  print(bim.tablo())
  """
  tabulate verisi döndürür.

  +--------------------------------------+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+--------------+
  | urun_baslik                          | urun_link                                                                             | urun_gorsel                                                                                | urun_fiyat   |
  |--------------------------------------+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+--------------|
  | HP Pavilion Gaming Laptop            | https://www.bim.com.tr/aktuel-urunler/hp-pavilion-gaming-laptop/kral.aspx             | https://www.bim.com.tr/Uploads/aktuel-urunler/653_buyuk_543X467_hp-laptop.jpg              | 6.999,00₺    |
  | Termal Mest                          | https://www.bim.com.tr/aktuel-urunler/termal-mest/aktuel.aspx                         | https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_termal%20mest.jpg          | 21,90₺       |
  | İnci Süslemeli Kadın Bere            | https://www.bim.com.tr/aktuel-urunler/inci-suslemeli-kadin-bere/aktuel.aspx           | https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_bere.jpg                   | 11,90₺       |
  | Çocuk Atkı Bere  Eldiven Takımı 3’lü | https://www.bim.com.tr/aktuel-urunler/cocuk-atki-bere-eldiven-takimi-3-lu/aktuel.aspx | https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_atkı%20eldiven%20takim.jpg | 19,90₺       |
  | Kışlık Çocuk Panduf                  | https://www.bim.com.tr/aktuel-urunler/kislik-cocuk-panduf/aktuel.aspx                 | https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_kislik%20panduf.jpg        | 16,90₺       |
  | Çocuk Bot                            | https://www.bim.com.tr/aktuel-urunler/cocuk-bot/aktuel.aspx                           | https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_cocuk%20bot%20.jpg         | 29,90₺       |
  | Kadın-Erkek Bot                      | https://www.bim.com.tr/aktuel-urunler/kadin-erkek-bot/aktuel.aspx                     | https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_bot%20erkek%20kadin.jpg    | 36,90₺       |
  | Peluş Erkek Kulaklık                 | https://www.bim.com.tr/aktuel-urunler/pelus-erkek-kulaklik/aktuel.aspx                | https://www.bim.com.tr/Uploads/aktuel-urunler/653_kucuk_543X467_pelus%20kulaklık.jpg       | 6,95₺        |
  +--------------------------------------+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+--------------+
  """

  print(bim.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['urun_baslik', 'urun_link', 'urun_gorsel', 'urun_fiyat']
  """