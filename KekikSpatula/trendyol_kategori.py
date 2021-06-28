# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from cloudscraper import CloudScraper
from parsel import Selector

from KekikSpatula import KekikSpatula

class TrendyolKategori(KekikSpatula):
    """
    TrendyolKategori : trendyol.com adresinden kategori ürünlerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan kategori ürünlerini döndürmesi için yazılmıştır.."

    def __init__(self, link:str) -> None:
        "kategori ürünlerini trendyol'dan dızlar."

        self.kaynak  = "trendyol.com"
        scraper = CloudScraper()
        istek   = scraper.get(link, headers=self.kimlik)
        secici  = Selector(istek.text)

        urunler = secici.xpath("//div[@class='prdct-cntnr-wrppr']//div[@class='p-card-chldrn-cntnr']")

        kekik_json = {"kaynak": self.kaynak, 'veri' : []}
        for urun in urunler:
            yildiz_sayisi = []
            for i_yildiz in urun.xpath(".//div[@class='ratings']/div"):
                yildiz = [tek_yildiz for tek_yildiz in i_yildiz.xpath(".//div[@class='full' and @style='width:100%;max-width:100%']")]
                yildiz_sayisi.append(len(yildiz))

            urun_bilgileri = {
                "link"       : "https://www.trendyol.com" + urun.xpath(".//a/@href").get(),
                "marka"      : urun.xpath(".//span[@class='prdct-desc-cntnr-ttl']/text()").get(),
                "yildiz"     : sum(yildiz_sayisi),
                "baslik"     : urun.xpath(".//span[@class='prdct-desc-cntnr-name hasRatings']/text()").get() or urun.xpath(".//span[@class='prdct-desc-cntnr-name']/text()").get(),
                "indirim"    : urun.xpath("normalize-space(.//div[@class='pr-bx-pr-dsc-pr'])").get() or None,
                "indirimsiz" : urun.xpath("normalize-space(.//div[@class='prc-box-sllng prc-box-sllng-w-dscntd'])").get() or None,
                "fiyat"      : urun.xpath("normalize-space(.//div[@class='product-price'])").get() or urun.xpath("normalize-space(.//div[@class='prc-box-dscntd'])").get()
            }
            kekik_json["veri"].append(urun_bilgileri)

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None