# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from parsel import Selector
from urllib.parse import unquote
from json import loads

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
            istek = requests.get(f"https://www.{self.kaynak}/arama?q={sorgu}{'&pg=' + str(sayfa) if sayfa != 1 else ''}", headers=self.kimlik, allow_redirects=True)
        except requests.exceptions.ConnectionError:
            return None

        secici = Selector(istek.text)
        urunler = secici.xpath("//ul[contains(@class, 'clearfix')]/li[contains(@class, 'column')]").getall()
        n11_urunler = []
        for urun in urunler:
            urun_secici = Selector(urun)
            n11_urunler.append({
                "baslik": urun_secici.xpath("//h3[contains(@class, 'productName')]/text()").extract()[-1].strip(),
                "resim": urun_secici.xpath("//img[contains(@class, 'lazy')]/@data-original").get(),
                "urun_linki": urun_secici.xpath("//a[contains(@class, 'plink')]/@href").get(),
                "urun_fiyatlari": {
                    "eski_fiyati": urun_secici.xpath("//span[contains(@class, 'oldPrice')]/del/text()").get() or None,
                    "yeni_fiyati": urun_secici.xpath("//span[contains(@class, 'newPrice')]/ins/text()").get().strip() + " TL",
                    "sepet_fiyati": urun_secici.xpath("//p[@class='view-instant-price']/text()").get(),
                },
                "urun_yıldız": ((int(urun_secici.xpath("//span[contains(@class, 'rating')]/@class").get().replace("rating r", "") if urun_secici.xpath("//span[contains(@class, 'rating')]/@class").get() else "0") / 100) * 5),
                "magaza_ismi": urun_secici.xpath("//span[contains(@class, 'sallerName')]/text()").extract()[0].strip(),
                "magaza_linki": "https://www.n11.com/magaza/" + urun_secici.xpath("//span[contains(@class, 'sallerName')]/text()").extract()[0].strip().lower().replace(" ", ""),
                "magaza_puan_yuzdesi": urun_secici.xpath("//span[contains(@class, 'point')]/text()").get()
            })

        kekik_json = {"kaynak": self.kaynak, 'veri' : n11_urunler}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None