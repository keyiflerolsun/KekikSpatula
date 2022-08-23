# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyTrendyol   import Kategori

from KekikSpatula import KekikSpatula

class TrendyolKategori(KekikSpatula):
    """
    TrendyolKategori : trendyol.com adresinden kategori ürünlerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan kategori ürünlerini döndürmesi için yazılmıştır.."

    def __init__(self, kategori_adi:str, sayfa_sayisi:int=1) -> None:
        """kategori ürünlerini trendyol'dan dızlar."""

        self.kaynak     = "trendyol.com"

        trend_kategori  = Kategori()

        kekik_json      = {"kaynak": self.kaynak, "veri": trend_kategori.urunleri_ver(kategori_adi, sayfa_sayisi)}

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None