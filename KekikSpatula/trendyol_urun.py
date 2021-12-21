# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from parsel import Selector
from urllib.parse import unquote
from json import loads

from KekikSpatula import KekikSpatula

class TrendyolUrun(KekikSpatula):
    """
    TrendyolUrun : trendyol.com adresinden ürün detayını hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan ürün detayını döndürmesi için yazılmıştır.."

    def __init__(self, link:str):
        "ürün detayını trendyol'dan dızlar."

        kaynak = "trendyol.com"

        if link.startswith('https://m.'):
            url = link.replace('https://m.', 'https://')
        elif link.startswith('https://ty.gl'):
            try:
                kisa_link_header = requests.get(link, headers=self.kimlik, allow_redirects=False).headers['location']
                url = self.ayristir("adjust_redirect=", "&adjust_t=", unquote(kisa_link_header))
            except KeyError:
                return None
        else:
            url = link

        try:
            istek = requests.get(url, headers=self.kimlik, allow_redirects=True)
        except requests.exceptions.ConnectionError:
            return None

        secici = Selector(istek.text)

        # affiliate = "https://tr.rdrtr.com/aff_c?offer_id=3107&aff_id=24172&url=" + quote(url) + "%26utm_source%3Daff_t%26utm_medium%3Dcps%26utm_campaign%3Dgelirortaklari%26utm_subaff%3D{aff_id}%26adjust_tracker%3D21ouxa_bfy1cc%26adjust_campaign%3Dperformics_tr%26adjust_adgroup%3D1%26adjust_label%3D{transaction_id}"

        try:
            trendyol_veri = {
                "link"       : url.split('?')[0],
                "marka"      : secici.xpath("//h1[@class='pr-new-br']/a/text()").get().strip() if secici.xpath("//h1[@class='pr-new-br']/a/text()").get() else secici.xpath("//h1[@class='pr-new-br']/text()").get().strip(),
                "baslik"     : secici.xpath("//h1[@class='pr-new-br']/span/text()").get().strip(),
                "resim"      : secici.xpath("//div[@class='product-container']//img/@src").get(),
                "indirimsiz" : secici.xpath("//span[@class='prc-org']/text()").get(),
                "indirimli"  : secici.xpath("//span[@class='prc-slg prc-slg-w-dsc']/text()").get(),
                "kampanya"   : secici.xpath("//div[@class='pr-bx-pr-dsc']/text()").get() or secici.xpath("//span[@class='discounted-stamp-text']/text()").get(),
                "son_fiyat"  : secici.xpath("//span[@class='prc-dsc']/text()").get() or secici.xpath("//span[@class='prc-slg']/text()").get(),
                "yorumlar"   : self.trendyol_yorum(url),
                # "link"       : self.link_kisalt.tinyurl.short(url.split('?')[0])
            }
        except AttributeError:
            trendyol_veri = None

        kekik_json = {"kaynak": kaynak, 'veri' : trendyol_veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak

    def trendyol_yorum(self, link:str):
        try:
            urun, _ = link.split("?")
        except ValueError:
            urun = link
        urun    = urun.split('com/')[1]

        url    = "https://public-mdc.trendyol.com/discovery-web-socialgw-service/reviews/" + urun + "/yorumlar"
        kimlik = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        istek  = requests.get(url, headers=kimlik)
        veri   = loads(KekikSpatula.ayristir("STATE__ = ", ";", istek.json()['result']['hydrateScript']))

        yorum_verisi = veri['ratingAndReviewResponse']['ratingAndReview']['productReviews']['content']

        return [
            {
                'tarih'     : yorum['lastModifiedDate'],
                'satici'    : yorum['sellerName'],
                'kullanici' : yorum['userFullName'],
                'yildiz'    : yorum['rate'],
                'yorum'     : yorum['comment']
            }
            for yorum in yorum_verisi
        ]