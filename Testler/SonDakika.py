from KekikSpatula import SonDakika

def test_haber():
  haber = SonDakika()

  print(haber.veri)
  """
  json verisi döndürür

  {'kaynak': 'ntv.com.tr', 'veri': [{'haber': "İçişleri'nden yeni genelge: 4 gün boyunca kalabalık yerlerde yoğun denetim", 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberiicisleri-ulke-genelinde-4-gun-boyunca-kalabalik-yerlerde-yogun-denetim-yapilacak,z8vwsAfBdkakGNvtbIJLwQ'}, {'haber': 'Diego Maradona hayatını kaybetti (Maradona kimdir?)', 'link': 'https://www.ntv.com.tr/dunya/son-dakika-haberidiego-maradona-hayatini-kaybetti-maradona-kimdir,1CsehZzHKkGIS84LBNsPDA'}, {'haber': '25 Kasım\xa02020 corona virüs tablosu: 168 can kaybı, 6 bin 814 yeni hasta', 'link': 'https://www.ntv.com.tr/turkiye/25-kasim2020-corona-virus-tablosu-168-can-kaybi-6-bin-814-yeni-hasta,wyeY4Rmd00OvfaTiLlsAFA'}, {'haber': 'Sağlık Bakanı Koca: Son 24 saatte 28 bin 351 yeni vaka var', 'link': 'https://www.ntv.com.tr/turkiye/saglik-bakani-koca-son-24-saatte-28-bin-351-yeni-vaka-var,Kwf_bmijG0au0EnnOiXO0g'}, {'haber': 'MGK bildirisinde İrini vurgusu: Gerekli adımlar atılacak', 'link': 'https://www.ntv.com.tr/turkiye/mgk-bildirisinde-irini-vurgusu-gerekli-adimlar-atilacak,JvL5S2tlCUSjVlhH_vILdw'}, {'haber': 'Dolar kuru bugün ne kadar? (25 Kasım 2020 dolar - euro fiyatları)', 'link': 'https://www.ntv.com.tr/ekonomi/dolar-kuru-bugun-ne-kadar-25-kasim-2020-dolar-euro-fiyatlari,r4Gcb2_Ku0ixm-GtiJHTdg'}, {'haber': 'Benzine 37 kuruş zam', 'link': 'https://www.ntv.com.tr/ekonomi/son-dakika-haberi-benzine-37-kurus-zam,17pS62pqYECZ4eMJxOq_3Q'}, {'haber': 'Cumhurbaşkanı Erdoğan: Corona virüs bize bir kez daha aynı gemide oılduğumuzu hatırlattı', 'link': 'https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogan-corona-virus-bize-bir-kez-daha-ayni-gemide-oildugumuzu-hatirlatti,yV7b1WJUZk-cHT_6gYL75A'}, {'haber': "CHP'den İYİ Parti'ye ziyaret", 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-chpden-iyi-partiye-ziyaret,IiK2P410UEiK1ukdihjLVQ'}, {'haber': 'Fenerbahçe-Beşiktaş derbisinin hakemi belli oldu', 'link': 'https://www.ntv.com.tr/spor/son-dakika-fenerbahce-besiktas-derbisinin-hakemi-belli-oldu,qaWn4yc2Ykqeyw757jv9YA'}, {'haber': 'Bakan Koca duyurdu: İlk yerli tetanos-difteri aşısı kullanıma hazır', 'link': 'https://www.ntv.com.tr/saglik/bakan-koca-duyurdu-ilk-yerli-tetanos-difteri-asisi-kullanima-hazir,FdkDyG6H_kC3PqZ1l0EJRA'}, {'haber': 'Danıştay saldırısı cezasına onama', 'link': 'https://www.ntv.com.tr/turkiye/danistay-saldirisi-cezasina-onama,k_NMYYvmnUS79tSjIcG7Jw'}, {'haber': 'Saldırı girişiminde bulunan 17 terörist etkisiz hale getirildi', 'link': 'https://www.ntv.com.tr/turkiye/saldiri-girisiminde-bulunan-17-terorist-etkisiz-hale-getirildi,8sHU-6CJt02PIYeSOPQkPQ'}, {'haber': 'Altın fiyatları ne kadar?\xa0(25 Kasım 2020 gram ve çeyrek altın fiyatları)', 'link': 'https://www.ntv.com.tr/ekonomi/altin-fiyatlari-ne-kadar25-kasim-2020-gram-ve-ceyrek-altin-fiyatlari,2U_I-WElKk6Dtx8YpUOT3w'}, {'haber': 'Koronavirüs Bilim Kurulu bugün toplanıyor', 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-corona-virus-bilim-kurulu-bugun-toplaniyor,Tr-OvR5xtUmcFF5W8nGHxw'}, {'haber': 'SON DAKİKA:\xa0Medipol Başakşehir, Manchester United karşısında tutunamadı', 'link': 'https://www.ntv.com.tr/spor/son-dakika-medipol-basaksehir-manchester-united-deplasmaninda-4-1-kaybetti,3gUZoDnjv0agT0oTF0-_-Q'}, {'haber': "Azerbaycan ordusu 27 yıldır işgal altında bulunan Kelbecer'e girdi", 'link': 'https://www.ntv.com.tr/dunya/son-dakika-haberiazerbaycan-ordusu-27-yildir-isgal-altinda-bulunan-kelbecere-girdi,l0NkonPATUuHm5iT9rcyJA'}, {'haber': "Dışişleri'nden Yunanistan Dışişleri Bakanı Dendias'a tepki", 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-disislerinden-yunanistan-disisleri-bakaninin-turkiye-aciklamasina-tepki,KC-CJijVxUWAAnp1VVVFJg'}, {'haber': 'Cumhurbaşkanı Erdoğan, Rusya\xa0Lideri Putin ile telefonda\xa0Dağlık Karabağ ve ikili ilişkileri konuştu', 'link': 'https://www.ntv.com.tr/dunya/cumhurbaskani-erdogan-rusyalideri-putin-ile-telefondadaglik-karabag-ve-ikili-iliskileri-konustu,1Z6yzNEFbEGK6Yp1QUOlgA'}, {'haber': 'Hakim ve savcıların terfi sonuçları ilan edildi', 'link': 'https://www.ntv.com.tr/turkiye/hakim-ve-savcilarin-terfi-sonuclari-ilan-edildi,yo1_Y8J35keV0vOYuDdsTA'}, {'haber': 'Bakan Çavuşoğlu: Cevabımızı sahada da vereceğiz (Türk gemisine hukuksuz baskın)', 'link': 'https://www.ntv.com.tr/turkiye/bakan-cavusoglu-cevabimizi-sahada-da-verecegiz-turk-gemisine-hukuksuz-baskin,G9mv1VQ0qEWdwyEhgCzDzg'}, {'haber': '24\xa0Kasım 2020 corona virüs tablosu: 161 can kaybı, 7 bin 381 yeni hasta', 'link': 'https://www.ntv.com.tr/turkiye/24kasim-2020-corona-virus-tablosu-161-can-kaybi-7-bin-381-yeni-hasta,uCrrixb0A0WzQLSqqQJXSA'}, {'haber': 'Eski Diyarbakır milletvekili İhsan Arslan disipline sevk edildi', 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberieski-diyarbakir-milletvekili-ihsan-arslan-disipline-sevk-edildi,UiRm5H7TgEKxU_gQWO3okw'}, {'haber': "Çelik: Bülent Arınç'ın değerlendirmelerine MYK da katılmıyor", 'link': 'https://www.ntv.com.tr/turkiye/celik-bulent-arincin-degerlendirmelerine-myk-da-katilmiyor,ESmJFDJl5UqlVEisVxkOLw'}, {'haber': 'Dolar bugün kaç TL? (24 Kasım 2020 dolar - euro fiyatları)', 'link': 'https://www.ntv.com.tr/ekonomi/dolar-bugun-kac-tl-24-kasim-2020-dolar-euro-fiyatlari,vsS1YmGBPUO8F8BLZrjMqQ'}, {'haber': 'Lozan vurgulu üç yeni NAVTEX', 'link': 'https://www.ntv.com.tr/turkiye/lozan-vurgulu-uc-yeni-navtex,uppsWgGFakCgRUwZNgOgmw'}, {'haber': 'Bülent Arınç istifa etti', 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-bulent-arinc-istifa-etti,Gd4wM5qP5k-R_8tm2MEh3A'}, {'haber': "Bakan Akar'dan Türk gemisinde hukuk dışı aramaya tepki", 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-akardan-turk-gemisinde-hukuk-disi-aramaya-tepki,_y8ts_mU60SQZrF-uG5fKw'}, {'haber': "Kılıçdaroğlu'ndan Almanya'nın Türk gemisini aramasına tepki", 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-kilicdaroglundan-almanyanin-turk-gemisini-aramasina-tepki,2AraEvriRE23AOQW5ZlY3w'}, {'haber': "Rusya'nın geliştirdiği Sputnik V aşısının fiyatı belli oldu", 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-rusyanin-gelistirdigi-sputnik-v-asisinin-fiyati-belli-oldu,kN9EKmFPKkaaSuVaPjDeIQ'}, {'haber': 'Gram altın kaç TL oldu? 24 Kasım 2020 güncel çeyrek ve gram altın fiyatları', 'link': 'https://www.ntv.com.tr/ekonomi/gram-altin-kac-tl-oldu-24-kasim-2020-guncel-ceyrek-ve-gram-altin-fiyatlari,lynYY6sYFk-INYGy7Ae1ZQ'}, {'haber': 'Menemen Belediye Başkanı Serdar Aksoy tutuklandı', 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-menemen-belediye-baskani-serdar-aksoy-tutuklandi,I7k7MJT2akCLJtesP0Z3Hw'}, {'haber': "BDDK'dan normalleşme adımı:\xa0Aktif rasyosu uygulaması kaldırıldı", 'link': 'https://www.ntv.com.tr/ekonomi/son-dakika-haberibddkdan-normallesme-adimi,sdVJJS9spk6Trk09Ureg6Q'}, {'haber': "MİT'ten Irak-Suriye terör hattına darbe", 'link': 'https://www.ntv.com.tr/turkiye/mitten-irak-suriye-teror-hattina-darbe,mkDd3DNkMUecOgqCy3SbRA'}, {'haber': 'SON DAKİKA:\xa0Elazığ’da 3.2 büyüklüğünde deprem', 'link': 'https://www.ntv.com.tr/turkiye/son-dakikaelazigda-3-2-buyuklugunde-deprem-son-depremler,y3-_x_eU8ESnYUD23liE2Q'}, {'haber': 'Kamuyu zarara uğratan 70 kişi için gözaltı kararı', 'link': 'https://www.ntv.com.tr/turkiye/kamuyu-zarara-ugratan-70-kisi-icin-gozalti-karari,IRodu0KIWU-pgF_pvQfxYw'}]}
  """

  for urun in haber.nesne:
    print(urun.haber)
  """
  json verisini python nesnesine dönüştürür.

  İçişleri'nden yeni genelge: 4 gün boyunca kalabalık yerlerde yoğun denetim
  Diego Maradona hayatını kaybetti (Maradona kimdir?)
  25 Kasım 2020 corona virüs tablosu: 168 can kaybı, 6 bin 814 yeni hasta
  Sağlık Bakanı Koca: Son 24 saatte 28 bin 351 yeni vaka var
  MGK bildirisinde İrini vurgusu: Gerekli adımlar atılacak
  Dolar kuru bugün ne kadar? (25 Kasım 2020 dolar - euro fiyatları)
  Benzine 37 kuruş zam
  Cumhurbaşkanı Erdoğan: Corona virüs bize bir kez daha aynı gemide oılduğumuzu hatırlattı
  CHP'den İYİ Parti'ye ziyaret
  Fenerbahçe-Beşiktaş derbisinin hakemi belli oldu
  Bakan Koca duyurdu: İlk yerli tetanos-difteri aşısı kullanıma hazır
  Danıştay saldırısı cezasına onama
  Saldırı girişiminde bulunan 17 terörist etkisiz hale getirildi
  Altın fiyatları ne kadar? (25 Kasım 2020 gram ve çeyrek altın fiyatları)
  Koronavirüs Bilim Kurulu bugün toplanıyor
  SON DAKİKA: Medipol Başakşehir, Manchester United karşısında tutunamadı
  Azerbaycan ordusu 27 yıldır işgal altında bulunan Kelbecer'e girdi
  Dışişleri'nden Yunanistan Dışişleri Bakanı Dendias'a tepki
  Cumhurbaşkanı Erdoğan, Rusya Lideri Putin ile telefonda Dağlık Karabağ ve ikili ilişkileri konuştu
  Hakim ve savcıların terfi sonuçları ilan edildi
  Bakan Çavuşoğlu: Cevabımızı sahada da vereceğiz (Türk gemisine hukuksuz baskın)
  24 Kasım 2020 corona virüs tablosu: 161 can kaybı, 7 bin 381 yeni hasta
  Eski Diyarbakır milletvekili İhsan Arslan disipline sevk edildi
  Çelik: Bülent Arınç'ın değerlendirmelerine MYK da katılmıyor
  Dolar bugün kaç TL? (24 Kasım 2020 dolar - euro fiyatları)
  Lozan vurgulu üç yeni NAVTEX
  Bülent Arınç istifa etti
  Bakan Akar'dan Türk gemisinde hukuk dışı aramaya tepki
  Kılıçdaroğlu'ndan Almanya'nın Türk gemisini aramasına tepki
  Rusya'nın geliştirdiği Sputnik V aşısının fiyatı belli oldu
  Gram altın kaç TL oldu? 24 Kasım 2020 güncel çeyrek ve gram altın fiyatları
  Menemen Belediye Başkanı Serdar Aksoy tutuklandı
  BDDK'dan normalleşme adımı: Aktif rasyosu uygulaması kaldırıldı
  MİT'ten Irak-Suriye terör hattına darbe
  SON DAKİKA: Elazığ’da 3.2 büyüklüğünde deprem
  Kamuyu zarara uğratan 70 kişi için gözaltı kararı
  """


  print(haber.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

  {
    "kaynak": "ntv.com.tr",
    "veri": [
      {
        "haber": "İçişleri'nden yeni genelge: 4 gün boyunca kalabalık yerlerde yoğun denetim",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberiicisleri-ulke-genelinde-4-gun-boyunca-kalabalik-yerlerde-yogun-denetim-yapilacak,z8vwsAfBdkakGNvtbIJLwQ"
      },
      {
        "haber": "Diego Maradona hayatını kaybetti (Maradona kimdir?)",
        "link": "https://www.ntv.com.tr/dunya/son-dakika-haberidiego-maradona-hayatini-kaybetti-maradona-kimdir,1CsehZzHKkGIS84LBNsPDA"
      },
      {
        "haber": "25 Kasım 2020 corona virüs tablosu: 168 can kaybı, 6 bin 814 yeni hasta",
        "link": "https://www.ntv.com.tr/turkiye/25-kasim2020-corona-virus-tablosu-168-can-kaybi-6-bin-814-yeni-hasta,wyeY4Rmd00OvfaTiLlsAFA"
      },
      {
        "haber": "Sağlık Bakanı Koca: Son 24 saatte 28 bin 351 yeni vaka var",
        "link": "https://www.ntv.com.tr/turkiye/saglik-bakani-koca-son-24-saatte-28-bin-351-yeni-vaka-var,Kwf_bmijG0au0EnnOiXO0g"
      },
      {
        "haber": "MGK bildirisinde İrini vurgusu: Gerekli adımlar atılacak",
        "link": "https://www.ntv.com.tr/turkiye/mgk-bildirisinde-irini-vurgusu-gerekli-adimlar-atilacak,JvL5S2tlCUSjVlhH_vILdw"
      },
      {
        "haber": "Dolar kuru bugün ne kadar? (25 Kasım 2020 dolar - euro fiyatları)",
        "link": "https://www.ntv.com.tr/ekonomi/dolar-kuru-bugun-ne-kadar-25-kasim-2020-dolar-euro-fiyatlari,r4Gcb2_Ku0ixm-GtiJHTdg"
      },
      {
        "haber": "Benzine 37 kuruş zam",
        "link": "https://www.ntv.com.tr/ekonomi/son-dakika-haberi-benzine-37-kurus-zam,17pS62pqYECZ4eMJxOq_3Q"
      },
      {
        "haber": "Cumhurbaşkanı Erdoğan: Corona virüs bize bir kez daha aynı gemide oılduğumuzu hatırlattı",
        "link": "https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogan-corona-virus-bize-bir-kez-daha-ayni-gemide-oildugumuzu-hatirlatti,yV7b1WJUZk-cHT_6gYL75A"
      },
      {
        "haber": "CHP'den İYİ Parti'ye ziyaret",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-chpden-iyi-partiye-ziyaret,IiK2P410UEiK1ukdihjLVQ"
      },
      {
        "haber": "Fenerbahçe-Beşiktaş derbisinin hakemi belli oldu",
        "link": "https://www.ntv.com.tr/spor/son-dakika-fenerbahce-besiktas-derbisinin-hakemi-belli-oldu,qaWn4yc2Ykqeyw757jv9YA"
      },
      {
        "haber": "Bakan Koca duyurdu: İlk yerli tetanos-difteri aşısı kullanıma hazır",
        "link": "https://www.ntv.com.tr/saglik/bakan-koca-duyurdu-ilk-yerli-tetanos-difteri-asisi-kullanima-hazir,FdkDyG6H_kC3PqZ1l0EJRA"
      },
      {
        "haber": "Danıştay saldırısı cezasına onama",
        "link": "https://www.ntv.com.tr/turkiye/danistay-saldirisi-cezasina-onama,k_NMYYvmnUS79tSjIcG7Jw"
      },
      {
        "haber": "Saldırı girişiminde bulunan 17 terörist etkisiz hale getirildi",
        "link": "https://www.ntv.com.tr/turkiye/saldiri-girisiminde-bulunan-17-terorist-etkisiz-hale-getirildi,8sHU-6CJt02PIYeSOPQkPQ"
      },
      {
        "haber": "Altın fiyatları ne kadar? (25 Kasım 2020 gram ve çeyrek altın fiyatları)",
        "link": "https://www.ntv.com.tr/ekonomi/altin-fiyatlari-ne-kadar25-kasim-2020-gram-ve-ceyrek-altin-fiyatlari,2U_I-WElKk6Dtx8YpUOT3w"
      },
      {
        "haber": "Koronavirüs Bilim Kurulu bugün toplanıyor",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-corona-virus-bilim-kurulu-bugun-toplaniyor,Tr-OvR5xtUmcFF5W8nGHxw"
      },
      {
        "haber": "SON DAKİKA: Medipol Başakşehir, Manchester United karşısında tutunamadı",
        "link": "https://www.ntv.com.tr/spor/son-dakika-medipol-basaksehir-manchester-united-deplasmaninda-4-1-kaybetti,3gUZoDnjv0agT0oTF0-_-Q"
      },
      {
        "haber": "Azerbaycan ordusu 27 yıldır işgal altında bulunan Kelbecer'e girdi",
        "link": "https://www.ntv.com.tr/dunya/son-dakika-haberiazerbaycan-ordusu-27-yildir-isgal-altinda-bulunan-kelbecere-girdi,l0NkonPATUuHm5iT9rcyJA"
      },
      {
        "haber": "Dışişleri'nden Yunanistan Dışişleri Bakanı Dendias'a tepki",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-disislerinden-yunanistan-disisleri-bakaninin-turkiye-aciklamasina-tepki,KC-CJijVxUWAAnp1VVVFJg"
      },
      {
        "haber": "Cumhurbaşkanı Erdoğan, Rusya Lideri Putin ile telefonda Dağlık Karabağ ve ikili ilişkileri konuştu",
        "link": "https://www.ntv.com.tr/dunya/cumhurbaskani-erdogan-rusyalideri-putin-ile-telefondadaglik-karabag-ve-ikili-iliskileri-konustu,1Z6yzNEFbEGK6Yp1QUOlgA"
      },
      {
        "haber": "Hakim ve savcıların terfi sonuçları ilan edildi",
        "link": "https://www.ntv.com.tr/turkiye/hakim-ve-savcilarin-terfi-sonuclari-ilan-edildi,yo1_Y8J35keV0vOYuDdsTA"
      },
      {
        "haber": "Bakan Çavuşoğlu: Cevabımızı sahada da vereceğiz (Türk gemisine hukuksuz baskın)",
        "link": "https://www.ntv.com.tr/turkiye/bakan-cavusoglu-cevabimizi-sahada-da-verecegiz-turk-gemisine-hukuksuz-baskin,G9mv1VQ0qEWdwyEhgCzDzg"
      },
      {
        "haber": "24 Kasım 2020 corona virüs tablosu: 161 can kaybı, 7 bin 381 yeni hasta",
        "link": "https://www.ntv.com.tr/turkiye/24kasim-2020-corona-virus-tablosu-161-can-kaybi-7-bin-381-yeni-hasta,uCrrixb0A0WzQLSqqQJXSA"
      },
      {
        "haber": "Eski Diyarbakır milletvekili İhsan Arslan disipline sevk edildi",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberieski-diyarbakir-milletvekili-ihsan-arslan-disipline-sevk-edildi,UiRm5H7TgEKxU_gQWO3okw"
      },
      {
        "haber": "Çelik: Bülent Arınç'ın değerlendirmelerine MYK da katılmıyor",
        "link": "https://www.ntv.com.tr/turkiye/celik-bulent-arincin-degerlendirmelerine-myk-da-katilmiyor,ESmJFDJl5UqlVEisVxkOLw"
      },
      {
        "haber": "Dolar bugün kaç TL? (24 Kasım 2020 dolar - euro fiyatları)",
        "link": "https://www.ntv.com.tr/ekonomi/dolar-bugun-kac-tl-24-kasim-2020-dolar-euro-fiyatlari,vsS1YmGBPUO8F8BLZrjMqQ"
      },
      {
        "haber": "Lozan vurgulu üç yeni NAVTEX",
        "link": "https://www.ntv.com.tr/turkiye/lozan-vurgulu-uc-yeni-navtex,uppsWgGFakCgRUwZNgOgmw"
      },
      {
        "haber": "Bülent Arınç istifa etti",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-bulent-arinc-istifa-etti,Gd4wM5qP5k-R_8tm2MEh3A"
      },
      {
        "haber": "Bakan Akar'dan Türk gemisinde hukuk dışı aramaya tepki",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-akardan-turk-gemisinde-hukuk-disi-aramaya-tepki,_y8ts_mU60SQZrF-uG5fKw"
      },
      {
        "haber": "Kılıçdaroğlu'ndan Almanya'nın Türk gemisini aramasına tepki",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-kilicdaroglundan-almanyanin-turk-gemisini-aramasina-tepki,2AraEvriRE23AOQW5ZlY3w"
      },
      {
        "haber": "Rusya'nın geliştirdiği Sputnik V aşısının fiyatı belli oldu",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-rusyanin-gelistirdigi-sputnik-v-asisinin-fiyati-belli-oldu,kN9EKmFPKkaaSuVaPjDeIQ"
      },
      {
        "haber": "Gram altın kaç TL oldu? 24 Kasım 2020 güncel çeyrek ve gram altın fiyatları",
        "link": "https://www.ntv.com.tr/ekonomi/gram-altin-kac-tl-oldu-24-kasim-2020-guncel-ceyrek-ve-gram-altin-fiyatlari,lynYY6sYFk-INYGy7Ae1ZQ"
      },
      {
        "haber": "Menemen Belediye Başkanı Serdar Aksoy tutuklandı",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-menemen-belediye-baskani-serdar-aksoy-tutuklandi,I7k7MJT2akCLJtesP0Z3Hw"
      },
      {
        "haber": "BDDK'dan normalleşme adımı: Aktif rasyosu uygulaması kaldırıldı",
        "link": "https://www.ntv.com.tr/ekonomi/son-dakika-haberibddkdan-normallesme-adimi,sdVJJS9spk6Trk09Ureg6Q"
      },
      {
        "haber": "MİT'ten Irak-Suriye terör hattına darbe",
        "link": "https://www.ntv.com.tr/turkiye/mitten-irak-suriye-teror-hattina-darbe,mkDd3DNkMUecOgqCy3SbRA"
      },
      {
        "haber": "SON DAKİKA: Elazığ’da 3.2 büyüklüğünde deprem",
        "link": "https://www.ntv.com.tr/turkiye/son-dakikaelazigda-3-2-buyuklugunde-deprem-son-depremler,y3-_x_eU8ESnYUD23liE2Q"
      },
      {
        "haber": "Kamuyu zarara uğratan 70 kişi için gözaltı kararı",
        "link": "https://www.ntv.com.tr/turkiye/kamuyu-zarara-ugratan-70-kisi-icin-gozalti-karari,IRodu0KIWU-pgF_pvQfxYw"
      }
    ]
  }
  """

  print(haber.tablo())
  """
  tabulate verisi döndürür.

  +----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
  | haber                                                                                              | link                                                                                                                                                    |
  |----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------|
  | İçişleri'nden yeni genelge: 4 gün boyunca kalabalık yerlerde yoğun denetim                         | https://www.ntv.com.tr/turkiye/son-dakika-haberiicisleri-ulke-genelinde-4-gun-boyunca-kalabalik-yerlerde-yogun-denetim-yapilacak,z8vwsAfBdkakGNvtbIJLwQ |
  | Diego Maradona hayatını kaybetti (Maradona kimdir?)                                                | https://www.ntv.com.tr/dunya/son-dakika-haberidiego-maradona-hayatini-kaybetti-maradona-kimdir,1CsehZzHKkGIS84LBNsPDA                                   |
  | 25 Kasım 2020 corona virüs tablosu: 168 can kaybı, 6 bin 814 yeni hasta                            | https://www.ntv.com.tr/turkiye/25-kasim2020-corona-virus-tablosu-168-can-kaybi-6-bin-814-yeni-hasta,wyeY4Rmd00OvfaTiLlsAFA                              |
  | Sağlık Bakanı Koca: Son 24 saatte 28 bin 351 yeni vaka var                                         | https://www.ntv.com.tr/turkiye/saglik-bakani-koca-son-24-saatte-28-bin-351-yeni-vaka-var,Kwf_bmijG0au0EnnOiXO0g                                         |
  | MGK bildirisinde İrini vurgusu: Gerekli adımlar atılacak                                           | https://www.ntv.com.tr/turkiye/mgk-bildirisinde-irini-vurgusu-gerekli-adimlar-atilacak,JvL5S2tlCUSjVlhH_vILdw                                           |
  | Dolar kuru bugün ne kadar? (25 Kasım 2020 dolar - euro fiyatları)                                  | https://www.ntv.com.tr/ekonomi/dolar-kuru-bugun-ne-kadar-25-kasim-2020-dolar-euro-fiyatlari,r4Gcb2_Ku0ixm-GtiJHTdg                                      |
  | Benzine 37 kuruş zam                                                                               | https://www.ntv.com.tr/ekonomi/son-dakika-haberi-benzine-37-kurus-zam,17pS62pqYECZ4eMJxOq_3Q                                                            |
  | Cumhurbaşkanı Erdoğan: Corona virüs bize bir kez daha aynı gemide oılduğumuzu hatırlattı           | https://www.ntv.com.tr/turkiye/cumhurbaskani-erdogan-corona-virus-bize-bir-kez-daha-ayni-gemide-oildugumuzu-hatirlatti,yV7b1WJUZk-cHT_6gYL75A           |
  | CHP'den İYİ Parti'ye ziyaret                                                                       | https://www.ntv.com.tr/turkiye/son-dakika-haberi-chpden-iyi-partiye-ziyaret,IiK2P410UEiK1ukdihjLVQ                                                      |
  | Fenerbahçe-Beşiktaş derbisinin hakemi belli oldu                                                   | https://www.ntv.com.tr/spor/son-dakika-fenerbahce-besiktas-derbisinin-hakemi-belli-oldu,qaWn4yc2Ykqeyw757jv9YA                                          |
  | Bakan Koca duyurdu: İlk yerli tetanos-difteri aşısı kullanıma hazır                                | https://www.ntv.com.tr/saglik/bakan-koca-duyurdu-ilk-yerli-tetanos-difteri-asisi-kullanima-hazir,FdkDyG6H_kC3PqZ1l0EJRA                                 |
  | Danıştay saldırısı cezasına onama                                                                  | https://www.ntv.com.tr/turkiye/danistay-saldirisi-cezasina-onama,k_NMYYvmnUS79tSjIcG7Jw                                                                 |
  | Saldırı girişiminde bulunan 17 terörist etkisiz hale getirildi                                     | https://www.ntv.com.tr/turkiye/saldiri-girisiminde-bulunan-17-terorist-etkisiz-hale-getirildi,8sHU-6CJt02PIYeSOPQkPQ                                    |
  | Altın fiyatları ne kadar? (25 Kasım 2020 gram ve çeyrek altın fiyatları)                           | https://www.ntv.com.tr/ekonomi/altin-fiyatlari-ne-kadar25-kasim-2020-gram-ve-ceyrek-altin-fiyatlari,2U_I-WElKk6Dtx8YpUOT3w                              |
  | Koronavirüs Bilim Kurulu bugün toplanıyor                                                          | https://www.ntv.com.tr/turkiye/son-dakika-haberi-corona-virus-bilim-kurulu-bugun-toplaniyor,Tr-OvR5xtUmcFF5W8nGHxw                                      |
  | SON DAKİKA: Medipol Başakşehir, Manchester United karşısında tutunamadı                            | https://www.ntv.com.tr/spor/son-dakika-medipol-basaksehir-manchester-united-deplasmaninda-4-1-kaybetti,3gUZoDnjv0agT0oTF0-_-Q                           |
  | Azerbaycan ordusu 27 yıldır işgal altında bulunan Kelbecer'e girdi                                 | https://www.ntv.com.tr/dunya/son-dakika-haberiazerbaycan-ordusu-27-yildir-isgal-altinda-bulunan-kelbecere-girdi,l0NkonPATUuHm5iT9rcyJA                  |
  | Dışişleri'nden Yunanistan Dışişleri Bakanı Dendias'a tepki                                         | https://www.ntv.com.tr/turkiye/son-dakika-haberi-disislerinden-yunanistan-disisleri-bakaninin-turkiye-aciklamasina-tepki,KC-CJijVxUWAAnp1VVVFJg         |
  | Cumhurbaşkanı Erdoğan, Rusya Lideri Putin ile telefonda Dağlık Karabağ ve ikili ilişkileri konuştu | https://www.ntv.com.tr/dunya/cumhurbaskani-erdogan-rusyalideri-putin-ile-telefondadaglik-karabag-ve-ikili-iliskileri-konustu,1Z6yzNEFbEGK6Yp1QUOlgA     |
  | Hakim ve savcıların terfi sonuçları ilan edildi                                                    | https://www.ntv.com.tr/turkiye/hakim-ve-savcilarin-terfi-sonuclari-ilan-edildi,yo1_Y8J35keV0vOYuDdsTA                                                   |
  | Bakan Çavuşoğlu: Cevabımızı sahada da vereceğiz (Türk gemisine hukuksuz baskın)                    | https://www.ntv.com.tr/turkiye/bakan-cavusoglu-cevabimizi-sahada-da-verecegiz-turk-gemisine-hukuksuz-baskin,G9mv1VQ0qEWdwyEhgCzDzg                      |
  | 24 Kasım 2020 corona virüs tablosu: 161 can kaybı, 7 bin 381 yeni hasta                            | https://www.ntv.com.tr/turkiye/24kasim-2020-corona-virus-tablosu-161-can-kaybi-7-bin-381-yeni-hasta,uCrrixb0A0WzQLSqqQJXSA                              |
  | Eski Diyarbakır milletvekili İhsan Arslan disipline sevk edildi                                    | https://www.ntv.com.tr/turkiye/son-dakika-haberieski-diyarbakir-milletvekili-ihsan-arslan-disipline-sevk-edildi,UiRm5H7TgEKxU_gQWO3okw                  |
  | Çelik: Bülent Arınç'ın değerlendirmelerine MYK da katılmıyor                                       | https://www.ntv.com.tr/turkiye/celik-bulent-arincin-degerlendirmelerine-myk-da-katilmiyor,ESmJFDJl5UqlVEisVxkOLw                                        |
  | Dolar bugün kaç TL? (24 Kasım 2020 dolar - euro fiyatları)                                         | https://www.ntv.com.tr/ekonomi/dolar-bugun-kac-tl-24-kasim-2020-dolar-euro-fiyatlari,vsS1YmGBPUO8F8BLZrjMqQ                                             |
  | Lozan vurgulu üç yeni NAVTEX                                                                       | https://www.ntv.com.tr/turkiye/lozan-vurgulu-uc-yeni-navtex,uppsWgGFakCgRUwZNgOgmw                                                                      |
  | Bülent Arınç istifa etti                                                                           | https://www.ntv.com.tr/turkiye/son-dakika-bulent-arinc-istifa-etti,Gd4wM5qP5k-R_8tm2MEh3A                                                               |
  | Bakan Akar'dan Türk gemisinde hukuk dışı aramaya tepki                                             | https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-akardan-turk-gemisinde-hukuk-disi-aramaya-tepki,_y8ts_mU60SQZrF-uG5fKw                           |
  | Kılıçdaroğlu'ndan Almanya'nın Türk gemisini aramasına tepki                                        | https://www.ntv.com.tr/turkiye/son-dakika-haberi-kilicdaroglundan-almanyanin-turk-gemisini-aramasina-tepki,2AraEvriRE23AOQW5ZlY3w                       |
  | Rusya'nın geliştirdiği Sputnik V aşısının fiyatı belli oldu                                        | https://www.ntv.com.tr/turkiye/son-dakika-haberi-rusyanin-gelistirdigi-sputnik-v-asisinin-fiyati-belli-oldu,kN9EKmFPKkaaSuVaPjDeIQ                      |
  | Gram altın kaç TL oldu? 24 Kasım 2020 güncel çeyrek ve gram altın fiyatları                        | https://www.ntv.com.tr/ekonomi/gram-altin-kac-tl-oldu-24-kasim-2020-guncel-ceyrek-ve-gram-altin-fiyatlari,lynYY6sYFk-INYGy7Ae1ZQ                        |
  | Menemen Belediye Başkanı Serdar Aksoy tutuklandı                                                   | https://www.ntv.com.tr/turkiye/son-dakika-haberi-menemen-belediye-baskani-serdar-aksoy-tutuklandi,I7k7MJT2akCLJtesP0Z3Hw                                |
  | BDDK'dan normalleşme adımı: Aktif rasyosu uygulaması kaldırıldı                                    | https://www.ntv.com.tr/ekonomi/son-dakika-haberibddkdan-normallesme-adimi,sdVJJS9spk6Trk09Ureg6Q                                                        |
  | MİT'ten Irak-Suriye terör hattına darbe                                                            | https://www.ntv.com.tr/turkiye/mitten-irak-suriye-teror-hattina-darbe,mkDd3DNkMUecOgqCy3SbRA                                                            |
  | SON DAKİKA: Elazığ’da 3.2 büyüklüğünde deprem                                                      | https://www.ntv.com.tr/turkiye/son-dakikaelazigda-3-2-buyuklugunde-deprem-son-depremler,y3-_x_eU8ESnYUD23liE2Q                                          |
  | Kamuyu zarara uğratan 70 kişi için gözaltı kararı                                                  | https://www.ntv.com.tr/turkiye/kamuyu-zarara-ugratan-70-kisi-icin-gozalti-karari,IRodu0KIWU-pgF_pvQfxYw                                                 |
  +----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
  """

  print(haber.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['haber', 'link']
  """