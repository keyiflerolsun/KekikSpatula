# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests import get
from json import loads

from KekikSpatula import KekikSpatula

class ArasKargo(KekikSpatula):
    """
    ArasKargo : araskargo.com.tr adresinden kargo verilerini döndürür.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan kargo verilerini döndürmesi için yazılmıştır.."

    def __init__(self, takip_numarasi:int) -> None:
        "kargo verilerini araskargo.com.tr'den alarak ayrıştırır."

        kaynak  = "araskargo.com.tr"
        takip   = loads(get(f"https://social.araskargo.com.tr/Facebook/KargoTakipDetay?trackingNumber={takip_numarasi}").json())
        detay   = loads(get(f"https://social.araskargo.com.tr/Facebook/KargoTakip?trackingNumber={takip_numarasi}").json())

        takip_veri = detay["cargoDetails"]["cargoDetail"][0]

        json_veri = {
            "takip_no"  : takip_numarasi,
            "durum"     : {
                "son_durum"    : takip_veri["cargoStatus"],
                "teslim_zaman" : takip_veri["unitArriveDate"],
                "teslim_alan"  : takip_veri["deliveredCustomerName"]
            },
            "fatura"    : {
                "gonderici"   : takip_veri["senderAccountName"],
                "cikis_sube"  : takip_veri["initialUnit"],
                "varis_sube"  : takip_veri["arrivalUnit"],
                "cikis_zaman" : takip_veri["unitLeaveDate"]
            },
            "hareketler" : [
                {
                   "islem_zaman"    : asama["transactionDate"],
                   "islem_birim"    : asama["destinationUnit"],
                   "islem_aciklama" : asama["transactionDescription"]
                }
                  for asama in takip["cargoMoveDetails"]["cargoMoveDetail"]
            ],
        }

        kekik_json = {"kaynak": kaynak, 'veri' : json_veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak