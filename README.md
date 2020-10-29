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

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2020 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/keyifUserBot/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/keyiflerolsun)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*