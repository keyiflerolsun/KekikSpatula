# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyTrendyol   import Urun

from KekikSpatula import KekikSpatula

class TrendyolUrun(KekikSpatula):
    """
    TrendyolUrun : trendyol.com adresinden ürün detayını hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan ürün detayını döndürmesi için yazılmıştır.."

    def __init__(self, link:str):
        """ürün detayını trendyol'dan dızlar."""

        self.kaynak     = "trendyol.com"

        trend_urun      = Urun()

        kekik_json      = {"kaynak": self.kaynak, "veri" : trend_urun.detay_ver(link)}

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None

    def trendyol_yorum(self, link:str):
        trend_urun = Urun()
        return trend_urun.yorumlar(link)