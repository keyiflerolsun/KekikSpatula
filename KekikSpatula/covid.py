# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from KekikSpatula import KekikSpatula
from typing import List, Dict
from tabulate import tabulate

class Covid(KekikSpatula):
    """
    Covid : Covid verileri döndürür

    Methodlar
    ----------
    .turkiye:
        Türkiye covid verilerini döndürür.

    .dunya_geneli:
        Dünya geneli Covid verilerini ayrıştırarak günlük ölüm sayısına göre sıralar.

    .dunya_tablo():
        Dünya geneli veriyi tabulate halinde döndürür.
    """

    def __repr__(self) -> str:
        return f"{__class__.__name__} Sınıfı -- Covid verileri döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        "Covid verilerini toplayarak ayrıştırır."

        kekik_json = {
            "kaynak": {
                "turkiye" : "corona.cbddo.gov.tr",
                "dunya"   : "interaktif.trthaber.com"
            },
            "veri": {
                "turkiye" : self.turkiye,
                "dunya"   : self.dunya_geneli
            }
        }

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.dunya_tablo = tabulate(self.kekik_json['veri']['dunya'], headers='keys', tablefmt="psql")

    @property
    def dunya_geneli(self) -> List[dict]:
        "Dünya geneli Covid verilerini ayrıştırarak günlük ölüm sayısına göre sıralar."

        kimlik  = {
            "authority"      : "interaktif.trthaber.com",
            "sec-gpc"        : "1",
            "sec-fetch-site" : "same-origin",
            "sec-fetch-mode" : "cors",
            "sec-fetch-dest" : "empty",
            "referer"        : "https://interaktif.trthaber.com/koronavirus/?map=1&counter=1&table=1&news=1&info=1"
        }
        kimlik.update(KekikSpatula.kimlik)

        trt_istek = requests.get("https://interaktif.trthaber.com/koronavirus/data/coronaCountries.json", headers=kimlik, allow_redirects=True)

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

        return sorted(veri, key=lambda sozluk: sozluk['bugunki_olum_sayisi'], reverse=True)

    @property
    def turkiye(self) -> Dict[str, int]:
        "Türkiye Covid verilerini toplayarak ayrıştırır."

        tr_veri = requests.get("https://corona.cbddo.gov.tr/Home/GetTotalData", allow_redirects=True).json()

        return {
            "vaka_sayisi"     : tr_veri["confirmedCount"],
            "olum_sayisi"     : tr_veri["deathCount"],
            "iyilesen_sayisi" : tr_veri["recovryCount"]
        }