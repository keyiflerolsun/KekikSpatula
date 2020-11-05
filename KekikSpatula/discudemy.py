# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

class DiscUdemy(object):
    """
    DiscUdemy : discudemy.com adresinden Udemy Kurslarını hazır formatlarda elinize verir.

    Methodlar
    ----------
        .veri()         -> dict:
            json verisi döndürür.

        .gorsel()       -> str:
            oluşan json verisini insanın okuyabileceği formatta döndürür.

        .tablo()        -> str:
            tabulate verisi döndürür.

        .anahtarlar()   -> list:
            kullanılan anahtar listesini döndürür.
    """
    def __init__(self, kategori:str):
        """Kategoriye göre Udemy Kurslarını discudemy.com'dan alarak bs4'ile ayrıştırır."""
        super().__init__()

        kaynak  = "discudemy.com"
        url     = f"https://www.discudemy.com/s-r/{kategori}.jsf"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
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

        json = {"kaynak": kaynak, 'veri' : udemy}

        self.json  = json if json['veri'] != [] else None

    def veri(self):
        """json verisi döndürür."""
        return self.json or None

    def gorsel(self, girinti:int=2, alfabetik:bool=False):
        """oluşan json verisini insanın okuyabileceği formatta döndürür."""
        return json.dumps(self.json, indent=girinti, sort_keys=alfabetik, ensure_ascii=False) if self.json else None

    def tablo(self, tablo_turu:str='psql'):
        """tabulate verisi döndürür."""
        return tabulate(self.json['veri'], headers='keys', tablefmt=tablo_turu) if self.json else None

    def anahtarlar(self):
        """kullanılan anahtar listesini döndürür."""
        return [anahtar for anahtar in self.json['veri'][0].keys()] if self.json else None