# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup

from KekikSpatula import KekikSpatula

import pandas as pd
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

class Doviz(KekikSpatula):
    """
    Doviz : altinkaynak.com adresinden döviz verilerini hazır formatlarda elinize verir.

    Methodlar
    ----------
        .veri:
            json verisi döndürür.

        .gorsel():
            oluşan json verisini insanın okuyabileceği formatta döndürür.

        .tablo():
            tabulate verisi döndürür.

        .anahtarlar:
            kullanılan anahtar listesini döndürür.

        .nesne:
            json verisini python nesnesine dönüştürür.
    """
    def __repr__(self) -> str:
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan döviz verilerini döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        "döviz verilerini altinkaynak.com'dan alarak pandas ile ayrıştırır."

        kaynak  = "altinkaynak.com"
        istek   = requests.get("http://www.altinkaynak.com/Doviz/Kur/Guncel")
        corba   = BeautifulSoup(istek.content, 'lxml')
        tablo   = corba.find('table', class_='table')

        panda_veri = pd.read_html(str(tablo))[0].rename(
            columns={
                'Unnamed: 0'    : 'birim',
                'Alış'          : 'alis',
                'Satış'         : 'satis',
                'Unnamed: 1'    : 'sil',
                'Unnamed: 5'    : 'sil',
                '₺ ₺'           : 'sil',
            }
        ).drop(columns = 'sil').dropna().reset_index(drop = True)

        for say in range(len(panda_veri['birim'])):
            panda_veri['birim'][say] = panda_veri['birim'][say][-3:]

        json_veri = json.loads(panda_veri.to_json(orient='records'))

        kekik_json = {"kaynak": kaynak, 'veri' : json_veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak