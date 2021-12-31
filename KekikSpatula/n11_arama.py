# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from parsel import Selector

from KekikSpatula import KekikSpatula

class N11Arama(KekikSpatula):
    """
    N11Arama : n11.com adresinden arama bilgilerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan arama bilgilerini döndürmesi için yazılmıştır.."

    def __init__(self, sorgu:str, sayfa:int = 1):
        "n11 de arama yapar"

        self.kaynak = "n11.com"

        try:
            istek = requests.get(f"https://www.{self.kaynak}/arama?q={sorgu}{f'&pg={sayfa}' if sayfa != 1 else ''}", headers=self.kimlik, allow_redirects=True)
        except requests.exceptions.ConnectionError:
            self.kekik_json = None
            return

        secici  = Selector(istek.text)
        urunler = secici.xpath("//ul[contains(@class, 'clearfix')]/li[contains(@class, 'column')]")

        veri = [
            {
                "baslik"         : urun.xpath("normalize-space(.//h3[contains(@class, 'productName')])").get(),
                "resim"          : urun.xpath(".//img[contains(@class, 'lazy')]/@data-original").get(),
                "urun_linki"     : urun.xpath(".//a[contains(@class, 'plink')]/@href").get(),
                "urun_fiyatlari" : {
                    "eski_fiyati"  : urun.xpath(".//span[contains(@class, 'oldPrice')]/del/text()").get() or None,
                    "yeni_fiyati"  : urun.xpath(".//span[contains(@class, 'newPrice')]/ins/text()").get().strip() + " TL",
                    "sepet_fiyati" : urun.xpath(".//p[@class='view-instant-price']/text()").get(),
                },
                "urun_yıldız"         : ((int(urun.xpath(".//span[contains(@class, 'rating')]/@class").get().replace("rating r", "") if urun.xpath(".//span[contains(@class, 'rating')]/@class").get() else "0") / 100) * 5),
                "magaza_ismi"         : urun.xpath(".//span[contains(@class, 'sallerName')]/text()").extract()[0].strip(),
                "magaza_linki"        : "https://www.n11.com/magaza/" + urun.xpath(".//span[contains(@class, 'sallerName')]/text()").extract()[0].strip().lower().replace(" ", ""),
                "magaza_puan_yuzdesi" : urun.xpath(".//span[contains(@class, 'point')]/text()").get()
            }
              for urun in urunler
        ]

        kekik_json = {"kaynak": self.kaynak, 'veri': veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
