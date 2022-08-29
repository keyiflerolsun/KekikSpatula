from KekikSpatula import SonDakika

def test_haber():
  haber = SonDakika()

  print(haber.veri)
  """
  json verisi döndürür

  {'kaynak': 'ntv.com.tr', 'veri': [{'haber': 'Gülşen tahliye\xa0edildi', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/mV1y00XI3k6dTjjHIA66bA.jpg', 'link': 'https://www.ntv.com.tr/turkiye/gulsen-tahliye-edilecek-mi,wLkIbiBHjUGk5daeJ_CKjg'}, {'haber': 'Ünsal Ban, yurtdışına kaçmaya çalışırken yakalandı', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/kISG5ug900Oni2ItjCAL5Q.jpg', 'link': 'https://www.ntv.com.tr/turkiye/unsal-ban-yurtdisina-kacmaya-calisirken-yakalandi,2NtsNE__B0qPLV91BoEQlg'}, {'haber': 'Temmuz ayı dış ticaret rakamları açıklandı', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/YZuYFxLy7UO8EmB8P74tEQ.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/temmuz-ayi-dis-ticaret-rakamlari-aciklandi,NeL9rRb7pUWPeEa2b5ZKJA'}, {'haber': 'Brent petrol fiyatı ne kadar oldu? (29 Ağustos 2022 petrol fiyatları)', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/d8BP-NRZAES1d6oBMeJkDg.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/brent-petrol-fiyati-ne-kadar-oldu-29-agustos-2022-petrol-fiyatlari,qKus0SOS4UWhWe262Pf4XQ'}, {'haber': 'Dolar kuru bugün ne kadar? (29 Ağustos 2022 dolar - euro fiyatları)', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/TpNCbaSQ5EKpQ_zD2R-0kQ.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/doviz/dolar-kuru-bugun-ne-kadar-29-agustos-2022-dolar-euro-fiyatlari,6V_VbQu9K0WEN1taePB3vA'}, {'haber': 'Çeyrek altın fiyatları bugün ne kadar oldu? 29 Ağustos 2022 güncel altın kuru fiyatları', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/PxLuI33TVkOAYYoc7SSrBg.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/altin/ceyrek-altin-fiyatlari-bugun-ne-kadar-oldu-29-agustos-2022-guncel-altin-kuru-fiyatlari,QQm9QQIO8EuRKX7tpFYBxw'}, {'haber': 'Dev maçta kazanan yok (Trabzonspor-Galatasaray maç sonucu)', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/QwkQnBgU5EKmzZyTspkkZg.jpg', 'link': 'https://www.ntv.com.tr/sporskor/son-dakika-dev-macta-kazanan-yok-trabzonspor-galatasaray-mac-sonucu,S7jr-qNX9EaKn_dxHhXjcw'}, {'haber': "Dünya Kupası Elemeleri:\xa0Milliler Sırbistan'ı geçemedi (Türkiye-Sırbistan maç sonucu)", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/_z3ldT-fzE68VnUScw9b5w.jpg', 'link': 'https://www.ntv.com.tr/sporskor/dunya-kupasi-elemeleri12-dev-adam-sirbistana-79-72-yenildi-turkiye-sirbistan-mac-sonucu,-6buirGsE0SuMzNMA4x59Q'}, {'haber': "S-300'le Türk F-16'larına taciz", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/-vHtB7DKnUmkzMhopDuaLA.jpg', 'link': 'https://www.ntv.com.tr/turkiye/s-300le-turk-f-16larina-taciz,eu-m13ogpk-MsEMpoXiIrw'}, {'haber': 'MSB: Tahıl yüklü 6 gemi daha hareket etti', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/iL-IHFS7O0WJB13tMbasBA.jpg', 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-msb-tahil-yuklu-6-gemi-daha-hareket-etti,-cGlwoX0f0ip1VtuefMVvg'}, {'haber': "SON DAKİKA:\xa0Galatasaray Cicaldau'yu kiraladı", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/S6iVZbIn-0egqoisQVjQRQ.jpg', 'link': 'https://www.ntv.com.tr/sporskor/son-dakikagalatasaray-cicaldauyu-kiraladi,9Rvu4iEwrkmbjfcJS1yfHA'}, {'haber': 'Cumhurbaşkanı Erdoğan Aliyev ile görüştü', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/FNKtCZGKyUu-OhnJYXMiIQ.jpg', 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-aliyev-ile-gorustu,lQMQtnu2PUy-WgfFsSPTvA'}, {'haber': "Bakan Koca'dan sağlık çalışanlarına teşvik açıklaması", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/Mru9VlmtYEaexK7pd84SWA.jpg', 'link': 'https://www.ntv.com.tr/saglik/son-dakika-haberi-bakan-kocadan-saglik-calisanlarina-tesvik-aciklamasi,rMIOV-sAhU-pXk8lgMOlNg'}, {'haber': "Sancaktepe'de komiser yardımcısı başından vurularak öldürüldü", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/fN-pj2A3RESTkA3YMJcAKg.jpg', 'link': 'https://www.ntv.com.tr/turkiye/sancaktepede-komiser-yardimcisi-basindan-vurularak-olduruldu,s6ETIZcjQ0m0nNsKz7QaeA'}, {'haber': 'Ukrayna limanlarından 1 milyon tonun üzerinde tahıl taşındı', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/sWquCtA4SUCsbluQBTIi1Q.jpg', 'link': 'https://www.ntv.com.tr/dunya/ukrayna-limanlarindan-1-milyon-tonun-uzerinde-tahil-tasindi,-ZMOjftVoki_NaObU0uygQ'}, {'haber': 'Eren Abluka-34 operasyonunda 19 roketatar sevk fişeği ve 16 milyon kök kenevir ele geçirildi', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/N7m40jP9Ak60KaKJXLd7yw.jpg', 'link': 'https://www.ntv.com.tr/turkiye/eren-abluka-34-operasyonunda-19-roketatar-sevk-fisegi-ve-16-milyon-kok-kenevir-ele-gecirildi,Xowk9XC1d0SLvn_7_EeaMw'}, {'haber': "Bakan Kurum'dan Kanal İstanbul açıklaması", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/DpgYwR5yk0KyQPq4cKxwJQ.jpg', 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-kurumdan-kanal-istanbul-aciklamasi,HA2fl6Gsh0-7r7-jmOUQiA'}, {'haber': "Dışişleri Bakanlığı'ndan Macron'a tepki", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/pjUgdZKjMkmcCiLJpWN66g.jpg', 'link': 'https://www.ntv.com.tr/dunya/son-dakika-haberi-disisleri-bakanligindan-macrona-tepki,zPzzzm4z2kWrLDIDjJbvOQ'}, {'haber': 'Çanakkale Boğazı girişinde kargo gemisi karaya oturdu', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/whtnTHRYpkmK7kLG75AHNA.jpg', 'link': 'https://www.ntv.com.tr/turkiye/canakkale-bogazi-girisinde-kargo-gemisi-karaya-oturdu,1IGmS04XRUu7_jAaQhvsFw'}, {'haber': 'Ticari mevduatlar da TMSF sigorta kapsamına alındı', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/2d0zqUXVdkOHNjsxNLz8rw.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/son-dakika-haberi-ticari-mevduatlar-da-tmsf-sigorta-kapsamina-alindi,dHdBUVXEeUqe8-U5_z8C0g'}, {'haber': "SON DAKİKA:\xa0Gaziantep FK, Antalyaspor'u farklı mağlup etti", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/f4E9sLGyv06mUSyOawW6eA.jpg', 'link': 'https://www.ntv.com.tr/sporskor/son-dakikagaziantep-fk-antalyasporu-farkli-maglup-etti,taFLMuj260yzqY4UoiF_nQ'}, {'haber': 'Fed Başkanı Powell: Enflasyonla mücadele acı verecek', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/lUjneafw2ESvhkMg3MpPIg.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/fed-baskani-powell-enflasyonla-mucadele-aci-verecek,Ua8_zWpch0mvIHQ-ri2G8A'}, {'haber': "Aliağa'da sökülecek Brezilya gemisinin izni iptal edildi", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/kMp0jTE3Jk2BMSbDQlQ9_g.jpg', 'link': 'https://www.ntv.com.tr/turkiye/aliagada-sokulecek-brezilya-gemisinin-izni-iptal-edildi,yB2NyNUtU0yyRJ8Zqy1srA'}, {'haber': 'Madrid Mutabakatı | İsveç-Finlandiya ile ilk toplantı yapıldı', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/NlNlhhOlDUGGauLJqoC-TA.jpg', 'link': 'https://www.ntv.com.tr/turkiye/madrid-mutabakati-isvec-finlandiya-ile-ilk-toplanti-yapildi,HMP6X6fa2EyVEWrfNuSipA'}, {'haber': "SON DAKİKA:\xa0Başakşehir ve Sivasspor'un Konferans Ligi’ndeki rakipleri belli oldu", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/bAtA2K3NGEefBmQazc3dzA.jpg', 'link': 'https://www.ntv.com.tr/sporskor/son-dakikabasaksehir-ve-sivassporun-konferans-ligindeki-rakipleri-belli-oldu,OqOCDAG1kk283cO-UyVjZg'}, {'haber': 'İcra düzenlemesinde yeni ayrıntılar', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/5oAyDc6khUOCpab0qstT9A.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/icra-duzenlemesinde-yeni-ayrintilar,T1cd-PtYrUuGrIO1HCPrSQ'}, {'haber': 'MHP af taleplerini inceliyor', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/vXF3g-qRvE6yCr9fi-xNfw.jpg', 'link': 'https://www.ntv.com.tr/turkiye/mhp-af-taleplerini-inceliyor,JbtmHHQHd0G5KVXbvmWYhg'}, {'haber': 'Cumhurbaşkanı Erdoğan:\xa0Hiçbir oyuna tahammülümüz yok', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/c_KGYHpGI0-q4VbCRi8lYg.jpg', 'link': 'https://www.ntv.com.tr/turkiye/cumhurbaskani-erdoganhicbir-oyuna-tahammulumuz-yok,SIEFWdffz0-k1b3pqZS4tA'}, {'haber': 'Tarımsal destek ödemeleri başladı', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/ljZcUB6juUW9u_Ift5g7WA.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/tarimsal-destek-odemeleri-basladi,7w28VxmGHUueIzAJiBPNRQ'}, {'haber': "Bakan Nebati'den ABD'nin TÜSİAD mektubuna ilişkin açıklama", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/g3UZhjogFkSBnJcaAy0GPg.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/bakan-nebatiden-abdnin-tusiad-mektubuna-iliskin-aciklama,H-G-0Ifxekm6pizIjwk7pw'}, {'haber': "Dünya'dan 100 ışık yılı uzaklıkta bir 'okyanus gezegeni' keşfedildi", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/iSBQHGmN9kWeMtokdv6Huw.jpg', 'link': 'https://www.ntv.com.tr/dunya/dunyadan-100-isik-yili-uzaklikta-bir-okyanus-gezegeni-kesfedildi,ERrqMyU95ku5-KV8XDqdxg'}, {'haber': 'Çeyrek altın fiyatları bugün ne kadar oldu?\xa026 Ağustos\xa02022 güncel altın kuru fiyatları', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/PxLuI33TVkOAYYoc7SSrBg.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/altin/ceyrek-altin-fiyatlari-bugun-ne-kadar-oldu26-agustos2022-guncel-altin-kuru-fiyatlari,VlM3ud3Sl0qUm0-XH5tQBA'}, {'haber': 'Brent petrol fiyatı ne kadar oldu? (26 Ağustos\xa02022 petrol fiyatları)', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/d8BP-NRZAES1d6oBMeJkDg.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/brent-petrol-fiyati-ne-kadar-oldu-26-agustos2022-petrol-fiyatlari,QH5YSGQBQ0WlFHBgxbmjnA'}, {'haber': 'Dolar kuru bugün ne kadar? (26 Ağustos\xa02022 dolar - euro fiyatları)', 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/TpNCbaSQ5EKpQ_zD2R-0kQ.jpg', 'link': 'https://www.ntv.com.tr/ntvpara/doviz/dolar-kuru-bugun-ne-kadar-26-agustos2022-dolar-euro-fiyatlari,G0HlVAGbGUm_wqexgcJSKQ'}, {'haber': "Fenerbahçe, UEFA Avrupa Ligi'nde gruplara kaldı", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/45wUbqHjj0aPeobrSIWuXg.jpg', 'link': 'https://www.ntv.com.tr/sporskor/son-dakika-fenerbahce-uefa-avrupa-liginde-gruplara-kaldi,GDRNmS35z0SpyLxAhCMc6g'}, {'haber': "Denizli'de yolcu otobüsü devrildi: 28 yaralı", 'gorsel': 'https://cdn1.ntv.com.tr/gorsel/h0up6Z7gi0WIgZYyOXA72g.jpg', 'link': 'https://www.ntv.com.tr/turkiye/son-dakika-haberi-denizlide-yolcu-otobusu-devrildi-28-yarali,n9s87oqJekGwL3QpbPaKDQ'}]}
  """

  for urun in haber.nesne:
    print(urun.haber)
  """
  json verisini python nesnesine dönüştürür.

    Gülşen tahliye edildi
    Ünsal Ban, yurtdışına kaçmaya çalışırken yakalandı
    Temmuz ayı dış ticaret rakamları açıklandı
    Brent petrol fiyatı ne kadar oldu? (29 Ağustos 2022 petrol fiyatları)
    Dolar kuru bugün ne kadar? (29 Ağustos 2022 dolar - euro fiyatları)
    Çeyrek altın fiyatları bugün ne kadar oldu? 29 Ağustos 2022 güncel altın kuru fiyatları
    Dev maçta kazanan yok (Trabzonspor-Galatasaray maç sonucu)
    Dünya Kupası Elemeleri: Milliler Sırbistan'ı geçemedi (Türkiye-Sırbistan maç sonucu)
    S-300'le Türk F-16'larına taciz
    MSB: Tahıl yüklü 6 gemi daha hareket etti
    SON DAKİKA: Galatasaray Cicaldau'yu kiraladı
    Cumhurbaşkanı Erdoğan Aliyev ile görüştü
    Bakan Koca'dan sağlık çalışanlarına teşvik açıklaması
    Sancaktepe'de komiser yardımcısı başından vurularak öldürüldü
    Ukrayna limanlarından 1 milyon tonun üzerinde tahıl taşındı
    Eren Abluka-34 operasyonunda 19 roketatar sevk fişeği ve 16 milyon kök kenevir ele geçirildi
    Bakan Kurum'dan Kanal İstanbul açıklaması
    Dışişleri Bakanlığı'ndan Macron'a tepki
    Çanakkale Boğazı girişinde kargo gemisi karaya oturdu
    Ticari mevduatlar da TMSF sigorta kapsamına alındı
    SON DAKİKA: Gaziantep FK, Antalyaspor'u farklı mağlup etti
    Fed Başkanı Powell: Enflasyonla mücadele acı verecek
    Aliağa'da sökülecek Brezilya gemisinin izni iptal edildi
    Madrid Mutabakatı | İsveç-Finlandiya ile ilk toplantı yapıldı
    SON DAKİKA: Başakşehir ve Sivasspor'un Konferans Ligi’ndeki rakipleri belli oldu
    İcra düzenlemesinde yeni ayrıntılar
    MHP af taleplerini inceliyor
    Cumhurbaşkanı Erdoğan: Hiçbir oyuna tahammülümüz yok
    Tarımsal destek ödemeleri başladı
    Bakan Nebati'den ABD'nin TÜSİAD mektubuna ilişkin açıklama
    Dünya'dan 100 ışık yılı uzaklıkta bir 'okyanus gezegeni' keşfedildi
    Çeyrek altın fiyatları bugün ne kadar oldu? 26 Ağustos 2022 güncel altın kuru fiyatları
    Brent petrol fiyatı ne kadar oldu? (26 Ağustos 2022 petrol fiyatları)
    Dolar kuru bugün ne kadar? (26 Ağustos 2022 dolar - euro fiyatları)
    Fenerbahçe, UEFA Avrupa Ligi'nde gruplara kaldı
    Denizli'de yolcu otobüsü devrildi: 28 yaralı
  """


  print(haber.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

    {
    "kaynak": "ntv.com.tr",
    "veri": [
        {
        "haber": "Gülşen tahliye edildi",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/mV1y00XI3k6dTjjHIA66bA.jpg",
        "link": "https://www.ntv.com.tr/turkiye/gulsen-tahliye-edilecek-mi,wLkIbiBHjUGk5daeJ_CKjg"
        },
        {
        "haber": "Ünsal Ban, yurtdışına kaçmaya çalışırken yakalandı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/kISG5ug900Oni2ItjCAL5Q.jpg",
        "link": "https://www.ntv.com.tr/turkiye/unsal-ban-yurtdisina-kacmaya-calisirken-yakalandi,2NtsNE__B0qPLV91BoEQlg"
        },
        {
        "haber": "Temmuz ayı dış ticaret rakamları açıklandı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/YZuYFxLy7UO8EmB8P74tEQ.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/temmuz-ayi-dis-ticaret-rakamlari-aciklandi,NeL9rRb7pUWPeEa2b5ZKJA"
        },
        {
        "haber": "Brent petrol fiyatı ne kadar oldu? (29 Ağustos 2022 petrol fiyatları)",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/d8BP-NRZAES1d6oBMeJkDg.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/brent-petrol-fiyati-ne-kadar-oldu-29-agustos-2022-petrol-fiyatlari,qKus0SOS4UWhWe262Pf4XQ"
        },
        {
        "haber": "Dolar kuru bugün ne kadar? (29 Ağustos 2022 dolar - euro fiyatları)",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/TpNCbaSQ5EKpQ_zD2R-0kQ.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/doviz/dolar-kuru-bugun-ne-kadar-29-agustos-2022-dolar-euro-fiyatlari,6V_VbQu9K0WEN1taePB3vA"
        },
        {
        "haber": "Çeyrek altın fiyatları bugün ne kadar oldu? 29 Ağustos 2022 güncel altın kuru fiyatları",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/PxLuI33TVkOAYYoc7SSrBg.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/altin/ceyrek-altin-fiyatlari-bugun-ne-kadar-oldu-29-agustos-2022-guncel-altin-kuru-fiyatlari,QQm9QQIO8EuRKX7tpFYBxw"
        },
        {
        "haber": "Dev maçta kazanan yok (Trabzonspor-Galatasaray maç sonucu)",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/QwkQnBgU5EKmzZyTspkkZg.jpg",
        "link": "https://www.ntv.com.tr/sporskor/son-dakika-dev-macta-kazanan-yok-trabzonspor-galatasaray-mac-sonucu,S7jr-qNX9EaKn_dxHhXjcw"
        },
        {
        "haber": "Dünya Kupası Elemeleri: Milliler Sırbistan'ı geçemedi (Türkiye-Sırbistan maç sonucu)",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/_z3ldT-fzE68VnUScw9b5w.jpg",
        "link": "https://www.ntv.com.tr/sporskor/dunya-kupasi-elemeleri12-dev-adam-sirbistana-79-72-yenildi-turkiye-sirbistan-mac-sonucu,-6buirGsE0SuMzNMA4x59Q"
        },
        {
        "haber": "S-300'le Türk F-16'larına taciz",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/-vHtB7DKnUmkzMhopDuaLA.jpg",
        "link": "https://www.ntv.com.tr/turkiye/s-300le-turk-f-16larina-taciz,eu-m13ogpk-MsEMpoXiIrw"
        },
        {
        "haber": "MSB: Tahıl yüklü 6 gemi daha hareket etti",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/iL-IHFS7O0WJB13tMbasBA.jpg",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-msb-tahil-yuklu-6-gemi-daha-hareket-etti,-cGlwoX0f0ip1VtuefMVvg"
        },
        {
        "haber": "SON DAKİKA: Galatasaray Cicaldau'yu kiraladı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/S6iVZbIn-0egqoisQVjQRQ.jpg",
        "link": "https://www.ntv.com.tr/sporskor/son-dakikagalatasaray-cicaldauyu-kiraladi,9Rvu4iEwrkmbjfcJS1yfHA"
        },
        {
        "haber": "Cumhurbaşkanı Erdoğan Aliyev ile görüştü",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/FNKtCZGKyUu-OhnJYXMiIQ.jpg",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-aliyev-ile-gorustu,lQMQtnu2PUy-WgfFsSPTvA"
        },
        {
        "haber": "Bakan Koca'dan sağlık çalışanlarına teşvik açıklaması",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/Mru9VlmtYEaexK7pd84SWA.jpg",
        "link": "https://www.ntv.com.tr/saglik/son-dakika-haberi-bakan-kocadan-saglik-calisanlarina-tesvik-aciklamasi,rMIOV-sAhU-pXk8lgMOlNg"
        },
        {
        "haber": "Sancaktepe'de komiser yardımcısı başından vurularak öldürüldü",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/fN-pj2A3RESTkA3YMJcAKg.jpg",
        "link": "https://www.ntv.com.tr/turkiye/sancaktepede-komiser-yardimcisi-basindan-vurularak-olduruldu,s6ETIZcjQ0m0nNsKz7QaeA"
        },
        {
        "haber": "Ukrayna limanlarından 1 milyon tonun üzerinde tahıl taşındı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/sWquCtA4SUCsbluQBTIi1Q.jpg",
        "link": "https://www.ntv.com.tr/dunya/ukrayna-limanlarindan-1-milyon-tonun-uzerinde-tahil-tasindi,-ZMOjftVoki_NaObU0uygQ"
        },
        {
        "haber": "Eren Abluka-34 operasyonunda 19 roketatar sevk fişeği ve 16 milyon kök kenevir ele geçirildi",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/N7m40jP9Ak60KaKJXLd7yw.jpg",
        "link": "https://www.ntv.com.tr/turkiye/eren-abluka-34-operasyonunda-19-roketatar-sevk-fisegi-ve-16-milyon-kok-kenevir-ele-gecirildi,Xowk9XC1d0SLvn_7_EeaMw"
        },
        {
        "haber": "Bakan Kurum'dan Kanal İstanbul açıklaması",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/DpgYwR5yk0KyQPq4cKxwJQ.jpg",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-kurumdan-kanal-istanbul-aciklamasi,HA2fl6Gsh0-7r7-jmOUQiA"
        },
        {
        "haber": "Dışişleri Bakanlığı'ndan Macron'a tepki",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/pjUgdZKjMkmcCiLJpWN66g.jpg",
        "link": "https://www.ntv.com.tr/dunya/son-dakika-haberi-disisleri-bakanligindan-macrona-tepki,zPzzzm4z2kWrLDIDjJbvOQ"
        },
        {
        "haber": "Çanakkale Boğazı girişinde kargo gemisi karaya oturdu",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/whtnTHRYpkmK7kLG75AHNA.jpg",
        "link": "https://www.ntv.com.tr/turkiye/canakkale-bogazi-girisinde-kargo-gemisi-karaya-oturdu,1IGmS04XRUu7_jAaQhvsFw"
        },
        {
        "haber": "Ticari mevduatlar da TMSF sigorta kapsamına alındı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/2d0zqUXVdkOHNjsxNLz8rw.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/son-dakika-haberi-ticari-mevduatlar-da-tmsf-sigorta-kapsamina-alindi,dHdBUVXEeUqe8-U5_z8C0g"
        },
        {
        "haber": "SON DAKİKA: Gaziantep FK, Antalyaspor'u farklı mağlup etti",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/f4E9sLGyv06mUSyOawW6eA.jpg",
        "link": "https://www.ntv.com.tr/sporskor/son-dakikagaziantep-fk-antalyasporu-farkli-maglup-etti,taFLMuj260yzqY4UoiF_nQ"
        },
        {
        "haber": "Fed Başkanı Powell: Enflasyonla mücadele acı verecek",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/lUjneafw2ESvhkMg3MpPIg.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/fed-baskani-powell-enflasyonla-mucadele-aci-verecek,Ua8_zWpch0mvIHQ-ri2G8A"
        },
        {
        "haber": "Aliağa'da sökülecek Brezilya gemisinin izni iptal edildi",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/kMp0jTE3Jk2BMSbDQlQ9_g.jpg",
        "link": "https://www.ntv.com.tr/turkiye/aliagada-sokulecek-brezilya-gemisinin-izni-iptal-edildi,yB2NyNUtU0yyRJ8Zqy1srA"
        },
        {
        "haber": "Madrid Mutabakatı | İsveç-Finlandiya ile ilk toplantı yapıldı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/NlNlhhOlDUGGauLJqoC-TA.jpg",
        "link": "https://www.ntv.com.tr/turkiye/madrid-mutabakati-isvec-finlandiya-ile-ilk-toplanti-yapildi,HMP6X6fa2EyVEWrfNuSipA"
        },
        {
        "haber": "SON DAKİKA: Başakşehir ve Sivasspor'un Konferans Ligi’ndeki rakipleri belli oldu",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/bAtA2K3NGEefBmQazc3dzA.jpg",
        "link": "https://www.ntv.com.tr/sporskor/son-dakikabasaksehir-ve-sivassporun-konferans-ligindeki-rakipleri-belli-oldu,OqOCDAG1kk283cO-UyVjZg"
        },
        {
        "haber": "İcra düzenlemesinde yeni ayrıntılar",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/5oAyDc6khUOCpab0qstT9A.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/icra-duzenlemesinde-yeni-ayrintilar,T1cd-PtYrUuGrIO1HCPrSQ"
        },
        {
        "haber": "MHP af taleplerini inceliyor",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/vXF3g-qRvE6yCr9fi-xNfw.jpg",
        "link": "https://www.ntv.com.tr/turkiye/mhp-af-taleplerini-inceliyor,JbtmHHQHd0G5KVXbvmWYhg"
        },
        {
        "haber": "Cumhurbaşkanı Erdoğan: Hiçbir oyuna tahammülümüz yok",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/c_KGYHpGI0-q4VbCRi8lYg.jpg",
        "link": "https://www.ntv.com.tr/turkiye/cumhurbaskani-erdoganhicbir-oyuna-tahammulumuz-yok,SIEFWdffz0-k1b3pqZS4tA"
        },
        {
        "haber": "Tarımsal destek ödemeleri başladı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/ljZcUB6juUW9u_Ift5g7WA.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/tarimsal-destek-odemeleri-basladi,7w28VxmGHUueIzAJiBPNRQ"
        },
        {
        "haber": "Bakan Nebati'den ABD'nin TÜSİAD mektubuna ilişkin açıklama",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/g3UZhjogFkSBnJcaAy0GPg.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/bakan-nebatiden-abdnin-tusiad-mektubuna-iliskin-aciklama,H-G-0Ifxekm6pizIjwk7pw"
        },
        {
        "haber": "Dünya'dan 100 ışık yılı uzaklıkta bir 'okyanus gezegeni' keşfedildi",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/iSBQHGmN9kWeMtokdv6Huw.jpg",
        "link": "https://www.ntv.com.tr/dunya/dunyadan-100-isik-yili-uzaklikta-bir-okyanus-gezegeni-kesfedildi,ERrqMyU95ku5-KV8XDqdxg"
        },
        {
        "haber": "Çeyrek altın fiyatları bugün ne kadar oldu? 26 Ağustos 2022 güncel altın kuru fiyatları",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/PxLuI33TVkOAYYoc7SSrBg.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/altin/ceyrek-altin-fiyatlari-bugun-ne-kadar-oldu26-agustos2022-guncel-altin-kuru-fiyatlari,VlM3ud3Sl0qUm0-XH5tQBA"
        },
        {
        "haber": "Brent petrol fiyatı ne kadar oldu? (26 Ağustos 2022 petrol fiyatları)",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/d8BP-NRZAES1d6oBMeJkDg.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/brent-petrol-fiyati-ne-kadar-oldu-26-agustos2022-petrol-fiyatlari,QH5YSGQBQ0WlFHBgxbmjnA"
        },
        {
        "haber": "Dolar kuru bugün ne kadar? (26 Ağustos 2022 dolar - euro fiyatları)",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/TpNCbaSQ5EKpQ_zD2R-0kQ.jpg",
        "link": "https://www.ntv.com.tr/ntvpara/doviz/dolar-kuru-bugun-ne-kadar-26-agustos2022-dolar-euro-fiyatlari,G0HlVAGbGUm_wqexgcJSKQ"
        },
        {
        "haber": "Fenerbahçe, UEFA Avrupa Ligi'nde gruplara kaldı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/45wUbqHjj0aPeobrSIWuXg.jpg",
        "link": "https://www.ntv.com.tr/sporskor/son-dakika-fenerbahce-uefa-avrupa-liginde-gruplara-kaldi,GDRNmS35z0SpyLxAhCMc6g"
        },
        {
        "haber": "Denizli'de yolcu otobüsü devrildi: 28 yaralı",
        "gorsel": "https://cdn1.ntv.com.tr/gorsel/h0up6Z7gi0WIgZYyOXA72g.jpg",
        "link": "https://www.ntv.com.tr/turkiye/son-dakika-haberi-denizlide-yolcu-otobusu-devrildi-28-yarali,n9s87oqJekGwL3QpbPaKDQ"
        }
    ]
    }
  """

  print(haber.tablo())
  """
  tabulate verisi döndürür.

    +----------------------------------------------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
    | haber                                                                                        | gorsel                                                    | link                                                                                                                                               |
    |----------------------------------------------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------|
    | Gülşen tahliye edildi                                                                        | https://cdn1.ntv.com.tr/gorsel/mV1y00XI3k6dTjjHIA66bA.jpg | https://www.ntv.com.tr/turkiye/gulsen-tahliye-edilecek-mi,wLkIbiBHjUGk5daeJ_CKjg                                                                   |
    | Ünsal Ban, yurtdışına kaçmaya çalışırken yakalandı                                           | https://cdn1.ntv.com.tr/gorsel/kISG5ug900Oni2ItjCAL5Q.jpg | https://www.ntv.com.tr/turkiye/unsal-ban-yurtdisina-kacmaya-calisirken-yakalandi,2NtsNE__B0qPLV91BoEQlg                                            |
    | Temmuz ayı dış ticaret rakamları açıklandı                                                   | https://cdn1.ntv.com.tr/gorsel/YZuYFxLy7UO8EmB8P74tEQ.jpg | https://www.ntv.com.tr/ntvpara/temmuz-ayi-dis-ticaret-rakamlari-aciklandi,NeL9rRb7pUWPeEa2b5ZKJA                                                   |
    | Brent petrol fiyatı ne kadar oldu? (29 Ağustos 2022 petrol fiyatları)                        | https://cdn1.ntv.com.tr/gorsel/d8BP-NRZAES1d6oBMeJkDg.jpg | https://www.ntv.com.tr/ntvpara/brent-petrol-fiyati-ne-kadar-oldu-29-agustos-2022-petrol-fiyatlari,qKus0SOS4UWhWe262Pf4XQ                           |
    | Dolar kuru bugün ne kadar? (29 Ağustos 2022 dolar - euro fiyatları)                          | https://cdn1.ntv.com.tr/gorsel/TpNCbaSQ5EKpQ_zD2R-0kQ.jpg | https://www.ntv.com.tr/ntvpara/doviz/dolar-kuru-bugun-ne-kadar-29-agustos-2022-dolar-euro-fiyatlari,6V_VbQu9K0WEN1taePB3vA                         |
    | Çeyrek altın fiyatları bugün ne kadar oldu? 29 Ağustos 2022 güncel altın kuru fiyatları      | https://cdn1.ntv.com.tr/gorsel/PxLuI33TVkOAYYoc7SSrBg.jpg | https://www.ntv.com.tr/ntvpara/altin/ceyrek-altin-fiyatlari-bugun-ne-kadar-oldu-29-agustos-2022-guncel-altin-kuru-fiyatlari,QQm9QQIO8EuRKX7tpFYBxw |
    | Dev maçta kazanan yok (Trabzonspor-Galatasaray maç sonucu)                                   | https://cdn1.ntv.com.tr/gorsel/QwkQnBgU5EKmzZyTspkkZg.jpg | https://www.ntv.com.tr/sporskor/son-dakika-dev-macta-kazanan-yok-trabzonspor-galatasaray-mac-sonucu,S7jr-qNX9EaKn_dxHhXjcw                         |
    | Dünya Kupası Elemeleri: Milliler Sırbistan'ı geçemedi (Türkiye-Sırbistan maç sonucu)         | https://cdn1.ntv.com.tr/gorsel/_z3ldT-fzE68VnUScw9b5w.jpg | https://www.ntv.com.tr/sporskor/dunya-kupasi-elemeleri12-dev-adam-sirbistana-79-72-yenildi-turkiye-sirbistan-mac-sonucu,-6buirGsE0SuMzNMA4x59Q     |
    | S-300'le Türk F-16'larına taciz                                                              | https://cdn1.ntv.com.tr/gorsel/-vHtB7DKnUmkzMhopDuaLA.jpg | https://www.ntv.com.tr/turkiye/s-300le-turk-f-16larina-taciz,eu-m13ogpk-MsEMpoXiIrw                                                                |
    | MSB: Tahıl yüklü 6 gemi daha hareket etti                                                    | https://cdn1.ntv.com.tr/gorsel/iL-IHFS7O0WJB13tMbasBA.jpg | https://www.ntv.com.tr/turkiye/son-dakika-haberi-msb-tahil-yuklu-6-gemi-daha-hareket-etti,-cGlwoX0f0ip1VtuefMVvg                                   |
    | SON DAKİKA: Galatasaray Cicaldau'yu kiraladı                                                 | https://cdn1.ntv.com.tr/gorsel/S6iVZbIn-0egqoisQVjQRQ.jpg | https://www.ntv.com.tr/sporskor/son-dakikagalatasaray-cicaldauyu-kiraladi,9Rvu4iEwrkmbjfcJS1yfHA                                                   |
    | Cumhurbaşkanı Erdoğan Aliyev ile görüştü                                                     | https://cdn1.ntv.com.tr/gorsel/FNKtCZGKyUu-OhnJYXMiIQ.jpg | https://www.ntv.com.tr/turkiye/son-dakika-haberi-cumhurbaskani-erdogan-aliyev-ile-gorustu,lQMQtnu2PUy-WgfFsSPTvA                                   |
    | Bakan Koca'dan sağlık çalışanlarına teşvik açıklaması                                        | https://cdn1.ntv.com.tr/gorsel/Mru9VlmtYEaexK7pd84SWA.jpg | https://www.ntv.com.tr/saglik/son-dakika-haberi-bakan-kocadan-saglik-calisanlarina-tesvik-aciklamasi,rMIOV-sAhU-pXk8lgMOlNg                        |
    | Sancaktepe'de komiser yardımcısı başından vurularak öldürüldü                                | https://cdn1.ntv.com.tr/gorsel/fN-pj2A3RESTkA3YMJcAKg.jpg | https://www.ntv.com.tr/turkiye/sancaktepede-komiser-yardimcisi-basindan-vurularak-olduruldu,s6ETIZcjQ0m0nNsKz7QaeA                                 |
    | Ukrayna limanlarından 1 milyon tonun üzerinde tahıl taşındı                                  | https://cdn1.ntv.com.tr/gorsel/sWquCtA4SUCsbluQBTIi1Q.jpg | https://www.ntv.com.tr/dunya/ukrayna-limanlarindan-1-milyon-tonun-uzerinde-tahil-tasindi,-ZMOjftVoki_NaObU0uygQ                                    |
    | Eren Abluka-34 operasyonunda 19 roketatar sevk fişeği ve 16 milyon kök kenevir ele geçirildi | https://cdn1.ntv.com.tr/gorsel/N7m40jP9Ak60KaKJXLd7yw.jpg | https://www.ntv.com.tr/turkiye/eren-abluka-34-operasyonunda-19-roketatar-sevk-fisegi-ve-16-milyon-kok-kenevir-ele-gecirildi,Xowk9XC1d0SLvn_7_EeaMw |
    | Bakan Kurum'dan Kanal İstanbul açıklaması                                                    | https://cdn1.ntv.com.tr/gorsel/DpgYwR5yk0KyQPq4cKxwJQ.jpg | https://www.ntv.com.tr/turkiye/son-dakika-haberi-bakan-kurumdan-kanal-istanbul-aciklamasi,HA2fl6Gsh0-7r7-jmOUQiA                                   |
    | Dışişleri Bakanlığı'ndan Macron'a tepki                                                      | https://cdn1.ntv.com.tr/gorsel/pjUgdZKjMkmcCiLJpWN66g.jpg | https://www.ntv.com.tr/dunya/son-dakika-haberi-disisleri-bakanligindan-macrona-tepki,zPzzzm4z2kWrLDIDjJbvOQ                                        |
    | Çanakkale Boğazı girişinde kargo gemisi karaya oturdu                                        | https://cdn1.ntv.com.tr/gorsel/whtnTHRYpkmK7kLG75AHNA.jpg | https://www.ntv.com.tr/turkiye/canakkale-bogazi-girisinde-kargo-gemisi-karaya-oturdu,1IGmS04XRUu7_jAaQhvsFw                                        |
    | Ticari mevduatlar da TMSF sigorta kapsamına alındı                                           | https://cdn1.ntv.com.tr/gorsel/2d0zqUXVdkOHNjsxNLz8rw.jpg | https://www.ntv.com.tr/ntvpara/son-dakika-haberi-ticari-mevduatlar-da-tmsf-sigorta-kapsamina-alindi,dHdBUVXEeUqe8-U5_z8C0g                         |
    | SON DAKİKA: Gaziantep FK, Antalyaspor'u farklı mağlup etti                                   | https://cdn1.ntv.com.tr/gorsel/f4E9sLGyv06mUSyOawW6eA.jpg | https://www.ntv.com.tr/sporskor/son-dakikagaziantep-fk-antalyasporu-farkli-maglup-etti,taFLMuj260yzqY4UoiF_nQ                                      |
    | Fed Başkanı Powell: Enflasyonla mücadele acı verecek                                         | https://cdn1.ntv.com.tr/gorsel/lUjneafw2ESvhkMg3MpPIg.jpg | https://www.ntv.com.tr/ntvpara/fed-baskani-powell-enflasyonla-mucadele-aci-verecek,Ua8_zWpch0mvIHQ-ri2G8A                                          |
    | Aliağa'da sökülecek Brezilya gemisinin izni iptal edildi                                     | https://cdn1.ntv.com.tr/gorsel/kMp0jTE3Jk2BMSbDQlQ9_g.jpg | https://www.ntv.com.tr/turkiye/aliagada-sokulecek-brezilya-gemisinin-izni-iptal-edildi,yB2NyNUtU0yyRJ8Zqy1srA                                      |
    | Madrid Mutabakatı | İsveç-Finlandiya ile ilk toplantı yapıldı                                | https://cdn1.ntv.com.tr/gorsel/NlNlhhOlDUGGauLJqoC-TA.jpg | https://www.ntv.com.tr/turkiye/madrid-mutabakati-isvec-finlandiya-ile-ilk-toplanti-yapildi,HMP6X6fa2EyVEWrfNuSipA                                  |
    | SON DAKİKA: Başakşehir ve Sivasspor'un Konferans Ligi’ndeki rakipleri belli oldu             | https://cdn1.ntv.com.tr/gorsel/bAtA2K3NGEefBmQazc3dzA.jpg | https://www.ntv.com.tr/sporskor/son-dakikabasaksehir-ve-sivassporun-konferans-ligindeki-rakipleri-belli-oldu,OqOCDAG1kk283cO-UyVjZg                |
    | İcra düzenlemesinde yeni ayrıntılar                                                          | https://cdn1.ntv.com.tr/gorsel/5oAyDc6khUOCpab0qstT9A.jpg | https://www.ntv.com.tr/ntvpara/icra-duzenlemesinde-yeni-ayrintilar,T1cd-PtYrUuGrIO1HCPrSQ                                                          |
    | MHP af taleplerini inceliyor                                                                 | https://cdn1.ntv.com.tr/gorsel/vXF3g-qRvE6yCr9fi-xNfw.jpg | https://www.ntv.com.tr/turkiye/mhp-af-taleplerini-inceliyor,JbtmHHQHd0G5KVXbvmWYhg                                                                 |
    | Cumhurbaşkanı Erdoğan: Hiçbir oyuna tahammülümüz yok                                         | https://cdn1.ntv.com.tr/gorsel/c_KGYHpGI0-q4VbCRi8lYg.jpg | https://www.ntv.com.tr/turkiye/cumhurbaskani-erdoganhicbir-oyuna-tahammulumuz-yok,SIEFWdffz0-k1b3pqZS4tA                                           |
    | Tarımsal destek ödemeleri başladı                                                            | https://cdn1.ntv.com.tr/gorsel/ljZcUB6juUW9u_Ift5g7WA.jpg | https://www.ntv.com.tr/ntvpara/tarimsal-destek-odemeleri-basladi,7w28VxmGHUueIzAJiBPNRQ                                                            |
    | Bakan Nebati'den ABD'nin TÜSİAD mektubuna ilişkin açıklama                                   | https://cdn1.ntv.com.tr/gorsel/g3UZhjogFkSBnJcaAy0GPg.jpg | https://www.ntv.com.tr/ntvpara/bakan-nebatiden-abdnin-tusiad-mektubuna-iliskin-aciklama,H-G-0Ifxekm6pizIjwk7pw                                     |
    | Dünya'dan 100 ışık yılı uzaklıkta bir 'okyanus gezegeni' keşfedildi                          | https://cdn1.ntv.com.tr/gorsel/iSBQHGmN9kWeMtokdv6Huw.jpg | https://www.ntv.com.tr/dunya/dunyadan-100-isik-yili-uzaklikta-bir-okyanus-gezegeni-kesfedildi,ERrqMyU95ku5-KV8XDqdxg                               |
    | Çeyrek altın fiyatları bugün ne kadar oldu? 26 Ağustos 2022 güncel altın kuru fiyatları      | https://cdn1.ntv.com.tr/gorsel/PxLuI33TVkOAYYoc7SSrBg.jpg | https://www.ntv.com.tr/ntvpara/altin/ceyrek-altin-fiyatlari-bugun-ne-kadar-oldu26-agustos2022-guncel-altin-kuru-fiyatlari,VlM3ud3Sl0qUm0-XH5tQBA   |
    | Brent petrol fiyatı ne kadar oldu? (26 Ağustos 2022 petrol fiyatları)                        | https://cdn1.ntv.com.tr/gorsel/d8BP-NRZAES1d6oBMeJkDg.jpg | https://www.ntv.com.tr/ntvpara/brent-petrol-fiyati-ne-kadar-oldu-26-agustos2022-petrol-fiyatlari,QH5YSGQBQ0WlFHBgxbmjnA                            |
    | Dolar kuru bugün ne kadar? (26 Ağustos 2022 dolar - euro fiyatları)                          | https://cdn1.ntv.com.tr/gorsel/TpNCbaSQ5EKpQ_zD2R-0kQ.jpg | https://www.ntv.com.tr/ntvpara/doviz/dolar-kuru-bugun-ne-kadar-26-agustos2022-dolar-euro-fiyatlari,G0HlVAGbGUm_wqexgcJSKQ                          |
    | Fenerbahçe, UEFA Avrupa Ligi'nde gruplara kaldı                                              | https://cdn1.ntv.com.tr/gorsel/45wUbqHjj0aPeobrSIWuXg.jpg | https://www.ntv.com.tr/sporskor/son-dakika-fenerbahce-uefa-avrupa-liginde-gruplara-kaldi,GDRNmS35z0SpyLxAhCMc6g                                    |
    | Denizli'de yolcu otobüsü devrildi: 28 yaralı                                                 | https://cdn1.ntv.com.tr/gorsel/h0up6Z7gi0WIgZYyOXA72g.jpg | https://www.ntv.com.tr/turkiye/son-dakika-haberi-denizlide-yolcu-otobusu-devrildi-28-yarali,n9s87oqJekGwL3QpbPaKDQ                                 |
    +----------------------------------------------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
  """

  print(haber.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['haber', 'gorsel', 'link']
  """