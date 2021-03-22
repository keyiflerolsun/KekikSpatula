from KekikSpatula import Sahibinden

sahibinden = Sahibinden('https://www.sahibinden.com/ilan/vasita-otomobil-porsche-ozkanogullari...2012-porsche-cayman-2.9-265-hp-otomatik-dogus-896061501/detay')

print(sahibinden.veri)
"""
json verisi döndürür

{'kaynak': 'sahibinden.com', 'veri': {'link': 'https://www.sahibinden.com/ilan/vasita-otomobil-porsche-ozkanogullari...2012-porsche-cayman-2.9-265-hp-otomatik-dogus-896061501/detay', 'baslik': 'özkanoğulları...2012 PORSCHE CAYMAN 2.9-265 HP OTOMATIK DOĞUŞ', 'resim': 'https://i0.shbdn.com/photos/06/15/01/x5_896061501xna.jpg', 'fiyat': '745.000 TL', 'yer': 'Bursa | Nilüfer | 23Nisan', 'detay': ['İlan No : 896061501', 'İlan Tarihi : 21 Mart 2021', 'Marka : Porsche', 'Seri : Cayman', 'Model : Cayman', 'Yıl : 2012', 'Yakıt : Benzin', 'Vites : Otomatik', 'KM : 52.000', 'Kasa Tipi : Coupe', 'Motor Gücü : 265 hp', 'Motor Hacmi : 2893 cc', 'Çekiş : Arkadan İtiş', 'Renk : Beyaz', 'Garanti : Hayır', 'Plaka / Uyruk : Türkiye (TR) Plakalı', 'Kimden : Galeriden', 'Görüntülü Arama İle Görülebilir : Evet', 'Takas : Hayır', 'Durumu : İkinci El']}}
"""

print(sahibinden.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "sahibinden.com",
  "veri": {
    "link": "https://www.sahibinden.com/ilan/vasita-otomobil-porsche-ozkanogullari...2012-porsche-cayman-2.9-265-hp-otomatik-dogus-896061501/detay",
    "baslik": "özkanoğulları...2012 PORSCHE CAYMAN 2.9-265 HP OTOMATIK DOĞUŞ",
    "resim": "https://i0.shbdn.com/photos/06/15/01/x5_896061501xna.jpg",
    "fiyat": "745.000 TL",
    "yer": "Bursa | Nilüfer | 23Nisan",
    "detay": [
      "İlan No : 896061501",
      "İlan Tarihi : 21 Mart 2021",
      "Marka : Porsche",
      "Seri : Cayman",
      "Model : Cayman",
      "Yıl : 2012",
      "Yakıt : Benzin",
      "Vites : Otomatik",
      "KM : 52.000",
      "Kasa Tipi : Coupe",
      "Motor Gücü : 265 hp",
      "Motor Hacmi : 2893 cc",
      "Çekiş : Arkadan İtiş",
      "Renk : Beyaz",
      "Garanti : Hayır",
      "Plaka / Uyruk : Türkiye (TR) Plakalı",
      "Kimden : Galeriden",
      "Görüntülü Arama İle Görülebilir : Evet",
      "Takas : Hayır",
      "Durumu : İkinci El"
    ]
  }
}
"""