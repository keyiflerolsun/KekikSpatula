# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import KekikSpatula

class SonDakika(KekikSpatula):
    """
    SonDakika : ntv.com.tr adresinden son dakika verilerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den son dakika verilerini döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        "son dakika verilerini ntv.com.tr'den alarak bs4'ile ayrıştırır."

        kaynak  = "ntv.com.tr"
        url     = "https://www.ntv.com.tr/son-dakika"
        kimlik  = self.kimlik
        istek   = requests.get(url, headers=kimlik)

        corba   = BeautifulSoup(istek.content, "lxml")

        kekik_json = {"kaynak": kaynak, 'veri' : []}

        for tablo in corba.findAll("ul", class_="gallery-page-video-list-items"):
            haber_manset = tablo.findAll("div", class_="card card--md")
            for haber in haber_manset:
                kekik_json['veri'].append(
                    {
                        "haber" : haber.p.text.replace('SON DAKİKA HABERİ:', '').replace(' | Son depremler', '').replace('SON DAKİKA: ', '').strip(),
                        "gorsel": haber.img['data-src'].split('?')[0],
                        "link"  : "https://www.ntv.com.tr" + haber.a['href'],
                    }
                )

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak