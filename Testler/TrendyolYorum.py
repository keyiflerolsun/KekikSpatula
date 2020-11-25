from KekikSpatula import TrendyolYorum

tr_yorum = TrendyolYorum('https://www.trendyol.com/soly/meltblown-filtre-3-katli-tam-ultrasonik-cerrahi-maske-yesil-100-adet-p-47636885?boutiqueId=535465&merchantId=184993')

print(tr_yorum.veri)
"""
json verisi döndürür

{'kaynak': 'trendyol.com', 'urun_linki': 'https://www.trendyol.com/soly/meltblown-filtre-3-katli-tam-ultrasonik-cerrahi-maske-yesil-100-adet-p-47636885', 'urun_adi': 'Meltblown Filtre 3 Katlı Tam Ultrasonik Cerrahi Maske Yeşil 100 Adet SOLYMLT100YESIL', 'veri': [{'kullanici': '**** ****', 'yildiz': 5, 'yorum': 'Kaliteli ürün, Teşekkürler.'}, {'kullanici': 's** a**', 'yildiz': 5, 'yorum': 'çok memnunum bu maskeden.Tedarikç firmada çok iyi tavsiye ederim'}, {'kullanici': 'Mehmet Yılmaz', 'yildiz': 4, 'yorum': 'Ürün kaliteli.'}, {'kullanici': 'B** g**', 'yildiz': 5, 'yorum': 'Şuana kadar kullandığım en iyi maske'}, {'kullanici': '**** ****', 'yildiz': 5, 'yorum': 'yeşil yazıyordu ama maske beyaz geldi yoksa kalitesi çok güzel'}, {'kullanici': '**** ****', 'yildiz': 5, 'yorum': 'ürün üfleme testinden geçiyor.'}, {'kullanici': 'M** G**', 'yildiz': 5, 'yorum': 'ilk aldığım ve hemen iade ettiğim üründen sonra, doğru tercihi yapmışım. kargo ambalajlama herşey mükemmel. maskenin yeşil renk olduğunu kutusunda beyaz göründüğünü bile küçük ve tatlı bir not ile belirtmişler. satıcı firma için harika bir artı. tebrikler ve teşekkürler.'}, {'kullanici': 'S** D**', 'yildiz': 2, 'yorum': 'Lastikleri çok gevşek eşim kullanmamış olsa kesin iade ederdim'}, {'kullanici': 'Ş** A**', 'yildiz': 5, 'yorum': 'Muhteşem paketleme,hızlı kargo,güvenli maske,teşekkürler'}, {'kullanici': 'Mehmet Öztoprak', 'yildiz': 1, 'yorum': 'Meltblown değil ve üç katlıda değil.'}]}
"""

for tr_yorum_nesnesi in tr_yorum.nesne:
    print(tr_yorum_nesnesi.yildiz)
"""
json verisini python nesnesine dönüştürür.

5
5
4
5
5
5
5
2
5
1
"""


print(tr_yorum.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "trendyol.com",
  "urun_linki": "https://www.trendyol.com/soly/meltblown-filtre-3-katli-tam-ultrasonik-cerrahi-maske-yesil-100-adet-p-47636885",
  "urun_adi": "Meltblown Filtre 3 Katlı Tam Ultrasonik Cerrahi Maske Yeşil 100 Adet SOLYMLT100YESIL",
  "veri": [
    {
      "kullanici": "**** ****",
      "yildiz": 5,
      "yorum": "Kaliteli ürün, Teşekkürler."
    },
    {
      "kullanici": "s** a**",
      "yildiz": 5,
      "yorum": "çok memnunum bu maskeden.Tedarikç firmada çok iyi tavsiye ederim"
    },
    {
      "kullanici": "Mehmet Yılmaz",
      "yildiz": 4,
      "yorum": "Ürün kaliteli."
    },
    {
      "kullanici": "B** g**",
      "yildiz": 5,
      "yorum": "Şuana kadar kullandığım en iyi maske"
    },
    {
      "kullanici": "**** ****",
      "yildiz": 5,
      "yorum": "yeşil yazıyordu ama maske beyaz geldi yoksa kalitesi çok güzel"
    },
    {
      "kullanici": "**** ****",
      "yildiz": 5,
      "yorum": "ürün üfleme testinden geçiyor."
    },
    {
      "kullanici": "M** G**",
      "yildiz": 5,
      "yorum": "ilk aldığım ve hemen iade ettiğim üründen sonra, doğru tercihi yapmışım. kargo ambalajlama herşey mükemmel. maskenin yeşil renk olduğunu kutusunda beyaz göründüğünü bile küçük ve tatlı bir not ile belirtmişler. satıcı firma için harika bir artı. tebrikler ve teşekkürler."
    },
    {
      "kullanici": "S** D**",
      "yildiz": 2,
      "yorum": "Lastikleri çok gevşek eşim kullanmamış olsa kesin iade ederdim"
    },
    {
      "kullanici": "Ş** A**",
      "yildiz": 5,
      "yorum": "Muhteşem paketleme,hızlı kargo,güvenli maske,teşekkürler"
    },
    {
      "kullanici": "Mehmet Öztoprak",
      "yildiz": 1,
      "yorum": "Meltblown değil ve üç katlıda değil."
    }
  ]
}
"""

print(tr_yorum.tablo())
"""
tabulate verisi döndürür.

+-----------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kullanici       |   yildiz | yorum                                                                                                                                                                                                                                                                           |
|-----------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **** ****       |        5 | Kaliteli ürün, Teşekkürler.                                                                                                                                                                                                                                                     |
| s** a**         |        5 | çok memnunum bu maskeden.Tedarikç firmada çok iyi tavsiye ederim                                                                                                                                                                                                                |
| Mehmet Yılmaz   |        4 | Ürün kaliteli.                                                                                                                                                                                                                                                                  |
| B** g**         |        5 | Şuana kadar kullandığım en iyi maske                                                                                                                                                                                                                                            |
| **** ****       |        5 | yeşil yazıyordu ama maske beyaz geldi yoksa kalitesi çok güzel                                                                                                                                                                                                                  |
| **** ****       |        5 | ürün üfleme testinden geçiyor.                                                                                                                                                                                                                                                  |
| M** G**         |        5 | ilk aldığım ve hemen iade ettiğim üründen sonra, doğru tercihi yapmışım. kargo ambalajlama herşey mükemmel. maskenin yeşil renk olduğunu kutusunda beyaz göründüğünü bile küçük ve tatlı bir not ile belirtmişler. satıcı firma için harika bir artı. tebrikler ve teşekkürler. |
| S** D**         |        2 | Lastikleri çok gevşek eşim kullanmamış olsa kesin iade ederdim                                                                                                                                                                                                                  |
| Ş** A**         |        5 | Muhteşem paketleme,hızlı kargo,güvenli maske,teşekkürler                                                                                                                                                                                                                        |
| Mehmet Öztoprak |        1 | Meltblown değil ve üç katlıda değil.                                                                                                                                                                                                                                            |
+-----------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

print(tr_yorum.anahtarlar)
"""
kullanılan anahtar listesini döndürür.

['kullanici', 'yildiz', 'yorum']
"""