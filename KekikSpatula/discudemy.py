# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import KekikSpatula

class DiscUdemy(KekikSpatula):
    """
    DiscUdemy : discudemy.com adresinden Udemy Kurslarını hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan Udemy Kurslarını döndürmesi için yazılmıştır.."

    def __init__(self, kategori:str):
        "Kategoriye göre Udemy Kurslarını discudemy.com'dan alarak bs4'ile ayrıştırır."

        kaynak  = "discudemy.com"
        url     = f"https://www.discudemy.com/s-r/{kategori}.jsf"
        kimlik  = self.kimlik
        istek   = requests.get(url, headers=kimlik, allow_redirects=True)

        corba   = BeautifulSoup(istek.content, "lxml")

        udemy   = []
        for tek in corba.findAll('section', class_="card"):
            dil = tek.find('label', class_='ui green disc-fee label')

            if dil.text.lower() == 'ads':
                continue

            baslik = tek.find('div', class_='header')

            disc_link   = requests.get('https://www.discudemy.com/go/' + baslik.a['href'].split('/')[-1])
            disc_corba  = BeautifulSoup(disc_link.content, 'lxml')
            baglanti    = disc_corba.select('body > div.ui.container.mt10 > div:nth-child(3) > div > a')[0]['href']

            udemy.append({
                'dil': dil.text,
                'baslik': baslik.text.strip(),
                'baglanti': baglanti
            })

        kekik_json = {"kaynak": kaynak, 'veri' : udemy}

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak