# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd

class SonDepremler(object):
    """
    SonDepremler : afet.gen.tr adresinden son deprem verilerini hazır formatlarda elinize verir.

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
        """son deprem verilerini afet.gen.tr'den alarak pandas ile ayrıştırır."""
        super().__init__()

        kaynak  = "afet.gen.tr'"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        istek   = requests.get("http://www.afet.gen.tr/son-depremler.php", headers=kimlik)
        corba   = BeautifulSoup(istek.content, 'lxml')
        tablo   = corba.find('table', width="100%")

        panda_veri = pd.read_html(str(tablo))[0].rename(
            columns={
                0   : 'Tarih',
                1   : 'Saat',
                2   : 'Enlem(N)',
                3   : 'Boylam(E)',
                4   : 'Derinlik(km)',
                5   : 'MD',
                6   : 'ML',
                7   : 'MS',
                8   : 'Yer'
            }
        ).drop([0], axis=0).reset_index(drop = True)

        json_veri = json.loads(panda_veri.to_json(orient='records'))

        json_ = {"kaynak": kaynak, 'veri' : json_veri}

        self.json  = json_ if json_['veri'] != [] else None

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