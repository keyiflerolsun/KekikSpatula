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
pip install KekikSpatula
```

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

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2020 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/keyifUserBot/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/keyiflerolsun)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*