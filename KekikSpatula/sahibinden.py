# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests     import get
from parsel       import Selector

from KekikSpatula import KekikSpatula

class Sahibinden(KekikSpatula):
    """
    Ezan : sahibinden.com adresinden ilanı hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan ilanı döndürmesi için yazılmıştır.."

    def __init__(self, sahibinden_url:str):
        """ilanı sahibinden'den dızlar."""

        self.kaynak  = "sahibinden.com"
        kimlik  = self.kimlik.copy()
        kimlik.update({"Referer": f"https://www.{self.kaynak}/?JLBreadCrumbEnable=false"})
        istek   = get(sahibinden_url, headers=kimlik, allow_redirects=True)

        secici  = Selector(istek.text)

        ilan           = secici.xpath("//div[@class='classifiedDetailTitle']")
        detay_baslik   = secici.xpath("//ul[@class='classifiedInfoList']/li/strong/text()").getall()
        detay_aciklama = secici.xpath("//ul[@class='classifiedInfoList']/li/span/text()").getall()

        try:
            kekik_json     = {
                "kaynak" : self.kaynak,
                "veri"   : {
                    "link"   : sahibinden_url,
                    "baslik" : ilan.xpath("//h1/text()").get().strip(),
                    "resim"  : ilan.xpath("//img[@class='stdImg']/@src").get(),
                    "fiyat"  : ilan.xpath("//div[@class='classifiedInfo ']/h3/text()").get().strip(),
                    "yer"    : "".join(ilan.xpath("//div[@class='classifiedInfo ']/h2/a/text()").getall()).replace(" ", "").lstrip("\n").replace("\n", " | ").replace("Mh.", ""),
                    "detay"  : [
                        f'{detay_baslik[bak].strip()} : {detay_aciklama[bak].strip()}'
                          for bak in range(len(detay_baslik))
                    ]
                }
            }
        except AttributeError:
            kekik_json     = {
                "kaynak" : self.kaynak,
                "veri"   : {
                    "link" : sahibinden_url,
                    "hata" : "İlan Yayında Değil.."
                }
            }

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None