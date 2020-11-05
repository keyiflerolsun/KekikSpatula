# ✂️ KekikSpatula

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/bc0a52a9b57f4c29930cbd6c796f9a8b)](https://www.codacy.com/gh/keyiflerolsun/KekikSpatula/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=keyiflerolsun/KekikSpatula&amp;utm_campaign=Badge_Grade) ![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/KekikSpatula) ![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/KekikSpatula&title=Profile%20Views) [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/keyiflerolsun/KekikSpatula)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/KekikSpatula)
![PyPI - Status](https://img.shields.io/pypi/status/KekikSpatula)
![PyPI](https://img.shields.io/pypi/v/KekikSpatula)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/KekikSpatula)
![PyPI - License](https://img.shields.io/pypi/l/KekikSpatula)

**Siz uğraşmayın diye** *biz uğraştık..* **~** `dızz 🐍`

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum - Kullanım

```bash
# Yüklemek
pip install KekikSpatula

# Güncellemek
pip install -U KekikSpatula
```

## 📝 Proje İlerlemesi

- [x] `v0.1.0` *~* **[NobetciEczane](https://github.com/keyiflerolsun/KekikSpatula#%EF%B8%8F-nobetcieczane)** *Spatulası ile proje başlamıştır..*
- [x] `v0.1.1` *ile* **[Akaryakit](https://github.com/keyiflerolsun/KekikSpatula#%EF%B8%8F-akaryakit)** *Spatulası Eklenmiştir..*
- [x] `v0.1.2` *ile* **[Doviz](https://github.com/keyiflerolsun/KekikSpatula#-doviz)** *Spatulası Eklenmiştir..*
- [x] `v0.1.3` *ile* **[SonDepremler](https://github.com/keyiflerolsun/KekikSpatula#-sondepremler)** *Spatulası Eklenmiştir..*
- [x] `v0.1.4` *ile* **[BimAktuel](https://github.com/keyiflerolsun/KekikSpatula#-bimaktuel)** *Spatulası Eklenmiştir..*
- [x] `v0.1.5` *ile* **[SonDakika](https://github.com/keyiflerolsun/KekikSpatula#-sondakika)** *Spatulası Eklenmiştir..*
- [x] `v0.1.6` *ile* **[HavaDurumu](https://github.com/keyiflerolsun/KekikSpatula#%EF%B8%8F-havadurumu)** *Spatulası Eklenmiştir..*
- [x] `v0.1.7` *ile* **[Ezan](https://github.com/keyiflerolsun/KekikSpatula#-ezan)** *Spatulası Eklenmiştir..*
- [x] `v0.1.8` *ile* **HavaDurumu** *Karakter Sorunu Çözülmüştür..*
- [x] `v0.1.9` *ile* **[DiscUdemy](https://github.com/keyiflerolsun/KekikSpatula#-discudemy)** *Spatulası Eklenmiştir..*

### ⚕️ NobetciEczane

```python
from KekikSpatula import NobetciEczane

eczane = NobetciEczane('Çanakkale', 'Merkez')

print(eczane.veri())
    """
    JSON(dict) Veri Döndürür

    {'kaynak': 'eczaneler.gen.tr', 'veri': [{'ad': 'Betül Eczanesi', 'mahalle': None, 'adres': 'Cumhuriyet Mahallesi Sahil Yolu Caddesi, No:8/A Dükkan 1 Kepez Kepez Ağız ve Diş Hastanesi karşısı Merkez / Çanakkale', 'tarif': None, 'telefon': '0 (286) 263-52-63'}, {'ad': 'Elçin Eczanesi', 'mahalle': None, 'adres': 'Cevatpaşa Mahallesi, İnönü Caddesi Lale Apartmanı No:76/B Merkez / Çanakkale', 'tarif': 'Endüstri Meslek Lisesi karşısı, Ayhan Çiçekçiliğin yanı', 'telefon': '0 (286) 217-47-07'}, {'ad': 'İrem Eczanesi', 'mahalle': None, 'adres': 'İnönü Caddesi, No:135 Merkez / Çanakkale', 'tarif': 'Emniyet Müdürlüğü karşısı', 'telefon': '0 (286) 213-06-92'}]}
    """

print(eczane.gorsel())
    """
    Okunabilir JSON(str) Döndürür

    {
    "kaynak": "eczaneler.gen.tr",
    "veri": [
        {
        "ad": "Betül Eczanesi",
        "mahalle": null,
        "adres": "Cumhuriyet Mahallesi Sahil Yolu Caddesi, No:8/A Dükkan 1 Kepez Kepez Ağız ve Diş Hastanesi karşısı Merkez / Çanakkale",
        "tarif": null,
        "telefon": "0 (286) 263-52-63"
        },
        {
        "ad": "Elçin Eczanesi",
        "mahalle": null,
        "adres": "Cevatpaşa Mahallesi, İnönü Caddesi Lale Apartmanı No:76/B Merkez / Çanakkale",
        "tarif": "Endüstri Meslek Lisesi karşısı, Ayhan Çiçekçiliğin yanı",
        "telefon": "0 (286) 217-47-07"
        },
        {
        "ad": "İrem Eczanesi",
        "mahalle": null,
        "adres": "İnönü Caddesi, No:135 Merkez / Çanakkale",
        "tarif": "Emniyet Müdürlüğü karşısı",
        "telefon": "0 (286) 213-06-92"
        }
    ]
    }
    """

print(eczane.tablo())
    """
    Tabulate(str) Döndürür

    +----------------+-----------+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+-------------------+
    | ad             | mahalle   | adres                                                                                                                 | tarif                                                   | telefon           |
    |----------------+-----------+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+-------------------|
    | Betül Eczanesi |           | Cumhuriyet Mahallesi Sahil Yolu Caddesi, No:8/A Dükkan 1 Kepez Kepez Ağız ve Diş Hastanesi karşısı Merkez / Çanakkale |                                                         | 0 (286) 263-52-63 |
    | Elçin Eczanesi |           | Cevatpaşa Mahallesi, İnönü Caddesi Lale Apartmanı No:76/B Merkez / Çanakkale                                          | Endüstri Meslek Lisesi karşısı, Ayhan Çiçekçiliğin yanı | 0 (286) 217-47-07 |
    | İrem Eczanesi  |           | İnönü Caddesi, No:135 Merkez / Çanakkale                                                                              | Emniyet Müdürlüğü karşısı                               | 0 (286) 213-06-92 |
    +----------------+-----------+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+-------------------+
    """

print(eczane.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['ad', 'mahalle', 'adres', 'tarif', 'telefon']
    """
```

### ⛽️ Akaryakit

```python
from KekikSpatula import Akaryakit

akaryakit = Akaryakit()

print(akaryakit.veri())
    """
    JSON(dict) Veri Döndürür

    {'kaynak': 'finans.haberler.com', 'son_guncellenme': '29.10.2020 21:56', 'veri': [{'cinsi': 'Kurşunsuz 95 -- ₺/lt', 'fiyati': '4,85 TL'}, {'cinsi': 'Kurşunsuz 95(Excellium95) -- ₺/lt', 'fiyati': '6,70 TL'}, {'cinsi': 'Gazyağı -- ₺/lt', 'fiyati': '5,05 TL'}, {'cinsi': 'Motorin(Eurodiesel) -- ₺/lt', 'fiyati': '6,11 TL'}, {'cinsi': 'Motorin(Excellium Eurodiesel) -- ₺/lt', 'fiyati': '6,15 TL'}, {'cinsi': 'Kalorifer Yakıtı -- ₺/Kg', 'fiyati': '4,29 TL'}, {'cinsi': 'Fuel Oil -- ₺/Kg', 'fiyati': '4,03 TL'}]}
    """

print(akaryakit.gorsel())
    """
    Okunabilir JSON(str) Döndürür

    {
    "kaynak": "finans.haberler.com",
    "son_guncellenme": "29.10.2020 21:56",
    "veri": [
        {
        "cinsi": "Kurşunsuz 95 -- ₺/lt",
        "fiyati": "4,85 TL"
        },
        {
        "cinsi": "Kurşunsuz 95(Excellium95) -- ₺/lt",
        "fiyati": "6,70 TL"
        },
        {
        "cinsi": "Gazyağı -- ₺/lt",
        "fiyati": "5,05 TL"
        },
        {
        "cinsi": "Motorin(Eurodiesel) -- ₺/lt",
        "fiyati": "6,11 TL"
        },
        {
        "cinsi": "Motorin(Excellium Eurodiesel) -- ₺/lt",
        "fiyati": "6,15 TL"
        },
        {
        "cinsi": "Kalorifer Yakıtı -- ₺/Kg",
        "fiyati": "4,29 TL"
        },
        {
        "cinsi": "Fuel Oil -- ₺/Kg",
        "fiyati": "4,03 TL"
        }
    ]
    }
    """

print(akaryakit.tablo())
    """
    Tabulate(str) Döndürür

    +---------------------------------------+----------+
    | cinsi                                 | fiyati   |
    |---------------------------------------+----------|
    | Kurşunsuz 95 -- ₺/lt                  | 4,85 TL  |
    | Kurşunsuz 95(Excellium95) -- ₺/lt     | 6,70 TL  |
    | Gazyağı -- ₺/lt                       | 5,05 TL  |
    | Motorin(Eurodiesel) -- ₺/lt           | 6,11 TL  |
    | Motorin(Excellium Eurodiesel) -- ₺/lt | 6,15 TL  |
    | Kalorifer Yakıtı -- ₺/Kg              | 4,29 TL  |
    | Fuel Oil -- ₺/Kg                      | 4,03 TL  |
    +---------------------------------------+----------+
    """

print(akaryakit.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['cinsi', 'fiyati']
    """
```

### 💱 Doviz

```python
from KekikSpatula import Doviz

doviz = Doviz()

print(doviz.veri())
    """
    JSON(dict) Veri Döndürür

    {'kaynak': 'altinkaynak.com', 'veri': [{'Birim': 'USD', 'Alış': 8.245, 'Satış': 8.275}, {'Birim': 'EUR', 'Alış': 9.67, 'Satış': 9.71}, {'Birim': 'CHF', 'Alış': 8.991, 'Satış': 9.064}, {'Birim': 'GBP', 'Alış': 10.649, 'Satış': 10.747}, {'Birim': 'DKK', 'Alış': 1.2831, 'Satış': 1.3014}, {'Birim': 'SEK', 'Alış': 0.9217, 'Satış': 0.933}, {'Birim': 'NOK', 'Alış': 0.8677, 'Satış': 0.8845}, {'Birim': 'JPY', 'Alış': 0.0779, 'Satış': 0.0793}, {'Birim': 'SAR', 'Alış': 2.168, 'Satış': 2.205}, {'Birim': 'AUD', 'Alış': 5.74, 'Satış': 5.833}, {'Birim': 'CAD', 'Alış': 6.152, 'Satış': 6.227}, {'Birim': 'RUB', 'Alış': 0.0975, 'Satış': 0.1084}, {'Birim': 'AZN', 'Alış': 3.8943, 'Satış': 5.0085}, {'Birim': 'CNY', 'Alış': 1.068, 'Satış': 1.2521}, {'Birim': 'RON', 'Alış': 1.5229, 'Satış': 2.0487}, {'Birim': 'AED', 'Alış': 1.9617, 'Satış': 2.2934}, {'Birim': 'BGN', 'Alış': 4.085, 'Satış': 5.033}, {'Birim': 'KWD', 'Alış': 24.269, 'Satış': 27.1044}]}
    """

print(doviz.gorsel())
    """
    Okunabilir JSON(str) Döndürür

    {
    "kaynak": "altinkaynak.com",
    "veri": [
        {
        "Birim": "USD",
        "Alış": 8.245,
        "Satış": 8.275
        },
        {
        "Birim": "EUR",
        "Alış": 9.67,
        "Satış": 9.71
        },
        {
        "Birim": "CHF",
        "Alış": 8.991,
        "Satış": 9.064
        },
        {
        "Birim": "GBP",
        "Alış": 10.649,
        "Satış": 10.747
        },
        {
        "Birim": "DKK",
        "Alış": 1.2831,
        "Satış": 1.3014
        },
        {
        "Birim": "SEK",
        "Alış": 0.9217,
        "Satış": 0.933
        },
        {
        "Birim": "NOK",
        "Alış": 0.8677,
        "Satış": 0.8845
        },
        {
        "Birim": "JPY",
        "Alış": 0.0779,
        "Satış": 0.0793
        },
        {
        "Birim": "SAR",
        "Alış": 2.168,
        "Satış": 2.205
        },
        {
        "Birim": "AUD",
        "Alış": 5.74,
        "Satış": 5.833
        },
        {
        "Birim": "CAD",
        "Alış": 6.152,
        "Satış": 6.227
        },
        {
        "Birim": "RUB",
        "Alış": 0.0975,
        "Satış": 0.1084
        },
        {
        "Birim": "AZN",
        "Alış": 3.8943,
        "Satış": 5.0085
        },
        {
        "Birim": "CNY",
        "Alış": 1.068,
        "Satış": 1.2521
        },
        {
        "Birim": "RON",
        "Alış": 1.5229,
        "Satış": 2.0487
        },
        {
        "Birim": "AED",
        "Alış": 1.9617,
        "Satış": 2.2934
        },
        {
        "Birim": "BGN",
        "Alış": 4.085,
        "Satış": 5.033
        },
        {
        "Birim": "KWD",
        "Alış": 24.269,
        "Satış": 27.1044
        }
    ]
    }
    """

print(doviz.tablo())
    """
    Tabulate(str) Döndürür

    +---------+---------+---------+
    | Birim   |    Alış |   Satış |
    |---------+---------+---------|
    | USD     |  8.245  |  8.275  |
    | EUR     |  9.67   |  9.71   |
    | CHF     |  8.991  |  9.064  |
    | GBP     | 10.649  | 10.747  |
    | DKK     |  1.2831 |  1.3014 |
    | SEK     |  0.9217 |  0.933  |
    | NOK     |  0.8677 |  0.8845 |
    | JPY     |  0.0779 |  0.0793 |
    | SAR     |  2.168  |  2.205  |
    | AUD     |  5.74   |  5.833  |
    | CAD     |  6.152  |  6.227  |
    | RUB     |  0.0975 |  0.1084 |
    | AZN     |  3.8943 |  5.0085 |
    | CNY     |  1.068  |  1.2521 |
    | RON     |  1.5229 |  2.0487 |
    | AED     |  1.9617 |  2.2934 |
    | BGN     |  4.085  |  5.033  |
    | KWD     | 24.269  | 27.1044 |
    +---------+---------+---------+
    """

print(doviz.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['Birim', 'Alış', 'Satış']
    """
```

### 🌀 SonDepremler

```python
from KekikSpatula import SonDepremler

deprem = SonDepremler()

print(deprem.veri())
    """
    JSON(dict) Veri Döndürür
    """

print(deprem.gorsel())
    """
    Okunabilir JSON(str) Döndürür

        {
        "Tarih": "2020.10.18",
        "Saat": "07:10:23",
        "Enlem(N)": "38.6587",
        "Boylam(E)": "43.0703",
        "Derinlik(km)": "4.3",
        "MD": "-.-",
        "ML": "2.8",
        "MS": "-.-",
        "Yer": "VAN GOLU İlksel"
        },
        {
        "Tarih": "2020.10.18",
        "Saat": "07:04:46",
        "Enlem(N)": "35.5735",
        "Boylam(E)": "26.3203",
        "Derinlik(km)": "6.5",
        "MD": "-.-",
        "ML": "2.7",
        "MS": "-.-",
        "Yer": "AKDENIZ İlksel"
        },
        {
        "Tarih": "2020.10.18",
        "Saat": "06:56:20",
        "Enlem(N)": "34.7457",
        "Boylam(E)": "26.7503",
        "Derinlik(km)": "10.8",
        "MD": "-.-",
        "ML": "2.4",
        "MS": "-.-",
        "Yer": "GIRIT ADASI ACIKLARI (AKDENIZ) İlksel"
        },
        {
        "Tarih": "2020.10.18",
        "Saat": "05:16:08",
        "Enlem(N)": "40.7805",
        "Boylam(E)": "31.7178",
        "Derinlik(km)": "15.1",
        "MD": "-.-",
        "ML": "1.6",
        "MS": "-.-",
        "Yer": "TATLAR-(BOLU) İlksel"
        }
    ]
    }
    """

print(deprem.tablo())
    """
    Tabulate(str) Döndürür

    +------------+----------+------------+-------------+----------------+------+------+------+------------------------------------------------------------+
    | Tarih      | Saat     |   Enlem(N) |   Boylam(E) |   Derinlik(km) | MD   |   ML | MS   | Yer                                                        |
    |------------+----------+------------+-------------+----------------+------+------+------+------------------------------------------------------------|
    | 2020.10.29 | 22:11:08 |    38.773  |     42.9525 |            6.4 | -.-  |  1.8 | -.-  | KARSIYAKA-ADILCEVAZ (BITLIS) İlksel                        |
    | 2020.10.29 | 21:33:17 |    39.572  |     41.3577 |            8.2 | -.-  |  2.4 | -.-  | GOZLUCE-TEKMAN (ERZURUM) İlksel                            |
    """

print(deprem.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['Tarih', 'Saat', 'Enlem(N)', 'Boylam(E)', 'Derinlik(km)', 'MD', 'ML', 'MS', 'Yer']
    """
```

### 🛒 BimAktuel

```python
from KekikSpatula import BimAktuel

bim = BimAktuel()

print(bim.veri())
    """
    JSON(dict) Veri Döndürür

    {'kaynak': 'bim.com.tr', 'tarih': '30 Ekim Cuma', 'veri': [{'urun_baslik': 'Dijitsu 65 Inç TV Smart LED Uydu Alıcılı', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/dijitsu-65-inc-tv-smart-led-uydu-alicili/kral.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/643_buyuk_543X467_tv.jpg', 'urun_fiyat': '4.399,00₺'}, {'urun_baslik': '51 Parça Altın Fileli Rölyefli Yemek Takımı', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/51-parca-altin-fileli-rolyefli-yemek-takimi/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_51%20parca%20altin%20fileli.jpg', 'urun_fiyat': '369,00₺'}, {'urun_baslik': 'Sahan Seti', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/sahan-seti/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_sahan%20seti%204%20parca.jpg', 'urun_fiyat': '119,00₺'}, {'urun_baslik': 'Granit Karnıyarık  Tenceresi', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/granit-karniyarik-tenceresi/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_granit%20karniyarik.jpg', 'urun_fiyat': '79,90₺'}, {'urun_baslik': 'Granit Tava Seti 2’li', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/granit-tava-seti-2-li/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_granit%20tava%20seti.jpg', 'urun_fiyat': '79,90₺'}, {'urun_baslik': 'Taşıma Kapaklı Kek Kalıbı', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/tasima-kapakli-kek-kalibi/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_tasima%20kapakli%20kek%20kalibi.jpg', 'urun_fiyat': '39,90₺'}, {'urun_baslik': 'Baton ve Dilimli Kek Kalıbı Çeşitleri', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/baton-ve-dilimli-kek-kalibi-cesitleri/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_baton%20ve%20dilimli%20kek.jpg', 'urun_fiyat': '19,90₺'}, {'urun_baslik': '6’lı Ayaklı Kahve Yanı Su Bardağı', 'urun_link': 'https://www.bim.com.tr/aktuel-urunler/6-li-ayakli-kahve-yani-su-bardagi/aktuel.aspx', 'urun_gorsel': 'https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_6li%20ayakli%20kahv.jpg', 'urun_fiyat': '25,00₺'}]}
    """

print(bim.gorsel())
    """
    Okunabilir JSON(str) Döndürür

    {
    "kaynak": "bim.com.tr",
    "tarih": "30 Ekim Cuma",
    "veri": [
        {
        "urun_baslik": "Dijitsu 65 Inç TV Smart LED Uydu Alıcılı",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/dijitsu-65-inc-tv-smart-led-uydu-alicili/kral.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/643_buyuk_543X467_tv.jpg",
        "urun_fiyat": "4.399,00₺"
        },
        {
        "urun_baslik": "51 Parça Altın Fileli Rölyefli Yemek Takımı",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/51-parca-altin-fileli-rolyefli-yemek-takimi/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_51%20parca%20altin%20fileli.jpg",
        "urun_fiyat": "369,00₺"
        },
        {
        "urun_baslik": "Sahan Seti",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/sahan-seti/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_sahan%20seti%204%20parca.jpg",
        "urun_fiyat": "119,00₺"
        },
        {
        "urun_baslik": "Granit Karnıyarık  Tenceresi",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/granit-karniyarik-tenceresi/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_granit%20karniyarik.jpg",
        "urun_fiyat": "79,90₺"
        },
        {
        "urun_baslik": "Granit Tava Seti 2’li",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/granit-tava-seti-2-li/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_granit%20tava%20seti.jpg",
        "urun_fiyat": "79,90₺"
        },
        {
        "urun_baslik": "Taşıma Kapaklı Kek Kalıbı",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/tasima-kapakli-kek-kalibi/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_tasima%20kapakli%20kek%20kalibi.jpg",
        "urun_fiyat": "39,90₺"
        },
        {
        "urun_baslik": "Baton ve Dilimli Kek Kalıbı Çeşitleri",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/baton-ve-dilimli-kek-kalibi-cesitleri/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_baton%20ve%20dilimli%20kek.jpg",
        "urun_fiyat": "19,90₺"
        },
        {
        "urun_baslik": "6’lı Ayaklı Kahve Yanı Su Bardağı",
        "urun_link": "https://www.bim.com.tr/aktuel-urunler/6-li-ayakli-kahve-yani-su-bardagi/aktuel.aspx",
        "urun_gorsel": "https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_6li%20ayakli%20kahv.jpg",
        "urun_fiyat": "25,00₺"
        }
    ]
    }
    """

print(bim.tablo())
    """
    Tabulate(str) Döndürür

    +---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------+
    | urun_baslik                                 | urun_link                                                                                     | urun_gorsel                                                                                         | urun_fiyat   |
    |---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------|
    | Dijitsu 65 Inç TV Smart LED Uydu Alıcılı    | https://www.bim.com.tr/aktuel-urunler/dijitsu-65-inc-tv-smart-led-uydu-alicili/kral.aspx      | https://www.bim.com.tr/Uploads/aktuel-urunler/643_buyuk_543X467_tv.jpg                              | 4.399,00₺    |
    | 51 Parça Altın Fileli Rölyefli Yemek Takımı | https://www.bim.com.tr/aktuel-urunler/51-parca-altin-fileli-rolyefli-yemek-takimi/aktuel.aspx | https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_51%20parca%20altin%20fileli.jpg     | 369,00₺      |
    | Sahan Seti                                  | https://www.bim.com.tr/aktuel-urunler/sahan-seti/aktuel.aspx                                  | https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_sahan%20seti%204%20parca.jpg        | 119,00₺      |
    | Granit Karnıyarık  Tenceresi                | https://www.bim.com.tr/aktuel-urunler/granit-karniyarik-tenceresi/aktuel.aspx                 | https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_granit%20karniyarik.jpg             | 79,90₺       |
    | Granit Tava Seti 2’li                       | https://www.bim.com.tr/aktuel-urunler/granit-tava-seti-2-li/aktuel.aspx                       | https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_granit%20tava%20seti.jpg            | 79,90₺       |
    | Taşıma Kapaklı Kek Kalıbı                   | https://www.bim.com.tr/aktuel-urunler/tasima-kapakli-kek-kalibi/aktuel.aspx                   | https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_tasima%20kapakli%20kek%20kalibi.jpg | 39,90₺       |
    | Baton ve Dilimli Kek Kalıbı Çeşitleri       | https://www.bim.com.tr/aktuel-urunler/baton-ve-dilimli-kek-kalibi-cesitleri/aktuel.aspx       | https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_baton%20ve%20dilimli%20kek.jpg      | 19,90₺       |
    | 6’lı Ayaklı Kahve Yanı Su Bardağı           | https://www.bim.com.tr/aktuel-urunler/6-li-ayakli-kahve-yani-su-bardagi/aktuel.aspx           | https://www.bim.com.tr/Uploads/aktuel-urunler/643_kucuk_543X467_6li%20ayakli%20kahv.jpg             | 25,00₺       |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------+
    """

print(bim.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['urun_baslik', 'urun_link', 'urun_gorsel', 'urun_fiyat']
    """
```

### 📰 SonDakika

```python
from KekikSpatula import SonDakika

haber = SonDakika()

print(haber.veri())
    """
    JSON(dict) Veri Döndürür

    {'kaynak': 'ntv.com.tr', 'veri': [{'Haber': 'Mesut Yılmaz hayatını kaybetti', 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-mesut-yilmaz-hayatini-kaybetti,uUhAL55lZ0Wer3SRXwaXyw'}, {'Haber': "Merkez Bankası'ndan yeni adım", 'Link': 'https://www.ntv.com.tr/ekonomi/son-dakika-haberi-merkez-bankasindan-yeni-adim,i5ytNXpMWkikhyVTMsPkAw'}, {'Haber': 'Çeyrek ve gram altın fiyatları bugün ne kadar oldu? 30 Ekim 2020 anlık ve güncel çeyrek altın kuru fiyatları', 'Link': 'https://www.ntv.com.tr/ekonomi/ceyrek-ve-gram-altin-fiyatlari-bugun-ne-kadar-oldu-30-ekim-2020-anlik-ve-guncel-ceyrek-altin-kuru-fiyatlari,MAlt1qPmdkSAWayZS9WECA'}, {'Haber': 'Dolar\xa0kaç TL? (30 Ekim 2020 dolar - euro fiyatları)', 'Link': 'https://www.ntv.com.tr/ekonomi/dolarkac-tl-30-ekim-2020-dolar-euro-fiyatlari,7cUHGwdKzE2mh8IKkdmnMw'}, {'Haber': "2020 Yılı Cumhurbaşkanlığı Kültür ve Sanat Büyük Ödülleri'ne layık görülen isimler açıklandı", 'Link': 'https://www.ntv.com.tr/sanat/son-dakika-haberi2020-yili-cumhurbaskanligi-kultur-ve-sanat-buyuk-odullerine-layik-gorulen-isimler-aciklandi,phuDiX_3qUC-8VLjwsOamA'}, {'Haber': '29 Ekim 2020 corona virüs tablosu:\xa072 can kaybı,\xa02 bin 319 yeni hasta', 'Link': 'https://www.ntv.com.tr/turkiye/29-ekim-2020-corona-virus-tablosu72-can-kaybi-2-319-yeni-hasta-sayisi,TReNnv_5VkawG5b_29RHIA'}, {'Haber': 'Cumhurbaşkanı Erdoğan: En büyük gücümüz tarihi mirasımızdır', 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-konusuyor,CjkQF1OJK0-pNLSnrd4M8Q'}, {'Haber': 'İYİ Parti İstanbul Milletvekili Ümit Özdağ disipline sevk edildi', 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberiiyi-parti-istanbul-milletvekili-umit-ozdag-disipline-sevk-edildi,_RY4y88SdE2hzvd-GgJeZw'}, {'Haber': "MSB: 5 PKK/YPG'li terörist etkisiz hale getirildi", 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-msb-5-pkk-ypgli-terorist-etkisiz-hale-getirildi,kY1HOFFo5Ei-hbbLkiTfPA'}, {'Haber': "Türkiye'den Fransa'daki saldırıya kınama", 'Link': 'https://www.ntv.com.tr/turkiye/turkiyeden-fransadaki-saldiriya-kinama,ZcW7zg-wBka2phDu0lb0aw'}, {'Haber': "Putin'den Dağlık Karabağ açıklaması", 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-putinden-karabag-aciklamasi,4b5IoVqi-EapWsaKe5es2g'}, {'Haber': 'Cumhurbaşkanı Erdoğan,\xa0Azerbaycan Cumhurbaşkanı Aliyev ile görüştü', 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-azerbaycan-cumhurbaskani-aliyev-ile-gorustu,sXM2k0rFQUyeCqjV5BbGTQ'}, {'Haber': "Azerbaycan: Ermenistan'a ait iki SU-25 düşürüldü", 'Link': 'https://www.ntv.com.tr/dunya/son-dakika-haberi-azerbaycan-ermenistana-ait-iki-su-25-dusuruldu,mA05FnI0BEmncP3tXl8RdA'}, {'Haber': 'KYK burs başvurusu işlemleri başladı (KYK başvuruları ne zaman sona erecek?)', 'Link': 'https://www.ntv.com.tr/egitim/kyk-burs-basvurusu-islemleri-basladi-kyk-basvurulari-ne-zaman-sona-erecek,HLt8bu9DbEOnaSdn0dSZmw'}, {'Haber': "Medipol Başakşehir, Şampiyonlar Ligi'ndeki ikinci maçında da puanla tanışamadı", 'Link': 'https://www.ntv.com.tr/spor/son-dakika-basaksehir-evinde-psgye-boyun-egdi,Fa-afm0a7kKR6y5hyskRFg'}, {'Haber': "Fransa'da 30 Ekim itibarıyla sokağa çıkma kısıtlaması uygulanacak", 'Link': 'https://www.ntv.com.tr/dunya/son-dakika-haberi-fransada-30-ekim-itibariyla-sokaga-cikma-kisitlamasi-uygulanacak,z-K9bTbM_UyrdRED5Ef9Bw'}, {'Haber': "Sağlık Bakanı Koca'dan İstanbul'a uyarılar (Seyahat kısıtlaması olacak mı?)", 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-saglik-bakani-koca-konusuyor,b-LHq7Lbkkmp7gEjnklNHw'}, {'Haber': "Hatay'daki terör saldırısı girişimiyle ilgili 4 ilde 5 zanlı\xa0gözaltında", 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-hatayda-terorist-saldiri-girisimiyle-ilgili-4-ilde-5-zanli-gozaltina-alindi,g_BM_4KGMkSMp_ItO2nwUA'}, {'Haber': "Fransa’nın Ankara Büyükelçiliği Maslahatgüzarı Dışişleri Bakanlığı'na çağrıldı", 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberifransanin-ankara-buyukelciligi-maslahatguzari-disisleri-bakanligina-cagrildi,j6K-TsTpBkWUmADKfczyAQ'}, {'Haber': '28 Ekim 2020 corona virüs tablosu: 77 can kaybı, 2 bin 305 yeni hasta', 'Link': 'https://www.ntv.com.tr/turkiye/28-ekim-2020-corona-virus-tablosu-77-can-kaybi-2-bin-305-yeni-hasta,wHhHaSWSF0OSUNQwJ43b-g'}, {'Haber': 'Dolar kaç TL? / Dolar kuru bugün ne kadar? (28 Ekim 2020 dolar - euro fiyatları)', 'Link': 'https://www.ntv.com.tr/ekonomi/dolar-kac-tl-dolar-kuru-bugun-ne-kadar-28-ekim-2020-dolar-euro-fiyatlari,36JmpscvHEWnebHpvc6Vcg'}, {'Haber': 'Azerbaycan ordusu 13 köyü daha işgalden kurtardı', 'Link': 'https://www.ntv.com.tr/dunya/azerbaycan-ordusu-13-koyu-daha-isgalden-kurtardi,aXIaFg0kvE-7qZaAWMdEcQ'}, {'Haber': "Ermenistan Berde'yi vurdu", 'Link': 'https://www.ntv.com.tr/dunya/son-dakika-haberi-ermenistan-berdeyi-vurdu,qs9Xx4NOUUWMLgiy0bN7dQ'}, {'Haber': "Çavuşoğlu'ndan 'Paris elçisi geri çağrılacak mı' sorusuna\xa0yanıt", 'Link': 'https://www.ntv.com.tr/turkiye/cavusoglunda-paris-elcisi-geri-cagrilacak-mi-sorusunayanit,DZ-H2HCGM0-V3OXPD2PwAw'}, {'Haber': "Cumhurbaşkanı Erdoğan'dan saygısız karikatüre tepki", 'Link': 'https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogandan-saygisiz-karikature-tepki,3hB8BugSgEmhI-MUv2YsTg'}, {'Haber': 'Başsavcılıktan saygısız karikatür için soruşturma', 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-saygisiz-karikatur-hakkinda-sorusturma,kgRiUgSloEuhhxP2OBy31g'}, {'Haber': "Erzincan'da 4,3'lük deprem", 'Link': 'https://www.ntv.com.tr/turkiye/erzincanda-4-3luk-deprem,aQjHPqWDa0qk52yIAGLaBg'}, {'Haber': "Hava durumu: Meteoroloji'den kuvvetli yağış uyarısı (Bugün hava nasıl olacak?)", 'Link': 'https://www.ntv.com.tr/turkiye/hava-durumu-meteorolojiden-kuvvetli-yagis-uyarisi-bugun-hava-nasil-olacak,U7HaLGbIJEKyv0zNdw1bBQ'}, {'Haber': 'Batman ve Diyarbakır\'da "Yıldırım-14 Zori" operasyonu', 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-batman-ve-diyarbakirda-yildirim-14-zori-operasyonu,6TINK0VaB0OlWZakwj4Hmw'}, {'Haber': 'Çeyrek altın fiyatları bugün ne kadar?\xa028 Ekim\xa02020 anlık ve güncel altın kuru fiyatları', 'Link': 'https://www.ntv.com.tr/ekonomi/ceyrek-altin-fiyatlari-bugun-ne-kadar28-ekim2020-anlik-ve-guncel-altin-kuru-fiyatlari,xxleRErroka8n-BIY-rxzA'}, {'Haber': "Cumhurbaşkanı Erdoğan'dan 29 Ekim mesajı", 'Link': 'https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogandan-29-ekim-mesaji,UzuD3djE3UKXrBKTyVG-kQ'}, {'Haber': 'Bakan Albayrak: Fransız dergisini şiddetle kınıyorum', 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-albayrak-ahlaksizca-cumhurbaskanimiza-saldiran-fransiz-dergisini-siddetle-kiniyorum,hL12oeC3vUKgt-w2SxsaSg'}, {'Haber': 'Sahte içkiden 3 ölüm daha', 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-sahte-ickiden-3-olum-daha,mcXyVyrweUaYFkJohuFq3g'}, {'Haber': "FETÖ'nün Deniz Kuvvetleri ve Sahil Güvenlik yapılanmasına operasyon", 'Link': 'https://www.ntv.com.tr/turkiye/fetonun-deniz-kuvvetleri-ve-sahil-guvenlik-yapilanmasina-operasyon,JLMm-c0wN06xttjasr9p4A'}, {'Haber': "Ankara'da doğalgaz patlaması", 'Link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-ankarada-dogalgaz-patlamasi,BW66VpM-IkicNzPZBPSmXw'}, {'Haber': "SON DAKİKA:\xa0Ankara'da 3,8 büyüklüğünde deprem", 'Link': 'https://www.ntv.com.tr/turkiye/son-dakikaankarada-3-8-buyuklugunde-deprem-son-depremler,vLdaIMHEz0uU3JDjUJkM5w'}]}
    """

print(haber.gorsel())
    """
    Okunabilir JSON(str) Döndürür

    {
    "kaynak": "ntv.com.tr",
    "veri": [
        {
        "Haber": "Mesut Yılmaz hayatını kaybetti",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-mesut-yilmaz-hayatini-kaybetti,uUhAL55lZ0Wer3SRXwaXyw"
        },
        {
        "Haber": "Merkez Bankası'ndan yeni adım",
        "Link": "https://www.ntv.com.tr/ekonomi/son-dakika-haberi-merkez-bankasindan-yeni-adim,i5ytNXpMWkikhyVTMsPkAw"
        },
        {
        "Haber": "Çeyrek ve gram altın fiyatları bugün ne kadar oldu? 30 Ekim 2020 anlık ve güncel çeyrek altın kuru fiyatları",
        "Link": "https://www.ntv.com.tr/ekonomi/ceyrek-ve-gram-altin-fiyatlari-bugun-ne-kadar-oldu-30-ekim-2020-anlik-ve-guncel-ceyrek-altin-kuru-fiyatlari,MAlt1qPmdkSAWayZS9WECA"
        },
        {
        "Haber": "Dolar kaç TL? (30 Ekim 2020 dolar - euro fiyatları)",
        "Link": "https://www.ntv.com.tr/ekonomi/dolarkac-tl-30-ekim-2020-dolar-euro-fiyatlari,7cUHGwdKzE2mh8IKkdmnMw"
        },
        {
        "Haber": "2020 Yılı Cumhurbaşkanlığı Kültür ve Sanat Büyük Ödülleri'ne layık görülen isimler açıklandı",
        "Link": "https://www.ntv.com.tr/sanat/son-dakika-haberi2020-yili-cumhurbaskanligi-kultur-ve-sanat-buyuk-odullerine-layik-gorulen-isimler-aciklandi,phuDiX_3qUC-8VLjwsOamA"
        },
        {
        "Haber": "29 Ekim 2020 corona virüs tablosu: 72 can kaybı, 2 bin 319 yeni hasta",
        "Link": "https://www.ntv.com.tr/turkiye/29-ekim-2020-corona-virus-tablosu72-can-kaybi-2-319-yeni-hasta-sayisi,TReNnv_5VkawG5b_29RHIA"
        },
        {
        "Haber": "Cumhurbaşkanı Erdoğan: En büyük gücümüz tarihi mirasımızdır",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-konusuyor,CjkQF1OJK0-pNLSnrd4M8Q"
        },
        {
        "Haber": "İYİ Parti İstanbul Milletvekili Ümit Özdağ disipline sevk edildi",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberiiyi-parti-istanbul-milletvekili-umit-ozdag-disipline-sevk-edildi,_RY4y88SdE2hzvd-GgJeZw"
        },
        {
        "Haber": "MSB: 5 PKK/YPG'li terörist etkisiz hale getirildi",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-msb-5-pkk-ypgli-terorist-etkisiz-hale-getirildi,kY1HOFFo5Ei-hbbLkiTfPA"
        },
        {
        "Haber": "Türkiye'den Fransa'daki saldırıya kınama",
        "Link": "https://www.ntv.com.tr/turkiye/turkiyeden-fransadaki-saldiriya-kinama,ZcW7zg-wBka2phDu0lb0aw"
        },
        {
        "Haber": "Putin'den Dağlık Karabağ açıklaması",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-putinden-karabag-aciklamasi,4b5IoVqi-EapWsaKe5es2g"
        },
        {
        "Haber": "Cumhurbaşkanı Erdoğan, Azerbaycan Cumhurbaşkanı Aliyev ile görüştü",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-azerbaycan-cumhurbaskani-aliyev-ile-gorustu,sXM2k0rFQUyeCqjV5BbGTQ"
        },
        {
        "Haber": "Azerbaycan: Ermenistan'a ait iki SU-25 düşürüldü",
        "Link": "https://www.ntv.com.tr/dunya/son-dakika-haberi-azerbaycan-ermenistana-ait-iki-su-25-dusuruldu,mA05FnI0BEmncP3tXl8RdA"
        },
        {
        "Haber": "KYK burs başvurusu işlemleri başladı (KYK başvuruları ne zaman sona erecek?)",
        "Link": "https://www.ntv.com.tr/egitim/kyk-burs-basvurusu-islemleri-basladi-kyk-basvurulari-ne-zaman-sona-erecek,HLt8bu9DbEOnaSdn0dSZmw"
        },
        {
        "Haber": "Medipol Başakşehir, Şampiyonlar Ligi'ndeki ikinci maçında da puanla tanışamadı",
        "Link": "https://www.ntv.com.tr/spor/son-dakika-basaksehir-evinde-psgye-boyun-egdi,Fa-afm0a7kKR6y5hyskRFg"
        },
        {
        "Haber": "Fransa'da 30 Ekim itibarıyla sokağa çıkma kısıtlaması uygulanacak",
        "Link": "https://www.ntv.com.tr/dunya/son-dakika-haberi-fransada-30-ekim-itibariyla-sokaga-cikma-kisitlamasi-uygulanacak,z-K9bTbM_UyrdRED5Ef9Bw"
        },
        {
        "Haber": "Sağlık Bakanı Koca'dan İstanbul'a uyarılar (Seyahat kısıtlaması olacak mı?)",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-saglik-bakani-koca-konusuyor,b-LHq7Lbkkmp7gEjnklNHw"
        },
        {
        "Haber": "Hatay'daki terör saldırısı girişimiyle ilgili 4 ilde 5 zanlı gözaltında",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-hatayda-terorist-saldiri-girisimiyle-ilgili-4-ilde-5-zanli-gozaltina-alindi,g_BM_4KGMkSMp_ItO2nwUA"
        },
        {
        "Haber": "Fransa’nın Ankara Büyükelçiliği Maslahatgüzarı Dışişleri Bakanlığı'na çağrıldı",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberifransanin-ankara-buyukelciligi-maslahatguzari-disisleri-bakanligina-cagrildi,j6K-TsTpBkWUmADKfczyAQ"
        },
        {
        "Haber": "28 Ekim 2020 corona virüs tablosu: 77 can kaybı, 2 bin 305 yeni hasta",
        "Link": "https://www.ntv.com.tr/turkiye/28-ekim-2020-corona-virus-tablosu-77-can-kaybi-2-bin-305-yeni-hasta,wHhHaSWSF0OSUNQwJ43b-g"
        },
        {
        "Haber": "Dolar kaç TL? / Dolar kuru bugün ne kadar? (28 Ekim 2020 dolar - euro fiyatları)",
        "Link": "https://www.ntv.com.tr/ekonomi/dolar-kac-tl-dolar-kuru-bugun-ne-kadar-28-ekim-2020-dolar-euro-fiyatlari,36JmpscvHEWnebHpvc6Vcg"
        },
        {
        "Haber": "Azerbaycan ordusu 13 köyü daha işgalden kurtardı",
        "Link": "https://www.ntv.com.tr/dunya/azerbaycan-ordusu-13-koyu-daha-isgalden-kurtardi,aXIaFg0kvE-7qZaAWMdEcQ"
        },
        {
        "Haber": "Ermenistan Berde'yi vurdu",
        "Link": "https://www.ntv.com.tr/dunya/son-dakika-haberi-ermenistan-berdeyi-vurdu,qs9Xx4NOUUWMLgiy0bN7dQ"
        },
        {
        "Haber": "Çavuşoğlu'ndan 'Paris elçisi geri çağrılacak mı' sorusuna yanıt",
        "Link": "https://www.ntv.com.tr/turkiye/cavusoglunda-paris-elcisi-geri-cagrilacak-mi-sorusunayanit,DZ-H2HCGM0-V3OXPD2PwAw"
        },
        {
        "Haber": "Cumhurbaşkanı Erdoğan'dan saygısız karikatüre tepki",
        "Link": "https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogandan-saygisiz-karikature-tepki,3hB8BugSgEmhI-MUv2YsTg"
        },
        {
        "Haber": "Başsavcılıktan saygısız karikatür için soruşturma",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-saygisiz-karikatur-hakkinda-sorusturma,kgRiUgSloEuhhxP2OBy31g"
        },
        {
        "Haber": "Erzincan'da 4,3'lük deprem",
        "Link": "https://www.ntv.com.tr/turkiye/erzincanda-4-3luk-deprem,aQjHPqWDa0qk52yIAGLaBg"
        },
        {
        "Haber": "Hava durumu: Meteoroloji'den kuvvetli yağış uyarısı (Bugün hava nasıl olacak?)",
        "Link": "https://www.ntv.com.tr/turkiye/hava-durumu-meteorolojiden-kuvvetli-yagis-uyarisi-bugun-hava-nasil-olacak,U7HaLGbIJEKyv0zNdw1bBQ"
        },
        {
        "Haber": "Batman ve Diyarbakır'da \"Yıldırım-14 Zori\" operasyonu",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-batman-ve-diyarbakirda-yildirim-14-zori-operasyonu,6TINK0VaB0OlWZakwj4Hmw"
        },
        {
        "Haber": "Çeyrek altın fiyatları bugün ne kadar? 28 Ekim 2020 anlık ve güncel altın kuru fiyatları",
        "Link": "https://www.ntv.com.tr/ekonomi/ceyrek-altin-fiyatlari-bugun-ne-kadar28-ekim2020-anlik-ve-guncel-altin-kuru-fiyatlari,xxleRErroka8n-BIY-rxzA"
        },
        {
        "Haber": "Cumhurbaşkanı Erdoğan'dan 29 Ekim mesajı",
        "Link": "https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogandan-29-ekim-mesaji,UzuD3djE3UKXrBKTyVG-kQ"
        },
        {
        "Haber": "Bakan Albayrak: Fransız dergisini şiddetle kınıyorum",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-albayrak-ahlaksizca-cumhurbaskanimiza-saldiran-fransiz-dergisini-siddetle-kiniyorum,hL12oeC3vUKgt-w2SxsaSg"
        },
        {
        "Haber": "Sahte içkiden 3 ölüm daha",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-sahte-ickiden-3-olum-daha,mcXyVyrweUaYFkJohuFq3g"
        },
        {
        "Haber": "FETÖ'nün Deniz Kuvvetleri ve Sahil Güvenlik yapılanmasına operasyon",
        "Link": "https://www.ntv.com.tr/turkiye/fetonun-deniz-kuvvetleri-ve-sahil-guvenlik-yapilanmasina-operasyon,JLMm-c0wN06xttjasr9p4A"
        },
        {
        "Haber": "Ankara'da doğalgaz patlaması",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-ankarada-dogalgaz-patlamasi,BW66VpM-IkicNzPZBPSmXw"
        },
        {
        "Haber": "SON DAKİKA: Ankara'da 3,8 büyüklüğünde deprem",
        "Link": "https://www.ntv.com.tr/turkiye/son-dakikaankarada-3-8-buyuklugunde-deprem-son-depremler,vLdaIMHEz0uU3JDjUJkM5w"
        }
    ]
    }
    """

print(haber.tablo())
    """
    Tabulate(str) Döndürür

    +--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Haber                                                                                                        | Link                                                                                                                                                              |
    |--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Mesut Yılmaz hayatını kaybetti                                                                               | https://www.ntv.com.tr/turkiye/son-dakika-haberi-mesut-yilmaz-hayatini-kaybetti,uUhAL55lZ0Wer3SRXwaXyw                                                            |
    | Merkez Bankası'ndan yeni adım                                                                                | https://www.ntv.com.tr/ekonomi/son-dakika-haberi-merkez-bankasindan-yeni-adim,i5ytNXpMWkikhyVTMsPkAw                                                              |
    | Çeyrek ve gram altın fiyatları bugün ne kadar oldu? 30 Ekim 2020 anlık ve güncel çeyrek altın kuru fiyatları | https://www.ntv.com.tr/ekonomi/ceyrek-ve-gram-altin-fiyatlari-bugun-ne-kadar-oldu-30-ekim-2020-anlik-ve-guncel-ceyrek-altin-kuru-fiyatlari,MAlt1qPmdkSAWayZS9WECA |
    | Dolar kaç TL? (30 Ekim 2020 dolar - euro fiyatları)                                                          | https://www.ntv.com.tr/ekonomi/dolarkac-tl-30-ekim-2020-dolar-euro-fiyatlari,7cUHGwdKzE2mh8IKkdmnMw                                                               |
    | 2020 Yılı Cumhurbaşkanlığı Kültür ve Sanat Büyük Ödülleri'ne layık görülen isimler açıklandı                 | https://www.ntv.com.tr/sanat/son-dakika-haberi2020-yili-cumhurbaskanligi-kultur-ve-sanat-buyuk-odullerine-layik-gorulen-isimler-aciklandi,phuDiX_3qUC-8VLjwsOamA  |
    | 29 Ekim 2020 corona virüs tablosu: 72 can kaybı, 2 bin 319 yeni hasta                                        | https://www.ntv.com.tr/turkiye/29-ekim-2020-corona-virus-tablosu72-can-kaybi-2-319-yeni-hasta-sayisi,TReNnv_5VkawG5b_29RHIA                                       |
    | Cumhurbaşkanı Erdoğan: En büyük gücümüz tarihi mirasımızdır                                                  | https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-konusuyor,CjkQF1OJK0-pNLSnrd4M8Q                                                           |
    | İYİ Parti İstanbul Milletvekili Ümit Özdağ disipline sevk edildi                                             | https://www.ntv.com.tr/turkiye/son-dakika-haberiiyi-parti-istanbul-milletvekili-umit-ozdag-disipline-sevk-edildi,_RY4y88SdE2hzvd-GgJeZw                           |
    | MSB: 5 PKK/YPG'li terörist etkisiz hale getirildi                                                            | https://www.ntv.com.tr/turkiye/son-dakika-haberi-msb-5-pkk-ypgli-terorist-etkisiz-hale-getirildi,kY1HOFFo5Ei-hbbLkiTfPA                                           |
    | Türkiye'den Fransa'daki saldırıya kınama                                                                     | https://www.ntv.com.tr/turkiye/turkiyeden-fransadaki-saldiriya-kinama,ZcW7zg-wBka2phDu0lb0aw                                                                      |
    | Putin'den Dağlık Karabağ açıklaması                                                                          | https://www.ntv.com.tr/turkiye/son-dakika-haberi-putinden-karabag-aciklamasi,4b5IoVqi-EapWsaKe5es2g                                                               |
    | Cumhurbaşkanı Erdoğan, Azerbaycan Cumhurbaşkanı Aliyev ile görüştü                                           | https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-azerbaycan-cumhurbaskani-aliyev-ile-gorustu,sXM2k0rFQUyeCqjV5BbGTQ                         |
    | Azerbaycan: Ermenistan'a ait iki SU-25 düşürüldü                                                             | https://www.ntv.com.tr/dunya/son-dakika-haberi-azerbaycan-ermenistana-ait-iki-su-25-dusuruldu,mA05FnI0BEmncP3tXl8RdA                                              |
    | KYK burs başvurusu işlemleri başladı (KYK başvuruları ne zaman sona erecek?)                                 | https://www.ntv.com.tr/egitim/kyk-burs-basvurusu-islemleri-basladi-kyk-basvurulari-ne-zaman-sona-erecek,HLt8bu9DbEOnaSdn0dSZmw                                    |
    | Medipol Başakşehir, Şampiyonlar Ligi'ndeki ikinci maçında da puanla tanışamadı                               | https://www.ntv.com.tr/spor/son-dakika-basaksehir-evinde-psgye-boyun-egdi,Fa-afm0a7kKR6y5hyskRFg                                                                  |
    | Fransa'da 30 Ekim itibarıyla sokağa çıkma kısıtlaması uygulanacak                                            | https://www.ntv.com.tr/dunya/son-dakika-haberi-fransada-30-ekim-itibariyla-sokaga-cikma-kisitlamasi-uygulanacak,z-K9bTbM_UyrdRED5Ef9Bw                            |
    | Sağlık Bakanı Koca'dan İstanbul'a uyarılar (Seyahat kısıtlaması olacak mı?)                                  | https://www.ntv.com.tr/turkiye/son-dakika-haberi-saglik-bakani-koca-konusuyor,b-LHq7Lbkkmp7gEjnklNHw                                                              |
    | Hatay'daki terör saldırısı girişimiyle ilgili 4 ilde 5 zanlı gözaltında                                      | https://www.ntv.com.tr/turkiye/son-dakika-haberi-hatayda-terorist-saldiri-girisimiyle-ilgili-4-ilde-5-zanli-gozaltina-alindi,g_BM_4KGMkSMp_ItO2nwUA               |
    | Fransa’nın Ankara Büyükelçiliği Maslahatgüzarı Dışişleri Bakanlığı'na çağrıldı                               | https://www.ntv.com.tr/turkiye/son-dakika-haberifransanin-ankara-buyukelciligi-maslahatguzari-disisleri-bakanligina-cagrildi,j6K-TsTpBkWUmADKfczyAQ               |
    | 28 Ekim 2020 corona virüs tablosu: 77 can kaybı, 2 bin 305 yeni hasta                                        | https://www.ntv.com.tr/turkiye/28-ekim-2020-corona-virus-tablosu-77-can-kaybi-2-bin-305-yeni-hasta,wHhHaSWSF0OSUNQwJ43b-g                                         |
    | Dolar kaç TL? / Dolar kuru bugün ne kadar? (28 Ekim 2020 dolar - euro fiyatları)                             | https://www.ntv.com.tr/ekonomi/dolar-kac-tl-dolar-kuru-bugun-ne-kadar-28-ekim-2020-dolar-euro-fiyatlari,36JmpscvHEWnebHpvc6Vcg                                    |
    | Azerbaycan ordusu 13 köyü daha işgalden kurtardı                                                             | https://www.ntv.com.tr/dunya/azerbaycan-ordusu-13-koyu-daha-isgalden-kurtardi,aXIaFg0kvE-7qZaAWMdEcQ                                                              |
    | Ermenistan Berde'yi vurdu                                                                                    | https://www.ntv.com.tr/dunya/son-dakika-haberi-ermenistan-berdeyi-vurdu,qs9Xx4NOUUWMLgiy0bN7dQ                                                                    |
    | Çavuşoğlu'ndan 'Paris elçisi geri çağrılacak mı' sorusuna yanıt                                              | https://www.ntv.com.tr/turkiye/cavusoglunda-paris-elcisi-geri-cagrilacak-mi-sorusunayanit,DZ-H2HCGM0-V3OXPD2PwAw                                                  |
    | Cumhurbaşkanı Erdoğan'dan saygısız karikatüre tepki                                                          | https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogandan-saygisiz-karikature-tepki,3hB8BugSgEmhI-MUv2YsTg                                                          |
    | Başsavcılıktan saygısız karikatür için soruşturma                                                            | https://www.ntv.com.tr/turkiye/son-dakika-haberi-saygisiz-karikatur-hakkinda-sorusturma,kgRiUgSloEuhhxP2OBy31g                                                    |
    | Erzincan'da 4,3'lük deprem                                                                                   | https://www.ntv.com.tr/turkiye/erzincanda-4-3luk-deprem,aQjHPqWDa0qk52yIAGLaBg                                                                                    |
    | Hava durumu: Meteoroloji'den kuvvetli yağış uyarısı (Bugün hava nasıl olacak?)                               | https://www.ntv.com.tr/turkiye/hava-durumu-meteorolojiden-kuvvetli-yagis-uyarisi-bugun-hava-nasil-olacak,U7HaLGbIJEKyv0zNdw1bBQ                                   |
    | Batman ve Diyarbakır'da "Yıldırım-14 Zori" operasyonu                                                        | https://www.ntv.com.tr/turkiye/son-dakika-haberi-batman-ve-diyarbakirda-yildirim-14-zori-operasyonu,6TINK0VaB0OlWZakwj4Hmw                                        |
    | Çeyrek altın fiyatları bugün ne kadar? 28 Ekim 2020 anlık ve güncel altın kuru fiyatları                     | https://www.ntv.com.tr/ekonomi/ceyrek-altin-fiyatlari-bugun-ne-kadar28-ekim2020-anlik-ve-guncel-altin-kuru-fiyatlari,xxleRErroka8n-BIY-rxzA                       |
    | Cumhurbaşkanı Erdoğan'dan 29 Ekim mesajı                                                                     | https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogandan-29-ekim-mesaji,UzuD3djE3UKXrBKTyVG-kQ                                                                     |
    | Bakan Albayrak: Fransız dergisini şiddetle kınıyorum                                                         | https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-albayrak-ahlaksizca-cumhurbaskanimiza-saldiran-fransiz-dergisini-siddetle-kiniyorum,hL12oeC3vUKgt-w2SxsaSg |
    | Sahte içkiden 3 ölüm daha                                                                                    | https://www.ntv.com.tr/turkiye/son-dakika-haberi-sahte-ickiden-3-olum-daha,mcXyVyrweUaYFkJohuFq3g                                                                 |
    | FETÖ'nün Deniz Kuvvetleri ve Sahil Güvenlik yapılanmasına operasyon                                          | https://www.ntv.com.tr/turkiye/fetonun-deniz-kuvvetleri-ve-sahil-guvenlik-yapilanmasina-operasyon,JLMm-c0wN06xttjasr9p4A                                          |
    | Ankara'da doğalgaz patlaması                                                                                 | https://www.ntv.com.tr/turkiye/son-dakika-haberi-ankarada-dogalgaz-patlamasi,BW66VpM-IkicNzPZBPSmXw                                                               |
    | SON DAKİKA: Ankara'da 3,8 büyüklüğünde deprem                                                                | https://www.ntv.com.tr/turkiye/son-dakikaankarada-3-8-buyuklugunde-deprem-son-depremler,vLdaIMHEz0uU3JDjUJkM5w                                                    |
    +--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    """

print(haber.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['Haber', 'Link']
    """
```

### ☁️ HavaDurumu

```python
from KekikSpatula import HavaDurumu

hava = HavaDurumu('Çanakkale', 'Merkez')

print(hava.veri())
    """
    JSON(dict) Veri Döndürür

    {'kaynak': 'google.com', 'veri': [{'gun': 'Cuma 20:53', 'yer': 'Çanakkale Merkez', 'derece': 'Çok bulutlu 14°C'}]}
    """

print(hava.gorsel())
    """
    Okunabilir JSON(str) Döndürür

    {
    "kaynak": "google.com",
    "veri": [
        {
        "gun": "Cuma 20:53",
        "yer": "Çanakkale Merkez",
        "derece": "Çok bulutlu 14°C"
        }
    ]
    }
    """

print(hava.tablo())
    """
    Tabulate(str) Döndürür

    +------------+------------------+------------------+
    | gun        | yer              | derece           |
    |------------+------------------+------------------|
    | Cuma 20:53 | Çanakkale Merkez | Çok bulutlu 14°C |
    +------------+------------------+------------------+
    """

print(hava.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['gun', 'yer', 'derece']
    """
```

### 🕌 Ezan

```python
from KekikSpatula import Ezan

ezan = Ezan('İstanbul')

print(ezan.veri())
    """
    JSON(dict) Veri Döndürür

    {'kaynak': 'sabah.com.tr', 'veri': [{'il': 'Istanbul', 'imsak': '06:00', 'gunes': '07:26', 'ogle': '12:53', 'ikindi': '15:42', 'aksam': '18:10', 'yatsi': '19:30'}]}
    """

print(ezan.gorsel())
    """
    Okunabilir JSON(str) Döndürür

    {
    "kaynak": "sabah.com.tr",
    "veri": [
        {
        "il": "Istanbul",
        "imsak": "06:00",
        "gunes": "07:26",
        "ogle": "12:53",
        "ikindi": "15:42",
        "aksam": "18:10",
        "yatsi": "19:30"
        }
    ]
    }
    """

print(ezan.tablo())
    """
    Tabulate(str) Döndürür

    +----------+---------+---------+--------+----------+---------+---------+
    | il       | imsak   | gunes   | ogle   | ikindi   | aksam   | yatsi   |
    |----------+---------+---------+--------+----------+---------+---------|
    | Istanbul | 06:00   | 07:26   | 12:53  | 15:42    | 18:10   | 19:30   |
    +----------+---------+---------+--------+----------+---------+---------+
    """

print(ezan.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['il', 'imsak', 'gunes', 'ogle', 'ikindi', 'aksam', 'yatsi']
    """
```

### 📺 DiscUdemy

```python
from KekikSpatula import DiscUdemy

udemy = DiscUdemy('Python')

print(udemy.veri())
    """
    JSON(dict) Veri Döndürür

    {'kaynak': 'discudemy.com', 'veri': [{'dil': 'English', 'baslik': 'Python-3 Boot Camp in GUI automation for absolute beginners | [LQ]', 'baglanti': 'https://www.udemy.com/course/python-3-boot-camp-in-gui-automation-for-absolute-beginners/?couponCode=17AC8721C666BB7E6710'}, {'dil': 'English', 'baslik': 'Hands on Python3 Regular Expressions for Absolute Beginners', 'baglanti': 'https://www.udemy.com/course/hands-on-python3-regular-expression-2020/?couponCode=0E676A889BA3CAEAE08C'}, {'dil': 'Portuguese', 'baslik': 'Machine Learning e Data Science com Python de A a Z', 'baglanti': 'https://www.udemy.com/course/machine-learning-e-data-science-com-python-y/?couponCode=IAEXPERTMLPFREE'}, {'dil': 'Turkish', 'baslik': 'Python Temel Eğitim Seti', 'baglanti': 'https://www.udemy.com/course/python-temel-egitim-seti/'}, {'dil': 'English', 'baslik': 'Automate the Boring Stuff with Python Programming', 'baglanti': 'https://www.udemy.com/course/automate/?couponCode=NOV2020FREE2'}, {'dil': 'English', 'baslik': 'Python for Beginners:Introduction to Python', 'baglanti': 'https://www.udemy.com/course/python-crash-course-for-beginners-l/?couponCode=6357A09370F9974153C2'}, {'dil': 'English', 'baslik': 'Python And Flask Framework Complete Course For Beginners', 'baglanti': 'https://www.udemy.com/course/python-for-beginners-course-/?couponCode=DEA08795957534B227AF'}, {'dil': 'English', 'baslik': 'Data Science for Sports - Analyze and Visualize Sports Data', 'baglanti': 'https://www.udemy.com/course/data-science-for-sports/?couponCode=TCRFREECOUPON'}, {'dil': 'English', 'baslik': 'Python Programming Tutorial For The Absolute Beginner + Code | [LQ]', 'baglanti': 'https://www.udemy.com/course/python-programming-tutorial-for-the-absolute-beginner-code-included/?couponCode=16B720317BECEFEA284E'}, {'dil': 'English', 'baslik': 'Python And Django Framework For Beginners Complete Course', 'baglanti': 'https://www.udemy.com/course/python-and-django-for-beginners/?couponCode=5680B2C7FC0FBFB690B4'}, {'dil': 'English', 'baslik': 'Building an IMDB clone with Python (Flask) and Neo4j', 'baglanti': 'https://www.udemy.com/course/building-an-imdb-clone-with-python-flask-and-neo4j/'}, {'dil': 'English', 'baslik': 'Implementation of ML Algorithm Using Python', 'baglanti': 'https://www.udemy.com/course/implementation-of-ml-algorithm-using-python/'}, {'dil': 'English', 'baslik': 'Introduction To Computer Science With Python Part 1', 'baglanti': 'https://www.udemy.com/course/introduction-to-computer-science-with-python/'}, {'dil': 'English', 'baslik': 'Python For Data Science - For Absolute Beginners', 'baglanti': 'https://www.udemy.com/course/python-for-data-science-for-absolute-beginners/'}, {'dil': 'English', 'baslik': 'Machine Learning & Data Science Foundations Masterclass', 'baglanti': 'https://www.udemy.com/course/machine-learning-data-science-foundations-masterclass/?couponCode=CLUB11'}]}
    """

print(udemy.gorsel())
    """
    Okunabilir JSON(str) Döndürür

    {
    "kaynak": "discudemy.com",
    "veri": [
        {
        "dil": "English",
        "baslik": "Python-3 Boot Camp in GUI automation for absolute beginners | [LQ]",
        "baglanti": "https://www.udemy.com/course/python-3-boot-camp-in-gui-automation-for-absolute-beginners/?couponCode=17AC8721C666BB7E6710"
        },
        {
        "dil": "English",
        "baslik": "Hands on Python3 Regular Expressions for Absolute Beginners",
        "baglanti": "https://www.udemy.com/course/hands-on-python3-regular-expression-2020/?couponCode=0E676A889BA3CAEAE08C"
        },
        {
        "dil": "Portuguese",
        "baslik": "Machine Learning e Data Science com Python de A a Z",
        "baglanti": "https://www.udemy.com/course/machine-learning-e-data-science-com-python-y/?couponCode=IAEXPERTMLPFREE"
        },
        {
        "dil": "Turkish",
        "baslik": "Python Temel Eğitim Seti",
        "baglanti": "https://www.udemy.com/course/python-temel-egitim-seti/"
        },
        {
        "dil": "English",
        "baslik": "Automate the Boring Stuff with Python Programming",
        "baglanti": "https://www.udemy.com/course/automate/?couponCode=NOV2020FREE2"
        },
        {
        "dil": "English",
        "baslik": "Python for Beginners:Introduction to Python",
        "baglanti": "https://www.udemy.com/course/python-crash-course-for-beginners-l/?couponCode=6357A09370F9974153C2"
        },
        {
        "dil": "English",
        "baslik": "Python And Flask Framework Complete Course For Beginners",
        "baglanti": "https://www.udemy.com/course/python-for-beginners-course-/?couponCode=DEA08795957534B227AF"
        },
        {
        "dil": "English",
        "baslik": "Data Science for Sports - Analyze and Visualize Sports Data",
        "baglanti": "https://www.udemy.com/course/data-science-for-sports/?couponCode=TCRFREECOUPON"
        },
        {
        "dil": "English",
        "baslik": "Python Programming Tutorial For The Absolute Beginner + Code | [LQ]",
        "baglanti": "https://www.udemy.com/course/python-programming-tutorial-for-the-absolute-beginner-code-included/?couponCode=16B720317BECEFEA284E"
        },
        {
        "dil": "English",
        "baslik": "Python And Django Framework For Beginners Complete Course",
        "baglanti": "https://www.udemy.com/course/python-and-django-for-beginners/?couponCode=5680B2C7FC0FBFB690B4"
        },
        {
        "dil": "English",
        "baslik": "Building an IMDB clone with Python (Flask) and Neo4j",
        "baglanti": "https://www.udemy.com/course/building-an-imdb-clone-with-python-flask-and-neo4j/"
        },
        {
        "dil": "English",
        "baslik": "Implementation of ML Algorithm Using Python",
        "baglanti": "https://www.udemy.com/course/implementation-of-ml-algorithm-using-python/"
        },
        {
        "dil": "English",
        "baslik": "Introduction To Computer Science With Python Part 1",
        "baglanti": "https://www.udemy.com/course/introduction-to-computer-science-with-python/"
        },
        {
        "dil": "English",
        "baslik": "Python For Data Science - For Absolute Beginners",
        "baglanti": "https://www.udemy.com/course/python-for-data-science-for-absolute-beginners/"
        },
        {
        "dil": "English",
        "baslik": "Machine Learning & Data Science Foundations Masterclass",
        "baglanti": "https://www.udemy.com/course/machine-learning-data-science-foundations-masterclass/?couponCode=CLUB11"
        }
    ]
    }
    """

print(udemy.tablo())
    """
    Tabulate(str) Döndürür

    +------------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | dil        | baslik                                                              | baglanti                                                                                                                          |
    |------------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------|
    | English    | Python-3 Boot Camp in GUI automation for absolute beginners | [LQ]  | https://www.udemy.com/course/python-3-boot-camp-in-gui-automation-for-absolute-beginners/?couponCode=17AC8721C666BB7E6710         |
    | English    | Hands on Python3 Regular Expressions for Absolute Beginners         | https://www.udemy.com/course/hands-on-python3-regular-expression-2020/?couponCode=0E676A889BA3CAEAE08C                            |
    | Portuguese | Machine Learning e Data Science com Python de A a Z                 | https://www.udemy.com/course/machine-learning-e-data-science-com-python-y/?couponCode=IAEXPERTMLPFREE                             |
    | Turkish    | Python Temel Eğitim Seti                                            | https://www.udemy.com/course/python-temel-egitim-seti/                                                                            |
    | English    | Automate the Boring Stuff with Python Programming                   | https://www.udemy.com/course/automate/?couponCode=NOV2020FREE2                                                                    |
    | English    | Python for Beginners:Introduction to Python                         | https://www.udemy.com/course/python-crash-course-for-beginners-l/?couponCode=6357A09370F9974153C2                                 |
    | English    | Python And Flask Framework Complete Course For Beginners            | https://www.udemy.com/course/python-for-beginners-course-/?couponCode=DEA08795957534B227AF                                        |
    | English    | Data Science for Sports - Analyze and Visualize Sports Data         | https://www.udemy.com/course/data-science-for-sports/?couponCode=TCRFREECOUPON                                                    |
    | English    | Python Programming Tutorial For The Absolute Beginner + Code | [LQ] | https://www.udemy.com/course/python-programming-tutorial-for-the-absolute-beginner-code-included/?couponCode=16B720317BECEFEA284E |
    | English    | Python And Django Framework For Beginners Complete Course           | https://www.udemy.com/course/python-and-django-for-beginners/?couponCode=5680B2C7FC0FBFB690B4                                     |
    | English    | Building an IMDB clone with Python (Flask) and Neo4j                | https://www.udemy.com/course/building-an-imdb-clone-with-python-flask-and-neo4j/                                                  |
    | English    | Implementation of ML Algorithm Using Python                         | https://www.udemy.com/course/implementation-of-ml-algorithm-using-python/                                                         |
    | English    | Introduction To Computer Science With Python Part 1                 | https://www.udemy.com/course/introduction-to-computer-science-with-python/                                                        |
    | English    | Python For Data Science - For Absolute Beginners                    | https://www.udemy.com/course/python-for-data-science-for-absolute-beginners/                                                      |
    | English    | Machine Learning & Data Science Foundations Masterclass             | https://www.udemy.com/course/machine-learning-data-science-foundations-masterclass/?couponCode=CLUB11                             |
    +------------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    """

print(udemy.anahtarlar())
    """
    Anahtarları(list) Döndürür

    ['dil', 'baslik', 'baglanti']
    """
```

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2020 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/keyifUserBot/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/keyiflerolsun)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*