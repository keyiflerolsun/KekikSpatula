# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

class NobetciEczane(object):
    """
    NobetciEczane : eczaneler.gen.tr adresinden nöbetçi eczane verilerini hazır formatlarda elinize verir.

    Öz Nitelikler
    -------------
        il (str): Nöbetçi Eczane Bilgisi istenilen il
        ilce (str): Nöbetçi Eczane Bilgisi istenilen ilçe

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
    def __init__(self, il:str, ilce:str):
        """il ve ilçe bilgisini eczaneler.gen.tr'de arayarak bs4'ile ayrıştırır."""
        super().__init__()

        il      = il.replace('İ', "i").lower()
        ilce    = ilce.lower()

        tr2eng  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
        il      = il.translate(tr2eng)
        ilce    = ilce.translate(tr2eng)

        kaynak  = "eczaneler.gen.tr"
        url     = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        istek   = requests.get(url, headers=kimlik)

        corba = BeautifulSoup(istek.content, "lxml")
        bugun = corba.find('div', id='nav-bugun')

        json = {"kaynak": kaynak, 'veri' : []}
        try:
            for bak in bugun.findAll('tr')[1:]:
                ad    = bak.find('span', class_='isim').text
                mah   = (None if bak.find('div', class_='my-2') is None else bak.find('div', class_='my-2').text)
                adres = bak.find('span', class_='text-capitalize').text
                tarif = (None if bak.find('span', class_='text-secondary font-italic') is None else bak.find('span', class_='text-secondary font-italic').text)
                telf  = bak.find('div', class_='col-lg-3 py-lg-2').text

                json['veri'].append({
                    'ad'        : ad,
                    'mahalle'   : mah,
                    'adres'     : adres,
                    'tarif'     : tarif,
                    'telefon'   : telf
                })
        except AttributeError:
            pass

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