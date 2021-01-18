from KekikSpatula import Sahibinden

sahibinden = Sahibinden('https://www.sahibinden.com/ilan/vasita-otomobil-porsche-turkiyede-tek-dogus-cikisli-orijinal-racing-yellow-pdk-chrono-890759244/detay')

print(sahibinden.veri)
"""
json verisi döndürür

{'kaynak': 'sahibinden.com', 'veri': {'link': 'https://www.sahibinden.com/ilan/vasita-otomobil-porsche-turkiyede-tek-dogus-cikisli-orijinal-racing-yellow-pdk-chrono-890759244/detay', 'baslik': 'TÜRKİYEDE TEK. Doğuş Çıkışlı Orijinal Racing Yellow-PDK-Chrono', 'resim': 'https://i0.shbdn.com/photos/75/92/44/x5_8907592440mo.jpg', 'fiyat': '1.040.000 TL', 'yer': 'İstanbul | Sarıyer | Baltalimanı', 'detay': ['İlan No : 890759244', 'İlan Tarihi : 15 Ocak 2021', 'Marka : Porsche', 'Seri : Cayman', 'Model : Cayman', 'Yıl : 2013', 'Yakıt : Benzin', 'Vites : Yarı Otomatik', 'KM : 49.356', 'Kasa Tipi : Coupe', 'Motor Gücü : 275 hp', 'Motor Hacmi : 2706 cc', 'Çekiş : Arkadan İtiş', 'Renk : Sarı', 'Garanti : Evet', 'Plaka / Uyruk : Türkiye (TR) Plakalı', 'Kimden : Sahibinden', 'Görüntülü Arama İle Görülebilir : Evet', 'Takas : Hayır', 'Durumu : İkinci El']}}
"""

print(sahibinden.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "sahibinden.com",
  "veri": {
    "link": "https://www.sahibinden.com/ilan/vasita-otomobil-porsche-turkiyede-tek-dogus-cikisli-orijinal-racing-yellow-pdk-chrono-890759244/detay",
    "baslik": "TÜRKİYEDE TEK. Doğuş Çıkışlı Orijinal Racing Yellow-PDK-Chrono",
    "resim": "https://i0.shbdn.com/photos/75/92/44/x5_8907592440mo.jpg",
    "fiyat": "1.040.000 TL",
    "yer": "İstanbul | Sarıyer | Baltalimanı",
    "detay": [
      "İlan No : 890759244",
      "İlan Tarihi : 15 Ocak 2021",
      "Marka : Porsche",
      "Seri : Cayman",
      "Model : Cayman",
      "Yıl : 2013",
      "Yakıt : Benzin",
      "Vites : Yarı Otomatik",
      "KM : 49.356",
      "Kasa Tipi : Coupe",
      "Motor Gücü : 275 hp",
      "Motor Hacmi : 2706 cc",
      "Çekiş : Arkadan İtiş",
      "Renk : Sarı",
      "Garanti : Evet",
      "Plaka / Uyruk : Türkiye (TR) Plakalı",
      "Kimden : Sahibinden",
      "Görüntülü Arama İle Görülebilir : Evet",
      "Takas : Hayır",
      "Durumu : İkinci El"
    ]
  }
}
"""