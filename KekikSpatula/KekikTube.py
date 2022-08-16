# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pytube       import YouTube
from Kekik        import okunabilir_byte, zaman_donustur

from KekikSpatula import KekikSpatula

class KekikTube(KekikSpatula):
    """
    KekikTube : YouTube'den Video Bilgilerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan Video Bilgilerini döndürmesi için yazılmıştır.."

    def __init__(self, yt_url:str):
        """YouTube'den Video Bilgilerini pytube ile Ayıklar."""

        self.kaynak = "Youtube.com"
        yt          = YouTube(yt_url)
        video       = yt.streams.get_highest_resolution()

        veri = {
            "sahip"     : yt.author,
            "baslik"    : yt.title,
            "sure"      : zaman_donustur(yt.length),
            "tarih"     : str(yt.publish_date.strftime("%d-%m-%Y")),
            "izlenme"   : yt.views,
            "resim"     : yt.thumbnail_url,
            "aciklama"  : yt.description,
            "kalite"    : video.resolution if video else None,
            "boyut"     : okunabilir_byte(video.filesize) if video else None,
            "url"       : video.url if video else None
        }

        kekik_json      = {"kaynak": self.kaynak, "veri" : [veri]}

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None