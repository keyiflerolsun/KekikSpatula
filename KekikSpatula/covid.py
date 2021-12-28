# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests import get
from KekikSpatula import KekikSpatula
from typing import Dict
class Covid(KekikSpatula):
    """
    Covid : interaktif.trthaber.com adresinden covid verilerini hazır formatlarda elinize verir.

    Methodlar
    ----------
        .veri:
            json verisi döndürür.

        .ulke(str):
            istediğiniz ülkenin covid verisini döndürür

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan covid verilerini döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        "interaktif.trthaber.com adresinden covid verilerini hazır formatlarda elinize verir."

        self.kaynak = "interaktif.trthaber.com"
        kimlik  = {
            "authority"      : self.kaynak,
            "sec-gpc"        : "1",
            "sec-fetch-site" : "same-origin",
            "sec-fetch-mode" : "cors",
            "sec-fetch-dest" : "empty",
            "referer"        : f"https://{self.kaynak}/koronavirus/?map=1&counter=1&table=1&news=1&info=1"
        }
        kimlik.update(KekikSpatula.kimlik)

        trt_istek = get(f"https://{self.kaynak}/koronavirus/data/coronaCountries.json", headers=kimlik, allow_redirects=True)

        veri = [
            {
                "ulke"                    : ulke["country"],
                "ulke_bayragi"            : ulke["countryInfo"]["flag"],
                "ulke_nufusu"             : ulke["population"],
                "aktif_hasta"             : ulke["active"],
                "vaka_sayisi"             : ulke["cases"],
                "bugunki_vaka_sayisi"     : ulke["todayCases"],
                "olum_sayisi"             : ulke["deaths"],
                "bugunki_olum_sayisi"     : ulke["todayDeaths"],
                "iyilesen_sayisi"         : ulke["recovered"],
                "bugunki_iyilesen_sayisi" : ulke["todayRecovered"],
                "ulke_harita_konum"       : f'{ulke["countryInfo"]["lat"]},{ulke["countryInfo"]["long"]}',
            }
              for ulke in trt_istek.json()
        ]

        self.dunya_geneli = sorted(veri, key=lambda sozluk: sozluk['bugunki_olum_sayisi'], reverse=True)

        kekik_json = {
            "kaynak" : self.kaynak,
            "veri"   : sorted(veri, key=lambda sozluk: sozluk['bugunki_olum_sayisi'], reverse=True)
        }

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None

    def ulke(self, ulke:str) -> Dict[str, int]:
        "İstediğiniz Ülkenin Covid Verisini Döndürür"

        for veri in self.dunya_geneli:
            if ulke.lower() in [veri['ulke'].lower(), veri['ulke_bayragi'].split('/')[-1].rstrip('.png')]:
                # del veri['ulke']
                return veri