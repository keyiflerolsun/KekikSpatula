# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from aiohttp import ClientSession
from asyncio import run
from atexit  import register as kapanirken
from parsel  import Selector
from regex   import search

class KekikGoogle:
    def __oturum_kapa(self):
        run(self.oturum.close())

    def __init__(self, dil:str="tr"):
        self.oturum = ClientSession()
        kapanirken(self.__oturum_kapa)

        self.dil    = dil
        self.kimlik = {
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Host"       : "www.google.com",
            "Referer"    : "https://www.google.com/",
        }

    async def __kaynak_kodu(self, sorgu:str) -> str:
        async with self.oturum.get(
            url     = "https://www.google.com/search",
            headers = self.kimlik,
            params  = {
                "q"  : sorgu,
                "lr" : f"lang_{self.dil.lower()}"
            },
        ) as yanit:
            return await yanit.text()

    async def __tarih_var_mi(self, metin:str) -> str | None:
        if tarih := search(r"([0-9]* [\D]{3} [0-9]{4})", metin) or search(r"([0-9]*\.[\d]{2}\.[0-9]{4})", metin):
            return tarih.group(1)
        else:
            return None

    async def __sonuc_duzenle(self, sonuclar:list) -> list:
        __sonuclar = []
        for sonuc in sonuclar:
            if tarih := await self.__tarih_var_mi(sonuc["aciklama"]):
                sonuc["tarih"]    = tarih
                sonuc["aciklama"] = sonuc["aciklama"].strip(f"{tarih} — ")
            else:
                sonuc["tarih"] = None

            __sonuclar.append(sonuc)

        return __sonuclar

    async def ara(self, sorgu: str) -> dict:
        kaynak_kod = await self.__kaynak_kodu(sorgu)
        secici     = Selector(kaynak_kod)

        bunlari_da_sordu = secici.xpath("//div[@jsname='Cpkphb']")
        oneriler         = [
            oneri.xpath("normalize-space(.//div[@data-q]/@data-q)").get()
              for oneri in bunlari_da_sordu
        ]

        sonuclar = secici.xpath("//div[@class='v7W49e']//div[@class='MjjYud']")
        sonuclar = await self.__sonuc_duzenle([
            {
                "link"     : sonuc.xpath(".//div[@class='yuRUbf']/a/@href").get(),
                "baslik"   : sonuc.xpath(".//div[@class='yuRUbf']/a/h3/text()").get(),
                "aciklama" : sonuc.xpath("normalize-space(.//div[contains(@class, 'yXK7lf')])").get().replace("\xa0", "")
            }
              for sonuc in sonuclar if sonuc.xpath(".//div[@class='yuRUbf']/a/@href").get()
        ])


        if not any([sonuclar, oneriler]):
            with open("bakalim.html", "w+") as dosya:
                dosya.write(kaynak_kod)

        cevap = secici.xpath("normalize-space(//div[@class='wDYxhc'])").get()
        if tarih := await self.__tarih_var_mi(cevap):
            cevap = cevap.strip(tarih).strip()
            sonuclar[0]["aciklama"] = cevap
            sonuclar[0]["tarih"] = tarih

        return {
            "sonuclar" : sonuclar,
            "cevap"    : cevap or None,
            "oneriler" : oneriler
        }