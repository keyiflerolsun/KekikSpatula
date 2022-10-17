# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests     import get
from parsel       import Selector

from KekikSpatula import KekikSpatula

class SonDakika(KekikSpatula):
    """
    SonDakika : `ntv.com.tr` adresinden son dakika verilerini hazır formatlarda elinize verir.

    Nitelikler
    ----------
        >>> .veri -> dict | None:
        json verisi döndürür.

        >>> .anahtarlar -> list | None:
        kullanılan anahtar listesini döndürür.

        >>> .nesne -> KekikNesne:
        json verisini python nesnesine dönüştürür.

    Metodlar
    ----------
        >>> .gorsel() -> str | None:
        oluşan json verisini insanın okuyabileceği formatta döndürür.

        >>> .tablo() -> str | None:
        tabulate verisi döndürür.
    """
    def __repr__(self) -> str:
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den son dakika verilerini döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        """son dakika verilerini `ntv.com.tr`'den alarak bs4'ile ayrıştırır."""

        self.kaynak = "ntv.com.tr"
        istek       = get(f"http://www.{self.kaynak}/son-dakika", headers=self.kimlik)
        secici      = Selector(istek.text)

        kekik_json = {"kaynak": self.kaynak, "veri" : []}

        for _haber in secici.xpath("//ul[@class='gallery-page-video-list-items']/li"):
            haber:Selector = _haber

            kekik_json["veri"].append(
                {
                    "haber"  : haber.xpath(".//h2/a/text()").get().replace("SON DAKİKA HABERİ:", "").replace(" | Son depremler", "").replace("SON DAKİKA: ", "").strip(),
                    "gorsel" : haber.xpath(".//source/@data-srcset").get().split("?")[0],
                    "link"   : "https://www.ntv.com.tr" + haber.xpath(".//h2/a/@href").get()
                }
            )

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None