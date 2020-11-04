# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

class HavaDurumu(object):
    """
    HavaDurumu : google.com adresinden hava durumu ve saat verisini hazır formatlarda elinize verir.

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
    def __init__(self, il:str, ilce:str):
        """hava durumu ve saat verisini google.com'dan alarak bs4'ile ayrıştırır."""
        super().__init__()

        kaynak  = "google.com"
        url     = f"https://www.google.com/search?&q={il}+{ilce}+hava+durumu" + "&lr=lang_tr&hl=tr"
        istek   = requests.get(url)

        corba   = BeautifulSoup(istek.text, "lxml")

        gun_durum   = corba.findAll('div', class_='BNeawe')
        gun, durum  = gun_durum[3].text.strip().split('\n')
        derece      = corba.find('div', class_='BNeawe').text

        json = {"kaynak": kaynak, 'veri' : [{
            'gun'     : gun,
            'yer'     : il.capitalize() + ' ' + ilce.capitalize(),
            'derece'  : f'{durum} {derece}'
        }]}

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