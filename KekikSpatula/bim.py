# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import KekikSpatula

class BimAktuel(KekikSpatula):
    """
    BimAktuel : bim.com.tr adresinden aktüel verilerini hazır formatlarda elinize verir.

    Methodlar
    ----------
        .veri         -> dict:
            json verisi döndürür.

        .gorsel()       -> str:
            oluşan json verisini insanın okuyabileceği formatta döndürür.

        .tablo()        -> str:
            tabulate verisi döndürür.

        .anahtarlar   -> list:
            kullanılan anahtar listesini döndürür.

        .nesne        -> Object:
            json verisini python nesnesine dönüştürür.
    """
    def __init__(self):
        "aktüel verilerini bim.com.tr'den alarak bs4'ile ayrıştırır."

        kaynak  = "bim.com.tr"
        url     = "https://www.bim.com.tr/default.aspx"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        istek   = requests.get(url, headers=kimlik, allow_redirects=True)

        corba   = BeautifulSoup(istek.content, "lxml")

        tarih       = corba.find('a', class_='active subButton').text.strip()
        urun_alani  = corba.find('div', class_='productArea')

        urun_rerero = []
        host = 'https://www.bim.com.tr'
        for urun in urun_alani.findAll('div', class_='inner'):
            try:
                urun_basligi    = urun.find('h2', class_='title').text.strip()
                urun_linki      = host + urun.a['href']
                urun_gorseli    = host + urun.img['src'].replace(' ', '%20')
                urun_fiyati     = urun.find('a', class_='gButton triangle').text.strip()

                urun_rerero.append({
                    "urun_baslik"   : urun_basligi,
                    "urun_link"     : urun_linki,
                    "urun_gorsel"   : urun_gorseli,
                    "urun_fiyat"    : urun_fiyati
                })
            except (AttributeError, KeyError):
                continue

        kekik_json = {"kaynak": kaynak, 'tarih': tarih, 'veri' : urun_rerero}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak

    def __repr__(self):
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den aktüel verilerini döndürmesi için yazılmıştır.."