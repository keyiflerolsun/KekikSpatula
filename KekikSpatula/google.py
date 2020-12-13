# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import KekikSpatula

class Google(KekikSpatula):
    """
    Google : Google araması yaparak; başlık, link ve açıklama'yı parse eder..

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'den başlık, link ve açıklama verisini döndürmesi için yazılmıştır.."

    def __init__(self, aranacak_sey:str):
        "Google araması yaparak; başlık, link ve açıklama'yı parse eder.."

        kaynak  = "google.com"
        url     = f"https://www.{kaynak}/search?&q={aranacak_sey}" + "&lr=lang_tr&hl=tr"
        istek   = requests.get(url)

        corba   = BeautifulSoup(istek.text, "lxml")

        sonuclar = corba.findAll('div', class_='ZINbbc')

        json_fetist = []
        for sonuc in sonuclar:
            baslik   = sonuc.find('div', class_='BNeawe').text if sonuc.find('div', class_='BNeawe') else None
            link     = sonuc.find('a')['href'].lstrip('/url?q=').split('&sa')[0].split('?fit%')[0] if sonuc.find('a') else None
            aciklama = [aciklamalar.find('div', class_='AP7Wnd').text for aciklamalar in sonuc.findAll('div', class_='kCrYT')]
            aciklama = '\n'.join(aciklama[1:])

            if baslik and aciklama:
                json_fetist.append({
                    'baslik'    : baslik,
                    'link'      : link.lstrip('imgres?imgurl=') if link.startswith('imgres?imgurl=') else link,
                    'aciklama'  : aciklama
                })

        kekik_json = {"kaynak": kaynak, 'veri' : json_fetist}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak