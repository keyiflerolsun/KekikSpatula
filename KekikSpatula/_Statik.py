# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyshorteners import Shortener
from re           import search, match
from json         import dumps
from tabulate     import tabulate
from ._Kimlikler  import kimlik_ver
from Kekik        import Nesne

class KekikSpatula(object):
    link_mi     = lambda link: bool(match(r"http(?:s?):\/\/(?:www\.)?", link))
    ayristir    = lambda berisi, gerisi, yazi : search(f'{berisi}(.*){gerisi}', yazi).group(1)
    kimlik      = {'User-Agent': kimlik_ver()}
    link_kisalt = Shortener()

    def __init__(self, kekik_json) -> None:
        super().__init__()
        self.kekik_json = kekik_json

    @property
    def veri(self) -> dict | None:
        """json verisi döndürür."""
        return self.kekik_json or None

    @property
    def nesne(self) -> Nesne:
        """json verisini python nesnesine dönüştürür"""
        return Nesne(self.kekik_json["veri"][0]) if len(self.kekik_json["veri"]) == 1 else list(Nesne(self.kekik_json).veri)

    def gorsel(self, girinti:int=2, alfabetik:bool=False) -> str | None:
        """oluşan json verisini insanın okuyabileceği formatta döndürür."""
        return dumps(self.kekik_json, indent=girinti, sort_keys=alfabetik, ensure_ascii=False) if self.kekik_json else None

    def tablo(self, tablo_turu:str='psql') -> str | None:
        """tabulate verisi döndürür."""
        try:
            return tabulate(self.kekik_json["veri"], headers='keys', tablefmt=tablo_turu) if self.kekik_json else None
        except TypeError:
            return None

    @property
    def anahtarlar(self) -> list | None:
        """kullanılan anahtar listesini döndürür."""
        try:
            return list(self.kekik_json["veri"][0].keys()) if self.kekik_json else None
        except (TypeError, KeyError):
            return None