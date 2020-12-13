# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests

from KekikSpatula import KekikSpatula

class Covid(KekikSpatula):
    """
    Covid : saglik.gov.tr adresinden covid verilerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan covid verileri döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        "covid verilerini saglik.gov.tr'den alır."

        kaynak  = "saglik.gov.tr"
        url     = "https://covid19.saglik.gov.tr/covid19api?getir=sondurum"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        istek   = requests.get(url, headers=kimlik).json()

        kekik_json = {"kaynak": kaynak, 'veri' : istek}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak