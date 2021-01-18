from KekikSpatula import Trendyol

trendyol = Trendyol('https://www.trendyol.com/soly/meltblown-filtre-3-katli-tam-ultrasonik-cerrahi-maske-yesil-100-adet-p-47636885?boutiqueId=535465&merchantId=184993')

print(trendyol.veri)
"""
json verisi döndürür

{'kaynak': 'trendyol.com', 'veri': {'link': 'https://www.trendyol.com/soly/meltblown-filtre-3-katli-tam-ultrasonik-cerrahi-maske-yesil-100-adet-p-47636885', 'marka': 'Soly', 'baslik': 'Meltblown Filtre 3 Katlı Tam Ultrasonik Cerrahi Maske Yeşil 100 Adet SOLYMLT100YESIL', 'resim': 'https://cdn.dsmcdn.com/mnresize/415/622/ty12/product/media/images/20200903/18/9515780/84286564/1/1_org_zoom.jpg', 'gercek': '125,00 TL', 'indirimli': '58 TL', 'kampanya': None, 'son_fiyat': None, 'yorumlar': [{'kullanici': 'Ş** A**', 'yildiz': 5, 'yorum': 'Muhteşem paketleme,hızlı kargo,güvenli maske,teşekkürler'}, {'kullanici': 'M** G**', 'yildiz': 5, 'yorum': 'ilk aldığım ve hemen iade ettiğim üründen sonra, doğru tercihi yapmışım. kargo ambalajlama herşey mükemmel. maskenin yeşil renk olduğunu kutusunda beyaz göründüğünü bile küçük ve tatlı bir not ile belirtmişler. satıcı firma için harika bir artı. tebrikler ve teşekkürler.'}, {'kullanici': 's** a**', 'yildiz': 5, 'yorum': 'çok memnunum bu maskeden.Tedarikç firmada çok iyi tavsiye ederim'}, {'kullanici': '**** ****', 'yildiz': 5, 'yorum': 'yeşil yazıyordu ama maske beyaz geldi yoksa kalitesi çok güzel'}, {'kullanici': 'B** g**', 'yildiz': 1, 'yorum': 'İlk siparişte aylar önce kutu içeriğimde mavi renkteydiler. Yeni verdiğim aynı marka aynı kutu resimlemelerine kadar birebir olmasına rağmen içinden su yeşili renkte tüy gibi hafif hava geçiren maskelerden çıktı. Hem fiyatı arttırmışlar hem kalite yerlerde. Bir daha bu markadan maske siparişi vermem.'}, {'kullanici': '**** ****', 'yildiz': 5, 'yorum': 'Kaliteli ürün, Teşekkürler.'}, {'kullanici': '**** ****', 'yildiz': 5, 'yorum': 'ürün üfleme testinden geçiyor.'}, {'kullanici': 'GAMZE KARA', 'yildiz': 5, 'yorum': 'Kaliteli bir maske'}, {'kullanici': 'S** D**', 'yildiz': 2, 'yorum': 'Lastikleri çok gevşek eşim kullanmamış olsa kesin iade ederdim'}, {'kullanici': 'Mehmet Yılmaz', 'yildiz': 4, 'yorum': 'Ürün kaliteli.'}, {'kullanici': 'Mehmet Öztoprak', 'yildiz': 1, 'yorum': 'Meltblown değil ve üç katlıda değil.'}, {'kullanici': 'E** A**', 'yildiz': 5, 'yorum': 'Feride çakar satıcısından alın harika ürün'}, {'kullanici': '**** ****', 'yildiz': 1, 'yorum': 'MALESEF HİÇ UMDUĞUMU BULAMADIM İP KOPUYOR VE ÇOK GEVŞEK İÇİNDEKİ MELTBLOW MADDE ÇOK BASİT DİĞER MARKALARINKİ İLE KARŞILAŞTIRDIM.MALESEF'}, {'kullanici': 'ece esen', 'yildiz': 1, 'yorum': 'ürünü onaylı oldugu için tercih ettim,, fakat daha takarken elimde kalıyor lastik yeri kopuyor 2 kutu almıştm pişmanım,,  çekiltirmedim ve küçük kafalı biriyim ona rağmen;)'}, {'kullanici': 'pınar bekci', 'yildiz': 5, 'yorum': 'Maskelerin bu şekilde standartlara uygun bir maske olması gerekiyor. Diğer standartlara uygun olmayan maskelerin maske olmadığını b maskeyi kullanınca. anlayacaksınız. Biz memnunuz. Sadece kendime değil etrafımdaki herkese tavsiye ediyorum, aldırıyorum. Benim 3. Siparişim olacak. Evdeki diğer maskeler çöpe gitti. Fakat fiyatı daha da indirebilseler çok güzel olur ama emin olun hiç koruması olmayan maskelerin fiyatlarına bakınca normal de geliyor bu fiyat.'}, {'kullanici': 'Sinem Tekin', 'yildiz': 3, 'yorum': 'İpleri çabuk kopuyor yoksa güzel maske.'}, {'kullanici': '**** ****', 'yildiz': 4, 'yorum': 'Daha önce kullandığım marka fakat bu sefer ipleri biraz daha uzun'}, {'kullanici': 'Muammer Demir', 'yildiz': 5, 'yorum': 'ürün anlatıldığı gibi güzel. hava akışı güzel. üflediğin zaman çakmak sönmüyor. kulak lastik kısmı uzun. kulakta mı değil mi belli değil. tavsiye ederim.'}]}}
"""

print(trendyol.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "trendyol.com",
  "veri": {
    "link": "https://www.trendyol.com/soly/meltblown-filtre-3-katli-tam-ultrasonik-cerrahi-maske-yesil-100-adet-p-47636885",
    "marka": "Soly",
    "baslik": "Meltblown Filtre 3 Katlı Tam Ultrasonik Cerrahi Maske Yeşil 100 Adet SOLYMLT100YESIL",
    "resim": "https://cdn.dsmcdn.com/mnresize/415/622/ty12/product/media/images/20200903/18/9515780/84286564/1/1_org_zoom.jpg",
    "gercek": "125,00 TL",
    "indirimli": "58 TL",
    "kampanya": null,
    "son_fiyat": null,
    "yorumlar": [
      {
        "kullanici": "Ş** A**",
        "yildiz": 5,
        "yorum": "Muhteşem paketleme,hızlı kargo,güvenli maske,teşekkürler"
      },
      {
        "kullanici": "M** G**",
        "yildiz": 5,
        "yorum": "ilk aldığım ve hemen iade ettiğim üründen sonra, doğru tercihi yapmışım. kargo ambalajlama herşey mükemmel. maskenin yeşil renk olduğunu kutusunda beyaz göründüğünü bile küçük ve tatlı bir not ile belirtmişler. satıcı firma için harika bir artı. tebrikler ve teşekkürler."
      },
      {
        "kullanici": "s** a**",
        "yildiz": 5,
        "yorum": "çok memnunum bu maskeden.Tedarikç firmada çok iyi tavsiye ederim"
      },
      {
        "kullanici": "**** ****",
        "yildiz": 5,
        "yorum": "yeşil yazıyordu ama maske beyaz geldi yoksa kalitesi çok güzel"
      },
      {
        "kullanici": "B** g**",
        "yildiz": 1,
        "yorum": "İlk siparişte aylar önce kutu içeriğimde mavi renkteydiler. Yeni verdiğim aynı marka aynı kutu resimlemelerine kadar birebir olmasına rağmen içinden su yeşili renkte tüy gibi hafif hava geçiren maskelerden çıktı. Hem fiyatı arttırmışlar hem kalite yerlerde. Bir daha bu markadan maske siparişi vermem."
      },
      {
        "kullanici": "**** ****",
        "yildiz": 5,
        "yorum": "Kaliteli ürün, Teşekkürler."
      },
      {
        "kullanici": "**** ****",
        "yildiz": 5,
        "yorum": "ürün üfleme testinden geçiyor."
      },
      {
        "kullanici": "GAMZE KARA",
        "yildiz": 5,
        "yorum": "Kaliteli bir maske"
      },
      {
        "kullanici": "S** D**",
        "yildiz": 2,
        "yorum": "Lastikleri çok gevşek eşim kullanmamış olsa kesin iade ederdim"
      },
      {
        "kullanici": "Mehmet Yılmaz",
        "yildiz": 4,
        "yorum": "Ürün kaliteli."
      },
      {
        "kullanici": "Mehmet Öztoprak",
        "yildiz": 1,
        "yorum": "Meltblown değil ve üç katlıda değil."
      },
      {
        "kullanici": "E** A**",
        "yildiz": 5,
        "yorum": "Feride çakar satıcısından alın harika ürün"
      },
      {
        "kullanici": "**** ****",
        "yildiz": 1,
        "yorum": "MALESEF HİÇ UMDUĞUMU BULAMADIM İP KOPUYOR VE ÇOK GEVŞEK İÇİNDEKİ MELTBLOW MADDE ÇOK BASİT DİĞER MARKALARINKİ İLE KARŞILAŞTIRDIM.MALESEF"
      },
      {
        "kullanici": "ece esen",
        "yildiz": 1,
        "yorum": "ürünü onaylı oldugu için tercih ettim,, fakat daha takarken elimde kalıyor lastik yeri kopuyor 2 kutu almıştm pişmanım,,  çekiltirmedim ve küçük kafalı biriyim ona rağmen;)"
      },
      {
        "kullanici": "pınar bekci",
        "yildiz": 5,
        "yorum": "Maskelerin bu şekilde standartlara uygun bir maske olması gerekiyor. Diğer standartlara uygun olmayan maskelerin maske olmadığını b maskeyi kullanınca. anlayacaksınız. Biz memnunuz. Sadece kendime değil etrafımdaki herkese tavsiye ediyorum, aldırıyorum. Benim 3. Siparişim olacak. Evdeki diğer maskeler çöpe gitti. Fakat fiyatı daha da indirebilseler çok güzel olur ama emin olun hiç koruması olmayan maskelerin fiyatlarına bakınca normal de geliyor bu fiyat."
      },
      {
        "kullanici": "Sinem Tekin",
        "yildiz": 3,
        "yorum": "İpleri çabuk kopuyor yoksa güzel maske."
      },
      {
        "kullanici": "**** ****",
        "yildiz": 4,
        "yorum": "Daha önce kullandığım marka fakat bu sefer ipleri biraz daha uzun"
      },
      {
        "kullanici": "Muammer Demir",
        "yildiz": 5,
        "yorum": "ürün anlatıldığı gibi güzel. hava akışı güzel. üflediğin zaman çakmak sönmüyor. kulak lastik kısmı uzun. kulakta mı değil mi belli değil. tavsiye ederim."
      }
    ]
  }
}
"""