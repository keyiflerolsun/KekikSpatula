# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate


class Akaryakit(object):
    """Akaryakit : finans.haberler.com adresinden akaryakıt verilerini hazır formatlarda elinize verir.

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
        """akaryakıt finans.haberler.com'dan alarak bs4'ile ayrıştırır."""
        super().__init__()

        kaynak  = "finans.haberler.com"
        url     = "https://finans.haberler.com/akaryakit/"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        istek   = requests.get(url, headers=kimlik)

        corba   = BeautifulSoup(istek.content, "lxml")

        son_guncellenme = corba.select('body > div > div.hbMain.stickyNo > div:nth-child(3) > div > div.col696 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')[0].text
        cerceve         = corba.find('div', class_='hbTableContent piyasa')

        json = {"kaynak": kaynak, 'son_guncellenme': son_guncellenme, 'veri' : []}

        for tablo in cerceve.findAll('tr')[1:]:
            cinsi  = tablo.find('td', {'width' : '50%'}).text.replace(' TL',' -- ₺')
            fiyati = tablo.find('td', {'width' : '16%'}).text

            json['veri'].append({
                'cinsi'     : cinsi,
                'fiyati'    : fiyati
            })

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