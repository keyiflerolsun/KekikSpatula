# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import Statik

class SonDakika(Statik):
    """
    SonDakika : ntv.com.tr adresinden son dakika verilerini hazır formatlarda elinize verir.

    Methodlar
    ----------
        .veri()         -> dict:
            json verisi döndürür.

        .gorsel()       -> str:
            oluşan json verisini insanın okuyabileceği formatta döndürür.

        .tablo()        -> str:
            tabulate verisi döndürür.

        .anahtarlar()   -> list:
            kullanılan anahtar listesini döndürür.

        .nesne()        -> Object:
            json verisini python nesnesine dönüştürür.
    """
    def __init__(self):
        "son dakika verilerini ntv.com.tr'den alarak bs4'ile ayrıştırır."

        kaynak  = "ntv.com.tr"
        url     = "https://www.ntv.com.tr/son-dakika"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        istek   = requests.get(url, headers=kimlik)

        corba   = BeautifulSoup(istek.content, "lxml")

        kekik_json = {"kaynak": kaynak, 'veri' : []}

        for tablo in corba.findAll("ul", class_="gallery-page-video-list-items"):
            haber_manset = tablo.findAll("div", class_="card card--md")
            for haber in haber_manset:
                kekik_json['veri'].append(
                    {
                        "Haber": haber.p.text.replace('SON DAKİKA HABERİ:', '').replace(' | Son depremler', '').replace('SON DAKİKA: ', '').strip(),
                        "Link": "https://www.ntv.com.tr" + haber.a['href'],
                    }
                )

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None