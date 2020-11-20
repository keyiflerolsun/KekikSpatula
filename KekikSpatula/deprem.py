# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
import pandas as pd

from KekikSpatula import Statik

class SonDepremler(Statik):
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

        .nesne()        -> Object:
            json verisini python nesnesine dönüştürür.
    """
    def __init__(self):
        "son deprem verilerini afet.gen.tr'den alarak pandas ile ayrıştırır."

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

        kekik_json = {"kaynak": kaynak, 'veri' : json_veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None