from KekikSpatula import Google

google = Google('lorem impsum sit amet')

print(google.veri)
"""
json verisi döndürür

{'kaynak': 'google.com', 'veri': [{'baslik': 'Lorem Ipsum - All the facts - Lipsum generator', 'link': 'https://tr.lipsum.com/', 'aciklama': 'Lorem Ipsum pasajının ilk satırı olan "Lorem ipsum dolor sit amet" 1.10.32 sayılı bölümdeki bir satırdan gelmektedir. 1500\'lerden beri kullanılmakta olan standard \xa0...'}, {'baslik': 'Word Yardımı\'ndaki "Lorem ipsum dolor sit amet" metninin açıklaması', 'link': 'https://support.microsoft.com/tr-tr/help/114222/description-of-the-lorem-ipsum-dolor-sit-amet-text-that-appears-in-wor', 'aciklama': '17 Nis 2018 · Word Yardımı\'ndaki "Lorem ipsum dolor sit amet consectetuer" ile başlayan metin açıklanır. Metin, Latince\'ye benzer anlamsız bir cümledir ve\xa0...'}, {'baslik': 'lorem ipsum dolor sit amet - ekşi sözlük', 'link': 'https://eksisozluk.com/lorem-ipsum-dolor-sit-amet--921134', 'aciklama': 'lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. at\xa0...'}, {'baslik': 'Lorem Ipsum ne demek, ne işe yarar? Lorem Ipsum anlamı - Haberler', 'link': 'https://www.haberler.com/lorem-ipsum-ne-demek-ne-ise-yarar-lorem-ipsum-12576394-haberi/', 'aciklama': "2 Kas 2019 · Peki, lorem ipsum dolor sit amet nedir? Google'da bile henüz taslak halinde olan sitelerin sıralandığı Lorem ıpsum kavramı, metro istasyonlarına\xa0..."}, {'baslik': 'Lorem Ipsum Nedir ve Ne Anlama Gelir?', 'link': 'https://www.bidolubaski.com/blog/lorem-ipsum-nedir-ve-ne-anlama-gelir', 'aciklama': '"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis\xa0...'}, {'baslik': 'Lorem İpsum Dolor Sit Amet - Taha Akkurt', 'link': 'https://akkurttaha.blogspot.com/2019/07/lorem-ipsum-dolor-sit-amet.html', 'aciklama': '9 Tem 2019 · Lorem ipsum dolor sit amet… Hiç bu şekilde devam eden bir yazıyla karşılaştınız mı? Örneğin MS Office Word yardımında ya da hazır temalara\xa0...'}, {'baslik': 'Lorem Ipsum - Vikipedi', 'link': 'https://tr.wikipedia.org/wiki/Lorem_Ipsum', 'aciklama': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis\xa0...'}, {'baslik': 'Lorem Ipsum Dolor Sit Amet - Uçak Tekstil', 'link': 'https://ucaktekstil.com.tr/lorem-ipsum-dolor-sit-amet-5/', 'aciklama': 'Lorem Ipsum Dolor Sit Amet. Yaygın inancın tersine, Lorem Ipsum rastgele sözcüklerden oluşmaz. Kökleri M.Ö. 45 tarihinden bu yana klasik Latin edebiyatına\xa0...'}, {'baslik': 'lorem ipsum dolor sit amet - uludağ sözlük', 'link': 'https://www.uludagsozluk.com/k/lorem-ipsum-dolor-sit-amet/', 'aciklama': 'Lorem Ipsum, 500 yıl boyunca varlığını sürdürmekle kalmamış ve günümüzde elektronik yazı tipinin gerektiği birçok konuda hazır bir araç olarak kullanılmaya\xa0...'}, {'baslik': 'Lorem Ipsum: Anlıyorum ama konuşamıyorum! - Kampüs Haberleri', 'link': 'https://www.hurriyet.com.tr/kampus/lorem-ipsum-anliyorum-ama-konusamiyorum-40364027', 'aciklama': '13 Şub 2017 · Soner Sezer Lorem Ipsum meselesini sizin için yazdı. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci\xa0...'}]}
"""

for urun in google.nesne:
  print(urun.aciklama)
"""
json verisini python nesnesine dönüştürür.

Lorem Ipsum pasajının ilk satırı olan "Lorem ipsum dolor sit amet" 1.10.32 sayılı bölümdeki bir satırdan gelmektedir. 1500'lerden beri kullanılmakta olan standard  ...
17 Nis 2018 · Word Yardımı'ndaki "Lorem ipsum dolor sit amet consectetuer" ile başlayan metin açıklanır. Metin, Latince'ye benzer anlamsız bir cümledir ve ...
lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. at ...
2 Kas 2019 · Peki, lorem ipsum dolor sit amet nedir? Google'da bile henüz taslak halinde olan sitelerin sıralandığı Lorem ıpsum kavramı, metro istasyonlarına ...
"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis ...
9 Tem 2019 · Lorem ipsum dolor sit amet… Hiç bu şekilde devam eden bir yazıyla karşılaştınız mı? Örneğin MS Office Word yardımında ya da hazır temalara ...
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis ...
Lorem Ipsum Dolor Sit Amet. Yaygın inancın tersine, Lorem Ipsum rastgele sözcüklerden oluşmaz. Kökleri M.Ö. 45 tarihinden bu yana klasik Latin edebiyatına ...
Lorem Ipsum, 500 yıl boyunca varlığını sürdürmekle kalmamış ve günümüzde elektronik yazı tipinin gerektiği birçok konuda hazır bir araç olarak kullanılmaya ...
13 Şub 2017 · Soner Sezer Lorem Ipsum meselesini sizin için yazdı. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci ...
"""


print(google.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "google.com",
  "veri": [
    {
      "baslik": "Lorem Ipsum - All the facts - Lipsum generator",
      "link": "https://tr.lipsum.com/",
      "aciklama": "Lorem Ipsum pasajının ilk satırı olan \"Lorem ipsum dolor sit amet\" 1.10.32 sayılı bölümdeki bir satırdan gelmektedir. 1500'lerden beri kullanılmakta olan standard  ..."
    },
    {
      "baslik": "Word Yardımı'ndaki \"Lorem ipsum dolor sit amet\" metninin açıklaması",
      "link": "https://support.microsoft.com/tr-tr/help/114222/description-of-the-lorem-ipsum-dolor-sit-amet-text-that-appears-in-wor",
      "aciklama": "17 Nis 2018 · Word Yardımı'ndaki \"Lorem ipsum dolor sit amet consectetuer\" ile başlayan metin açıklanır. Metin, Latince'ye benzer anlamsız bir cümledir ve ..."
    },
    {
      "baslik": "lorem ipsum dolor sit amet - ekşi sözlük",
      "link": "https://eksisozluk.com/lorem-ipsum-dolor-sit-amet--921134",
      "aciklama": "lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. at ..."
    },
    {
      "baslik": "Lorem Ipsum ne demek, ne işe yarar? Lorem Ipsum anlamı - Haberler",
      "link": "https://www.haberler.com/lorem-ipsum-ne-demek-ne-ise-yarar-lorem-ipsum-12576394-haberi/",
      "aciklama": "2 Kas 2019 · Peki, lorem ipsum dolor sit amet nedir? Google'da bile henüz taslak halinde olan sitelerin sıralandığı Lorem ıpsum kavramı, metro istasyonlarına ..."
    },
    {
      "baslik": "Lorem Ipsum Nedir ve Ne Anlama Gelir?",
      "link": "https://www.bidolubaski.com/blog/lorem-ipsum-nedir-ve-ne-anlama-gelir",
      "aciklama": "\"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis ..."
    },
    {
      "baslik": "Lorem İpsum Dolor Sit Amet - Taha Akkurt",
      "link": "https://akkurttaha.blogspot.com/2019/07/lorem-ipsum-dolor-sit-amet.html",
      "aciklama": "9 Tem 2019 · Lorem ipsum dolor sit amet… Hiç bu şekilde devam eden bir yazıyla karşılaştınız mı? Örneğin MS Office Word yardımında ya da hazır temalara ..."
    },
    {
      "baslik": "Lorem Ipsum - Vikipedi",
      "link": "https://tr.wikipedia.org/wiki/Lorem_Ipsum",
      "aciklama": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis ..."
    },
    {
      "baslik": "Lorem Ipsum Dolor Sit Amet - Uçak Tekstil",
      "link": "https://ucaktekstil.com.tr/lorem-ipsum-dolor-sit-amet-5/",
      "aciklama": "Lorem Ipsum Dolor Sit Amet. Yaygın inancın tersine, Lorem Ipsum rastgele sözcüklerden oluşmaz. Kökleri M.Ö. 45 tarihinden bu yana klasik Latin edebiyatına ..."
    },
    {
      "baslik": "lorem ipsum dolor sit amet - uludağ sözlük",
      "link": "https://www.uludagsozluk.com/k/lorem-ipsum-dolor-sit-amet/",
      "aciklama": "Lorem Ipsum, 500 yıl boyunca varlığını sürdürmekle kalmamış ve günümüzde elektronik yazı tipinin gerektiği birçok konuda hazır bir araç olarak kullanılmaya ..."
    },
    {
      "baslik": "Lorem Ipsum: Anlıyorum ama konuşamıyorum! - Kampüs Haberleri",
      "link": "https://www.hurriyet.com.tr/kampus/lorem-ipsum-anliyorum-ama-konusamiyorum-40364027",
      "aciklama": "13 Şub 2017 · Soner Sezer Lorem Ipsum meselesini sizin için yazdı. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci ..."
    }
  ]
}
"""

print(google.tablo())
"""
tabulate verisi döndürür.

+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| baslik                                                              | link                                                                                                                   | aciklama                                                                                                                                                                |
|---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lorem Ipsum - All the facts - Lipsum generator                      | https://tr.lipsum.com/                                                                                                 | Lorem Ipsum pasajının ilk satırı olan "Lorem ipsum dolor sit amet" 1.10.32 sayılı bölümdeki bir satırdan gelmektedir. 1500'lerden beri kullanılmakta olan standard  ... |
| Word Yardımı'ndaki "Lorem ipsum dolor sit amet" metninin açıklaması | https://support.microsoft.com/tr-tr/help/114222/description-of-the-lorem-ipsum-dolor-sit-amet-text-that-appears-in-wor | 17 Nis 2018 · Word Yardımı'ndaki "Lorem ipsum dolor sit amet consectetuer" ile başlayan metin açıklanır. Metin, Latince'ye benzer anlamsız bir cümledir ve ...          |
| lorem ipsum dolor sit amet - ekşi sözlük                            | https://eksisozluk.com/lorem-ipsum-dolor-sit-amet--921134                                                              | lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. at ...      |
| Lorem Ipsum ne demek, ne işe yarar? Lorem Ipsum anlamı - Haberler   | https://www.haberler.com/lorem-ipsum-ne-demek-ne-ise-yarar-lorem-ipsum-12576394-haberi/                                | 2 Kas 2019 · Peki, lorem ipsum dolor sit amet nedir? Google'da bile henüz taslak halinde olan sitelerin sıralandığı Lorem ıpsum kavramı, metro istasyonlarına ...       |
| Lorem Ipsum Nedir ve Ne Anlama Gelir?                               | https://www.bidolubaski.com/blog/lorem-ipsum-nedir-ve-ne-anlama-gelir                                                  | "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis ...         |
| Lorem İpsum Dolor Sit Amet - Taha Akkurt                            | https://akkurttaha.blogspot.com/2019/07/lorem-ipsum-dolor-sit-amet.html                                                | 9 Tem 2019 · Lorem ipsum dolor sit amet… Hiç bu şekilde devam eden bir yazıyla karşılaştınız mı? Örneğin MS Office Word yardımında ya da hazır temalara ...             |
| Lorem Ipsum - Vikipedi                                              | https://tr.wikipedia.org/wiki/Lorem_Ipsum                                                                              | Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis ...          |
| Lorem Ipsum Dolor Sit Amet - Uçak Tekstil                           | https://ucaktekstil.com.tr/lorem-ipsum-dolor-sit-amet-5/                                                               | Lorem Ipsum Dolor Sit Amet. Yaygın inancın tersine, Lorem Ipsum rastgele sözcüklerden oluşmaz. Kökleri M.Ö. 45 tarihinden bu yana klasik Latin edebiyatına ...          |
| lorem ipsum dolor sit amet - uludağ sözlük                          | https://www.uludagsozluk.com/k/lorem-ipsum-dolor-sit-amet/                                                             | Lorem Ipsum, 500 yıl boyunca varlığını sürdürmekle kalmamış ve günümüzde elektronik yazı tipinin gerektiği birçok konuda hazır bir araç olarak kullanılmaya ...         |
| Lorem Ipsum: Anlıyorum ama konuşamıyorum! - Kampüs Haberleri        | https://www.hurriyet.com.tr/kampus/lorem-ipsum-anliyorum-ama-konusamiyorum-40364027                                    | 13 Şub 2017 · Soner Sezer Lorem Ipsum meselesini sizin için yazdı. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci ...            |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

print(google.anahtarlar)
"""
kullanılan anahtar listesini döndürür.

['baslik', 'link', 'aciklama']
"""