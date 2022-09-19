# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikSpatula.Lib import KekikGoogle
from asyncio          import new_event_loop

async def gg_ver(dil, aranacak_sey):
    gg = KekikGoogle(dil=dil)
    return await gg.ara(aranacak_sey)

from KekikSpatula import KekikSpatula

class Google(KekikSpatula):
    """
    Google : Google araması yaparak; başlık, link ve açıklama'yı parse eder..

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den başlık, link ve açıklama verisini döndürmesi için yazılmıştır.."

    def __init__(self, aranacak_sey:str, dil:str="tr"):
        """Google araması yaparak; başlık, link ve açıklama'yı parse eder.."""

        self.kaynak = "google.com"

        veri = new_event_loop().run_until_complete(gg_ver(dil, aranacak_sey))

        kekik_json = {"kaynak": self.kaynak, "veri": veri["sonuclar"], "cevap": veri["cevap"], "oneriler": veri["oneriler"]}

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None