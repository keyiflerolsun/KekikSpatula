# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests     import get
from parsel       import Selector

from KekikSpatula import KekikSpatula

class CocukMasallari(KekikSpatula):
    """
    CocukMasallari : `masaloku.net` adresinden çocuk masallarını hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan çocuk masallarını döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        """çocuk masallarını `masaloku.net`'dan alarak parsel'ile ayrıştırır."""

        self.kaynak = "masaloku.net"
        istek       = get(f"https://{self.kaynak}", headers=self.kimlik, allow_redirects=True)

        secici      = Selector(istek.text)

        kekik_json  = {"kaynak": self.kaynak, "veri" : []}

        for masal in secici.xpath("//ul[@id='posts-container']/li[contains(@class, 'post-item')]"):
            adi   = masal.xpath(".//h2/a/text()").get()
            linki = masal.xpath(".//h2/a/@href").get()

            kekik_json["veri"].append(
                {
                    "ad"     : adi,
                    "link"   : linki,
                    "icerik" : "\n".join(Selector(get(linki, headers=self.kimlik, allow_redirects=True).text).xpath("//div[contains(@class, 'entry-content')]/p/text()").getall()[1:])
                }
            )

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None