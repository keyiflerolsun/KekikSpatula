# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import KekikSpatula

class HavaDurumu(KekikSpatula):
    """
    HavaDurumu : google.com adresinden hava durumu ve saat verisini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan hava durumu ve saat verisini döndürmesi için yazılmıştır.."

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
        self.kaynak      = kaynak