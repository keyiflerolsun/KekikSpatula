# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests     import get
from bs4          import BeautifulSoup

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

        corba      = BeautifulSoup(istek.content, "lxml")

        kekik_json = {"kaynak": self.kaynak, "veri" : []}

        for tablo in corba.findAll("ul", class_="gallery-page-video-list-items"):
            haber_manset = tablo.findAll("div", class_="card card--md")
            for haber in haber_manset:
                kekik_json["veri"].append(
                    {
                        "haber"  : haber.p.text.replace("SON DAKİKA HABERİ:", "").replace(" | Son depremler", "").replace("SON DAKİKA: ", "").strip(),
                        "gorsel" : haber.img["data-src"].split("?")[0],
                        "link"   : f"https://www.ntv.com.tr{haber.a['href']}"
                    }
                )

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None