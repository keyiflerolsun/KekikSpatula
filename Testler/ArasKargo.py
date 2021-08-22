from KekikSpatula import ArasKargo

kargo = ArasKargo(123456789)

print(kargo.veri)
"""
json verisi döndürür

{'kaynak': 'araskargo.com.tr', 'veri': {'takip_no': 123456789, 'durum': {'son_durum': 'TESLİM EDİLDİ', 'teslim_zaman': '2021-07-28 09:51:13.0', 'teslim_alan': 'AB*** CD***'}, 'fatura': {'gonderici': 'D * * G * * * D * * * * * İ * * * V * S * * * * * * * * * * * ', 'cikis_sube': 'ORHANGAZİ', 'varis_sube': 'SARIÇAY', 'cikis_zaman': '2021-07-27 00:00:00.0'}, 'hareketler': [{'islem_zaman': '2021-07-27 16:50:45.0', 'islem_birim': 'BURSA TRANSFER', 'islem_aciklama': 'ÇIKIŞ ŞUBESİNDE; Kargonuz çıkış şubesinden transfer merkezine gönderilmek üzere aracımıza yüklenmiştir. '}, {'islem_zaman': '2021-07-28 02:23:00.0', 'islem_birim': 'SARIÇAY', 'islem_aciklama': 'YOLDA; Kargonuz varış transfer merkezinden varış şubesine gönderiliyor.'}, {'islem_zaman': '2021-07-28 21:46:27.0', 'islem_birim': 'SARIÇAY', 'islem_aciklama': 'TESLİMAT ŞUBESİNDE; Kargonuz transfer merkezimizden teslimat şubemize ulaşmıştır.'}]}}
"""


print(kargo.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "araskargo.com.tr",
  "veri": {
    "takip_no": 123456789,
    "durum": {
      "son_durum": "TESLİM EDİLDİ",
      "teslim_zaman": "2021-07-28 09:51:13.0",
      "teslim_alan": "AB*** CD***"
    },
    "fatura": {
      "gonderici": "D * * G * * * D * * * * * İ * * * V * S * * * * * * * * * * * ",
      "cikis_sube": "ORHANGAZİ",
      "varis_sube": "SARIÇAY",
      "cikis_zaman": "2021-07-27 00:00:00.0"
    },
    "hareketler": [
      {
        "islem_zaman": "2021-07-27 16:50:45.0",
        "islem_birim": "BURSA TRANSFER",
        "islem_aciklama": "ÇIKIŞ ŞUBESİNDE; Kargonuz çıkış şubesinden transfer merkezine gönderilmek üzere aracımıza yüklenmiştir. "
      },
      {
        "islem_zaman": "2021-07-28 02:23:00.0",
        "islem_birim": "SARIÇAY",
        "islem_aciklama": "YOLDA; Kargonuz varış transfer merkezinden varış şubesine gönderiliyor."
      },
      {
        "islem_zaman": "2021-07-28 21:46:27.0",
        "islem_birim": "SARIÇAY",
        "islem_aciklama": "TESLİMAT ŞUBESİNDE; Kargonuz transfer merkezimizden teslimat şubemize ulaşmıştır."
      }
    ]
  }
}
"""