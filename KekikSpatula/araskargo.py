# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests import get
from json import loads
from parsel import Selector
import pandas as pd

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

    def __init__(self, gelen_no) -> None:
        "kargo verilerini araskargo.com.tr'den alarak ayrıştırır."

        takip_numarasi = str(gelen_no).replace(' ', '').strip()
        kaynak   = "araskargo.com.tr"
        takip    = loads(get(f"https://social.araskargo.com.tr/Facebook/KargoTakip?trackingNumber={takip_numarasi}").json())
        # detay    = loads(get(f"https://social.araskargo.com.tr/Facebook/KargoTakipDetay?trackingNumber={takip_numarasi}").json())

        if takip_numarasi[0].isdigit():
            takip_veri = takip["cargoDetails"]["cargoDetail"][0]
            fatura_no  = takip_veri["waybillId"]
            fatura = Selector(get(f"https://kargotakip.araskargo.com.tr/yurticigonbil.aspx?Cargo_Code={fatura_no}").text)
        else:
            seri      = takip_numarasi[:2]
            fat_no    = takip_numarasi[2:]
            fatura_no = f"{seri} {fat_no}"
            fatura = Selector(get(f"https://kargotakip.araskargo.com.tr/yurticigonbil.aspx?seri={seri}&fat_no={fat_no}&ref_no=&Cargo_Code=").text)

        json_veri = {
            "takip_no"  : takip_numarasi if takip_numarasi[0].isdigit() else None,
            "fatura_no" : fatura_no if len(fatura_no) > 15 else None,
            "seri_no"   : fatura.xpath("//span[@id='gfatno']/text()").get(),
            "durum"     : {
                "kargonun_cinsi" : fatura.xpath("//span[@id='Kargonun_Cinsi']/text()").get(),
                "son_durum"      : fatura.xpath("//span[@id='Son_Durum']/text()").get(),
                "teslim_tarihi"  : fatura.xpath("//span[@id='Teslim_Tarihi']/text()").get(),
                "teslim_saati"   : fatura.xpath("//span[@id='Teslim_Saati']/text()").get(),
                "teslim_alan"    : fatura.xpath("//span[@id='Teslim_Alan']/text()").get()
            },
            "fatura"    : {
                "ilk_cikis"     : fatura.xpath("normalize-space(//span[@id='LabelIlkCikis'])").get(),
                "cikis_subesi"  : fatura.xpath("normalize-space(//span[@id='cikis_subesi'])").get(),
                "varis_subesi"  : fatura.xpath("normalize-space(//span[@id='varis_subesi'])").get(),
                "gonderi_tipi"  : fatura.xpath("normalize-space(//span[@id='LabelGonTipi'])").get(),
                "fatura_turu"   : fatura.xpath("normalize-space(//span[@id='fatura_turu'])").get(),
                "cikis_tarihi"  : fatura.xpath("normalize-space(//span[@id='cikis_tarihi'])").get(),
                "gonderici"     : fatura.xpath("normalize-space(//span[@id='gonderici_adi_soyadi'])").get(),
                "alici"         : fatura.xpath("normalize-space(//span[@id='alici_adi_soyadi'])").get()
            },
            "hareketler" : loads(pd.read_html(str(fatura.xpath("//table[@id='DataGrid1']").get()))[0].rename(
                columns={
                    0 : 'zaman',
                    1 : 'birim',
                    2 : 'islem',
                }
            ).reset_index(drop = True).to_json(orient='records'))[1:]
        }

        kekik_json = {"kaynak": kaynak, 'veri' : json_veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak