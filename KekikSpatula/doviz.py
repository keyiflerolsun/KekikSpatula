# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

import pandas as pd
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

class Doviz(object):
    """
    Doviz : altinkaynak.com adresinden döviz verilerini hazır formatlarda elinize verir.

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
        """döviz verilerini altinkaynak.com'dan alarak bs4'ile ayrıştırır."""
        super().__init__()

        kaynak  = "altinkaynak.com"
        istek = requests.get("http://www.altinkaynak.com/Doviz/Kur/Guncel")
        corba = BeautifulSoup(istek.content, 'lxml')
        tablo = corba.find('table', class_='table')

        panda_veri = pd.read_html(str(tablo))[0].rename(
            columns={
                'Unnamed: 0'    : 'Birim',
                'Unnamed: 1'    : 'sil',
                'Unnamed: 5'    : 'sil',
                '₺ ₺'           : 'sil',
            }
        ).drop(columns = 'sil').dropna().reset_index(drop = True)

        for say in range(len(panda_veri['Birim'])):
            panda_veri['Birim'][say] = panda_veri['Birim'][say][-3:]

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