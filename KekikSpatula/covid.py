# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fake_useragent.fake import UserAgent
import requests
from KekikSpatula import KekikSpatula

class Covid(KekikSpatula):
    """
    Covid : interaktif.trthaber.com adresinden covid verilerini hazır formatlarda elinize verir.

    Methodlar
    ----------
    .veri:
        json verisi döndürür.

    .dunya_geneli:
        dunya geneli covid verilerisi döndürür.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan covid verileri döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        "covid verilerini interaktif.trthaber.com'den alarak ayrıştırır."

        kaynak  = "interaktif.trthaber.com"
        kimlik  = {
            "authority": "interaktif.trthaber.com",
            "user-agent": UserAgent().random,
            "sec-gpc": "1",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://interaktif.trthaber.com/koronavirus/?map=1&counter=1&table=1&news=1&info=1",
        }
        istek   = requests.get("https://interaktif.trthaber.com/koronavirus/data/coronaCountries.json", headers=kimlik, allow_redirects=True)
        
        covid_duzenli_data = []
        for covid in istek.json():
            try:
                ulke                    = covid["country"]
                ulke_bayragi            = covid["countryInfo"]["flag"]
                ulke_nufusu             = covid["population"]
                aktif_hasta             = covid["active"]
                vaka_sayisi             = covid["cases"]
                bugunki_vaka_sayisi     = covid["todayCases"]
                olum_sayisi             = covid["deaths"]
                bugunki_olum_sayisi     = covid["todayDeaths"]
                iyilesen_sayisi         = covid["recovered"]
                bugunki_iyilesen_sayisi = covid["todayRecovered"]
                ulke_harita_konum       = str(covid["countryInfo"]["lat"]) + "," + str(covid["countryInfo"]["long"])

                covid_duzenli_data.append({
                    "ulke"                    : ulke,
                    "ulke_bayragi"            : ulke_bayragi,
                    "ulke_nufusu"             : ulke_nufusu,
                    "aktif_hasta"             : aktif_hasta,
                    "vaka_sayisi"             : vaka_sayisi,
                    "bugunki_vaka_sayisi"     : bugunki_vaka_sayisi,
                    "olum_sayisi"             : olum_sayisi,
                    "bugunki_olum_sayisi"     : bugunki_olum_sayisi,
                    "iyilesen_sayisi"         : iyilesen_sayisi,
                    "bugunki_iyilesen_sayisi" : bugunki_iyilesen_sayisi,
                    "ulke_harita_konum"       : ulke_harita_konum,
                })
            except (AttributeError, KeyError):
                continue

        kekik_json = {"kaynak": kaynak, 'veri' : covid_duzenli_data}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak
        
        "dunya geneli covid verilerini corona.cbddo.gov.tr'den alarak ayrıştırır."

        kaynak  = "corona.cbddo.gov.tr"
        kimlik  = self.kimlik
        istek   = requests.get("https://corona.cbddo.gov.tr/Home/GetTotalData", headers=kimlik, allow_redirects=True)

        covid_verisi = istek.json()
        
        self.dunya_geneli = {"kaynak": kaynak, 'veri' : {"vaka_sayisi": covid_verisi["confirmedCount"], "olum_sayisi": covid_verisi["deathCount"], "iyilesen_sayisi": covid_verisi["recovryCount"]}}
