# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from parsel import Selector

from KekikSpatula import KekikSpatula

class CocukMasallari(KekikSpatula):
    """
    CocukMasallari : masaloku.net adresinden çocuk masallarını hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan çocuk masallarını döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        "çocuk masallarını masaloku.net'dan alarak parsel'ile ayrıştırır."

        kaynak  = "masaloku.net"
        url     = "https://masaloku.net"
        kimlik  = self.kimlik
        istek   = requests.get(url, headers=kimlik, allow_redirects=True)

        secici  = Selector(istek.text)

        kekik_json = {"kaynak": kaynak, 'veri' : []}
        for masal in secici.xpath("//div[@id='content_box']/article"):
            adi   = masal.xpath(".//h2/a/text()").get()
            linki = masal.xpath(".//h2/a/@href").get()

            kekik_json['veri'].append(
                {
                    'ad'     : adi,
                    'link'   : linki,
                    'icerik' : '\n'.join(Selector(requests.get(linki, headers=kimlik, allow_redirects=True).text).xpath("//div[@class='thecontent']/p/text()").getall()[1:])
                }
            )

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak