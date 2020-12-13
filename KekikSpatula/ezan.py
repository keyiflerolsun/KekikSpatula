# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from datetime import datetime
import pytz

from KekikSpatula import KekikSpatula

class Ezan(KekikSpatula):
    """
    Ezan : sabah.com.tr adresinden Ezan Saatleri verisini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den Ezan Saatleri verisini döndürmesi için yazılmıştır.."

    def __init__(self, il:str):
        "Ezan Saatleri verisini sabah.com.tr'den dızlar."

        il      = il.replace('İ', "i").lower()
        tr2eng  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
        il      = il.lower().translate(tr2eng)

        kaynak  = "sabah.com.tr"
        ezan_api  = f'https://www.sabah.com.tr/json/getpraytimes/{il}'
        json_veri = requests.get(ezan_api).json()['List'][0]

        imsak   = datetime.fromtimestamp(int(json_veri['Imsak'].split('(')[1][:-5]),  pytz.timezone("Turkey")).strftime("%H:%M")
        gunes   = datetime.fromtimestamp(int(json_veri['Gunes'].split('(')[1][:-5]),  pytz.timezone("Turkey")).strftime("%H:%M")
        ogle    = datetime.fromtimestamp(int(json_veri['Ogle'].split('(')[1][:-5]),   pytz.timezone("Turkey")).strftime("%H:%M")
        ikindi  = datetime.fromtimestamp(int(json_veri['Ikindi'].split('(')[1][:-5]), pytz.timezone("Turkey")).strftime("%H:%M")
        aksam   = datetime.fromtimestamp(int(json_veri['Aksam'].split('(')[1][:-5]),  pytz.timezone("Turkey")).strftime("%H:%M")
        yatsi   = datetime.fromtimestamp(int(json_veri['Yatsi'].split('(')[1][:-5]),  pytz.timezone("Turkey")).strftime("%H:%M")

        kekik_json = {"kaynak": kaynak, 'veri' : [{
            'il'        : il.capitalize(),
            'imsak'     : str(imsak),
            'gunes'     : str(gunes),
            'ogle'      : str(ogle),
            'ikindi'    : str(ikindi),
            'aksam'     : str(aksam),
            'yatsi'     : str(yatsi)
        }]}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak