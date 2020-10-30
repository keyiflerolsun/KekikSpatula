# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from datetime import datetime
from tabulate import tabulate

class Ezan(object):
    """
    Ezan : sabah.com.tr adresinden Ezan Saatleri verisini hazır formatlarda elinize verir.

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
    def __init__(self, il:str):
        """Ezan Saatleri verisini sabah.com.tr'den dızlar."""
        super().__init__()

        il      = il.replace('İ', "i").lower()
        tr2eng  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
        il      = il.lower().translate(tr2eng)

        kaynak  = "sabah.com.tr"
        ezan_api  = f'https://www.sabah.com.tr/json/getpraytimes/{il}'
        json_veri = requests.get(ezan_api).json()['List'][0]

        imsak   = datetime.fromtimestamp(int(json_veri['Imsak'].split('(')[1][:-5]))
        gunes   = datetime.fromtimestamp(int(json_veri['Gunes'].split('(')[1][:-5]))
        ogle    = datetime.fromtimestamp(int(json_veri['Ogle'].split('(')[1][:-5]))
        ikindi  = datetime.fromtimestamp(int(json_veri['Ikindi'].split('(')[1][:-5]))
        aksam   = datetime.fromtimestamp(int(json_veri['Aksam'].split('(')[1][:-5]))
        yatsi   = datetime.fromtimestamp(int(json_veri['Yatsi'].split('(')[1][:-5]))

        json = {"kaynak": kaynak, 'veri' : [{
            'il'        : il.capitalize(),
            'imsak'     : str(imsak).split()[1][:-3],
            'gunes'     : str(gunes).split()[1][:-3],
            'ogle'      : str(ogle).split()[1][:-3],
            'ikindi'    : str(ikindi).split()[1][:-3],
            'aksam'     : str(aksam).split()[1][:-3],
            'yatsi'     : str(yatsi).split()[1][:-3]
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