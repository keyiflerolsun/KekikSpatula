# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests     import get
from json         import loads
from bs4          import BeautifulSoup
import pandas     as pd

from KekikSpatula import KekikSpatula

class SonDepremler(KekikSpatula):
    """
    SonDepremler : afet.gen.tr adresinden son deprem verilerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den son deprem verilerini döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        """son deprem verilerini afet.gen.tr'den alarak pandas ile ayrıştırır."""

        self.kaynak = "afet.gen.tr"
        istek       = get(f"http://www.{self.kaynak}/son-depremler.php", headers=self.kimlik)
        corba       = BeautifulSoup(istek.content, "lxml")
        tablo       = corba.find("table", width="100%")

        panda_veri = pd.read_html(str(tablo))[0].rename(
            columns = {
                0   : "tarih",
                1   : "saat",
                2   : "enlem",
                3   : "boylam",
                4   : "derinlik",
                5   : "md",
                6   : "ml",
                7   : "ms",
                8   : "yer"
            }
        ).drop([0], axis=0).reset_index(drop=True)

        json_veri  = loads(panda_veri.to_json(orient="records"))

        kekik_json = {"kaynak": self.kaynak, "veri" : json_veri}

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None