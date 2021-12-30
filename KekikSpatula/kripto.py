# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests

from KekikSpatula import KekikSpatula

class Kripto(KekikSpatula):
    """
    Kripto : api.binance.com adresinden kline/candlestick verilerini hazır formatlarda elinize verir.

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
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan kline/candlestick verisini döndürmesi için yazılmıştır.."

    def __init__(self, sembol:str, aralik:str):
        "klines verisini api.binance.com'dan alarak düzenli bir format verir."

        kekik_json = []
        self.kaynak  = "api.binance.com"
        kullanilabilir_aralik = [ "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M" ]
        sembol = sembol.upper()

        if aralik not in kullanilabilir_aralik:
          kekik_json = {
            "kaynak" : self.kaynak,
            "veri": {
              "hata": "Aralık hatası",
              "bilgilendirme": "m -> minutes; h -> hours; d -> days; w -> weeks; M -> months",
              "aralik": kullanilabilir_aralik,
            }
          }
        else:
          sembol_kontrol_url = f"https://{self.kaynak}/api/v3/ticker/24hr?symbol={sembol}"
          sembol_kontrol_istek   = requests.get(sembol_kontrol_url)
          if sembol_kontrol_istek.status_code != 400:
            url     = f"https://{self.kaynak}/api/v3/klines?symbol={sembol}&interval={aralik}"
            istek   = requests.get(url)

            if istek.status_code == 200:
              veri = [
                {
                  "acilis_zamani"                   : veri[0],
                  "acilis"                          : veri[1],
                  "en_yuksek"                       : veri[2],
                  "en_dusuk"                        : veri[3],
                  "kapanis"                         : veri[4],
                  "hacim"                           : veri[5],
                  "kapanis_zamani"                  : veri[6],
                  "teklif_varlik_hacmi"             : veri[7],
                  "islem_sayisi"                    : veri[8],
                  "satin_alma_temel_varlik_hacmi"   : veri[9],
                  "satın_alma_teklifi_varlik_hacmi" : veri[10],
                }
                for veri in istek.json()
              ]
            else:
              kekik_json = {
                "kaynak" : self.kaynak,
                "veri": {
                  "hata": istek.json()["msg"],
                  "kod": istek.json()["code"],
                  "cozum": "Çıkan hata kodunu burda aratın https://github.com/binance/binance-spot-api-docs/blob/master/errors.md"
                }
              }

            kekik_json = {
              "kaynak": self.kaynak,
              "veri": veri
            }
          else:
            kekik_json = {
              "kaynak" : self.kaynak,
              "veri": {
                "hata": sembol_kontrol_istek.json()["msg"],
                "kod": sembol_kontrol_istek.json()["code"],
                "cozum": "Çıkan hata kodunu burda aratın https://github.com/binance/binance-spot-api-docs/blob/master/errors.md"
              }
            }

        self.kekik_json  = kekik_json if kekik_json['veri'] != [] else None