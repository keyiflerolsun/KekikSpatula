# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

class SonDakika(object):
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
    """
    def __init__(self):
        """son dakika verilerini ntv.com.tr'den alarak bs4'ile ayrıştırır."""
        super().__init__()

        kaynak  = "ntv.com.tr"
        url     = "https://www.ntv.com.tr/son-dakika"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        istek   = requests.get(url, headers=kimlik)

        corba   = BeautifulSoup(istek.content, "lxml")

        json = {"kaynak": kaynak, 'veri' : []}

        for tablo in corba.findAll("ul", class_="gallery-page-video-list-items"):
            haber_manset = tablo.findAll("div", class_="card card--md")
            for haber in haber_manset:
                json['veri'].append(
                    {
                        "Haber": haber.p.text.replace('SON DAKİKA HABERİ:', '').replace(' | Son depremler', '').replace('SON DAKİKA: ', '').strip(),
                        "Link": "https://www.ntv.com.tr" + haber.a['href'],
                    }
                )

        self.json  = json if json['veri'] != [] else None

    def veri(self):
        """json verisi döndürür."""
        return self.json or None

    def gorsel(self, girinti:int=2, alfabetik:bool=False):
        """oluşan json verisini insanın okuyabileceği formatta döndürür."""
        return json.dumps(self.json, indent=girinti, sort_keys=alfabetik, ensure_ascii=False) if self.json else None

    def tablo(self, tablo_turu:str='psql'):
        """tabulate verisi döndürür."""
        return tabulate(self.json['veri'], headers='keys', tablefmt=tablo_turu) if self.json else None

    def anahtarlar(self):
        """kullanılan anahtar listesini döndürür."""
        return [anahtar for anahtar in self.json['veri'][0].keys()] if self.json else None