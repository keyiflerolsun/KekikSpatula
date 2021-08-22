# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

from KekikSpatula import KekikSpatula

class NobetciEczane(KekikSpatula):
    """
    NobetciEczane : eczaneler.gen.tr adresinden nöbetçi eczane verilerini hazır formatlarda elinize verir.

    Öz Nitelikler
    -------------
        il (str): Nöbetçi Eczane Bilgisi istenilen il
        ilce (str): Nöbetçi Eczane Bilgisi istenilen ilçe

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan nöbetçi eczane verilerini döndürmesi için yazılmıştır.."

    def __init__(self, il:str, ilce:str):
        "il ve ilçe bilgisini eczaneler.gen.tr'de arayarak bs4'ile ayrıştırır."

        il      = il.replace('İ', "i").lower()
        ilce    = ilce.lower()

        tr2eng  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
        il      = il.translate(tr2eng)
        ilce    = ilce.translate(tr2eng)

        kaynak  = "eczaneler.gen.tr"
        url     = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
        kimlik  = self.kimlik
        istek   = requests.get(url, headers=kimlik)

        corba = BeautifulSoup(istek.content, "lxml")
        bugun = corba.find('div', id='nav-bugun')

        kekik_json = {"kaynak": kaynak, 'veri' : []}
        try:
            for bak in bugun.findAll('tr')[1:]:
                ad    = bak.find('span', class_='isim').text
                mah   = (None if bak.find('div', class_='my-2') is None else bak.find('div', class_='my-2').text)
                adres = bak.find('div', class_='col-lg-6').text
                tarif = (None if bak.find('span', class_='text-secondary font-italic') is None else bak.find('span', class_='text-secondary font-italic').text)
                telf  = bak.find('div', class_='col-lg-3 py-lg-2').text

                kekik_json['veri'].append({
                    'ad'        : ad,
                    'mahalle'   : mah,
                    'adres'     : adres,
                    'tarif'     : tarif,
                    'telefon'   : telf
                })
        except AttributeError:
            pass

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None
        self.kaynak      = kaynak