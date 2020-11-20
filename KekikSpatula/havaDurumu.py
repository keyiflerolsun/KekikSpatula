# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import Statik

class HavaDurumu(Statik):
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

        .nesne()        -> Object:
            json verisini python nesnesine dönüştürür.
    """
    def __init__(self, il:str, ilce:str):
        "hava durumu ve saat verisini google.com'dan alarak bs4'ile ayrıştırır."

        kaynak  = "google.com"
        url     = f"https://www.google.com/search?&q={il}+{ilce}+hava+durumu" + "&lr=lang_tr&hl=tr"
        istek   = requests.get(url)

        corba   = BeautifulSoup(istek.text, "lxml")

        gun_durum   = corba.findAll('div', class_='BNeawe')
        gun, durum  = gun_durum[3].text.strip().split('\n')
        derece      = corba.find('div', class_='BNeawe').text

        kekik_json = {"kaynak": kaynak, 'veri' : [{
            'gun'     : gun,
            'yer'     : il.capitalize() + ' ' + ilce.capitalize(),
            'derece'  : f'{durum} {derece}'
        }]}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None