# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup

from KekikSpatula import Statik

import pandas as pd
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

class Doviz(Statik):
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

        .nesne()        -> Object:
            json verisini python nesnesine dönüştürür.
    """
    def __init__(self):
        "döviz verilerini altinkaynak.com'dan alarak pandas ile ayrıştırır."

        kaynak  = "altinkaynak.com"
        istek   = requests.get("http://www.altinkaynak.com/Doviz/Kur/Guncel")
        corba   = BeautifulSoup(istek.content, 'lxml')
        tablo   = corba.find('table', class_='table')

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

        kekik_json = {"kaynak": kaynak, 'veri' : json_veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None