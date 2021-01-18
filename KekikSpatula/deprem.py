# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
import pandas as pd

from KekikSpatula import KekikSpatula

class SonDepremler(KekikSpatula):
    """
    SonDepremler : afet.gen.tr adresinden son deprem verilerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den son deprem verilerini döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        "son deprem verilerini afet.gen.tr'den alarak pandas ile ayrıştırır."

        kaynak  = "afet.gen.tr"
        kimlik  = self.kimlik
        istek   = requests.get("http://www.afet.gen.tr/son-depremler.php", headers=kimlik)
        corba   = BeautifulSoup(istek.content, 'lxml')
        tablo   = corba.find('table', width="100%")

        panda_veri = pd.read_html(str(tablo))[0].rename(
            columns={
                0   : 'tarih',
                1   : 'saat',
                2   : 'enlem',
                3   : 'boylam',
                4   : 'derinlik',
                5   : 'md',
                6   : 'ml',
                7   : 'ms',
                8   : 'yer'
            }
        ).drop([0], axis=0).reset_index(drop = True)

        json_veri = json.loads(panda_veri.to_json(orient='records'))

        kekik_json = {"kaynak": kaynak, 'veri' : json_veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak