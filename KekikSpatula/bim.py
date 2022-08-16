# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests     import get
from bs4          import BeautifulSoup

from KekikSpatula import KekikSpatula

class BimAktuel(KekikSpatula):
    """
    BimAktuel : bim.com.tr adresinden aktüel verilerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den aktüel verilerini döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        """aktüel verilerini bim.com.tr'den alarak bs4'ile ayrıştırır."""

        self.kaynak = "bim.com.tr"
        istek       = get(f"https://www.{self.kaynak}/", headers=self.kimlik, allow_redirects=True)

        corba       = BeautifulSoup(istek.content, "lxml")

        tarih       = corba.find("a", class_="active subButton").text.strip()
        urun_alani  = corba.find("div", class_="productArea")

        urun_rerero = []
        for urun in urun_alani.findAll("div", class_="inner"):
            try:
                urun_basligi    = urun.find("h2", class_="title").text.strip()
                urun_linki      = f"https://{self.kaynak}{urun.a['href']}"
                urun_gorseli    = f"https://{self.kaynak}{urun.img['src'].replace(' ', '%20')}"
                urun_fiyati     = urun.find("a", class_="gButton triangle").text.strip()

                urun_rerero.append({
                    "urun_baslik"   : urun_basligi,
                    "urun_link"     : urun_linki,
                    "urun_gorsel"   : urun_gorseli,
                    "urun_fiyat"    : urun_fiyati
                })
            except (AttributeError, KeyError):
                continue

        kekik_json = {"kaynak": self.kaynak, "tarih": tarih, "veri" : urun_rerero}

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None