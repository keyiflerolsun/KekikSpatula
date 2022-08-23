# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

class KekikNesne:
    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.__sozluk})"

    def __init__(self, sozluk:dict):
        """Sözlük Tipli Veriyi Python Nesnesine Çevirir"""
        self.__sozluk = sozluk

        assert isinstance(self.__sozluk, dict)
        for key, value in self.__sozluk.items():
            if isinstance(value, (list, tuple)):
                setattr(self, key, [KekikNesne(veri) if isinstance(veri, dict) else veri for veri in value])
            else:
                setattr(self, key, KekikNesne(value) if isinstance(value, dict) else value)

from KekikSpatula._Statik           import KekikSpatula
from KekikSpatula.nobetciEczane     import NobetciEczane
from KekikSpatula.akaryakit         import Akaryakit
from KekikSpatula.doviz             import Doviz
from KekikSpatula.deprem            import SonDepremler
from KekikSpatula.bim               import BimAktuel
from KekikSpatula.haber             import SonDakika
from KekikSpatula.havaDurumu        import HavaDurumu
from KekikSpatula.ezan              import Ezan
from KekikSpatula.discudemy         import DiscUdemy
# from KekikSpatula.google            import Google
from KekikSpatula.KekikTube         import KekikTube
from KekikSpatula.ucak              import UcuzUcak
from KekikSpatula.masal             import CocukMasallari
from KekikSpatula.trendyol_urun     import TrendyolUrun
from KekikSpatula.sahibinden        import Sahibinden
from KekikSpatula.trendyol_kategori import TrendyolKategori
# from KekikSpatula.araskargo         import ArasKargo
from KekikSpatula.covid             import Covid
from KekikSpatula.kripto            import Kripto
# from KekikSpatula.n11_arama         import N11Arama