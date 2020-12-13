# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import KekikSpatula

class TrendyolYorum(KekikSpatula):
    """
    Ezan : trendyol.com adresinden ürün yorumlarını hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan ürün yorumlarını döndürmesi için yazılmıştır.."

    def __init__(self, link:str):
        "ürün yorumlarını trendyol'den dızlar."

        try:
            urun, butik = link.split("?")
        except ValueError:
            urun = link

        kaynak  = "trendyol.com"
        url     = urun + "/yorumlar"
        kimlik  = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        istek   = requests.get(url, headers=kimlik)
        corba   = BeautifulSoup(istek.text, "html5lib")

        urun_ismi = corba.find('span', class_='product-name').text
        yorumlar  = corba.find('div', class_='pr-rnr-com')

        try:
            yorum_sahibi     = [yorum_sahibi.text.split(' | ')[0] for yorum_sahibi in yorumlar.findAll('span', class_='rnr-com-usr')]
            kullanici_yorumu = [yorum_.text for yorum_ in yorumlar.findAll('div', class_='rnr-com-tx')]

            yildiz_sayisi    = []
            for i_yildiz in yorumlar.findAll("div", attrs={'class':'ratings readonly'}):
                yildiz = [tek_yildiz for tek_yildiz in i_yildiz.findAll("div", attrs={'class': 'full', 'style': 'width:100%;max-width:100%'})]
                yildiz_sayisi.append(len(yildiz))

            trendyol_veri = [
                {
                    'kullanici' : yorum_sahibi[adet],
                    'yildiz'    : yildiz_sayisi[adet],
                    'yorum'     : kullanici_yorumu[adet]
                }
                for adet in range(len(yorum_sahibi))
            ]
        except AttributeError:
            trendyol_veri = [{'Yorum' : None}]

        kekik_json = {"kaynak": kaynak, 'urun_linki' : urun, 'urun_adi': urun_ismi, 'veri' : trendyol_veri}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak