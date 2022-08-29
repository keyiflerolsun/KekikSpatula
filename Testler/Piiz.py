from KekikSpatula import Piiz

def test_piiz():
  piiz = Piiz()

  print(piiz.veri)
  """
  json verisi döndürür

  {'kaynak': 'piizapp.com', 'veri': [{'tur': 'bira', 'ad': '33cl Bud Depozitosuz Şişe', 'fiyat': 21.0}, {'tur': 'bira', 'ad': '25cl Efes Malt Depozitosuz Şişe', 'fiyat': 21.0}, {'tur': 'bira', 'ad': '45cl Varım Kutu', 'fiyat': 22.0}, {'tur': 'bira', 'ad': '45cl Varım Limonlu Kutu', 'fiyat': 22.0}, {'tur': 'bira', 'ad': '23,7cl Tuborg Kırmızı Shot Special Kutu', 'fiyat': 22.5}, {'tur': 'bira', 'ad': '50cl Bud Kutu Şişe', 'fiyat': 23.0}, {'tur': 'bira', 'ad': '50cl Bud Depozitosuz Şişe', 'fiyat': 23.0}, {'tur': 'bira', 'ad': '33cl Tuborg Gold Depozitosuz Şişe', 'fiyat': 23.5}, {'tur': 'bira', 'ad': '33cl Tuborg Gold Kutu', 'fiyat': 23.5}, {'tur': 'bira', 'ad': '33cl Tuborg Amber Depozitosuz Şişe', 'fiyat': 23.5}, {'tur': 'bira', 'ad': '33cl Efes Pilsen Kutu', 'fiyat': 25.0}, {'tur': 'bira', 'ad': '33cl Carlsberg Kutu', 'fiyat': 25.5}, {'tur': 'bira', 'ad': '33cl Bomonti Red Ale Depozitosuz Şişe', 'fiyat': 26.0}, {'tur': 'bira', 'ad': '33cl Bomonti Black Depozitosuz Şişe', 'fiyat': 26.0}, {'tur': 'bira', 'ad': '33cl Miller Depozitosuz Şişe', 'fiyat': 26.0}, {'tur': 'bira', 'ad': '33cl Bomonti İpa Depozitosuz Şişe', 'fiyat': 26.5}, {'tur': 'bira', 'ad': '50cl Carlsberg Kutu', 'fiyat': 27.0}, {'tur': 'bira', 'ad': '33cl Carlsberg Depozitosuz Şişe', 'fiyat': 27.0}, {'tur': 'bira', 'ad': '50cl Tuborg Gold Depozitolu Şişe', 'fiyat': 27.5}, {'tur': 'bira', 'ad': '50cl Efes Malt Depozitolu Şişe', 'fiyat': 27.5}, {'tur': 'bira', 'ad': '35cl Frederic Marzen Lager Şişe', 'fiyat': 27.5}, {'tur': 'bira', 'ad': '35cl Frederic India Pale Ale Şişe', 'fiyat': 27.5}, {'tur': 'bira', 'ad': '35cl Frederic Brown Ale Şişe', 'fiyat': 27.5}, {'tur': 'bira', 'ad': '35cl Frederic White Ipa Şişe', 'fiyat': 27.5}, {'tur': 'bira', 'ad': '50cl Carlsberg Depozitolu Şişe', 'fiyat': 27.5}, {'tur': 'bira', 'ad': '33cl Grimbergen Blonde Depozitosuz Şişe', 'fiyat': 28.0}, {'tur': 'bira', 'ad': '33cl Kronenbourg 1664 Blanc Depozitosuz Şişe', 'fiyat': 28.0}, {'tur': 'bira', 'ad': '33cl SOL Cerveza Depozitosuz Şişe', 'fiyat': 28.0}, {'tur': 'bira', 'ad': '33cl Weihenstephan Depozitosuz Şişe', 'fiyat': 28.0}, {'tur': 'bira', 'ad': "33cl Beck's Depozitosuz Şişe", 'fiyat': 28.0}, {'tur': 'bira', 'ad': '50cl Bomonti Depozitolu Şişe', 'fiyat': 28.0}, {'tur': 'bira', 'ad': '50cl Tuborg Gold Kutu', 'fiyat': 28.0}, {'tur': 'bira', 'ad': '50cl Bomonti Depozitosuz Şişe', 'fiyat': 28.5}, {'tur': 'bira', 'ad': '50cl Tuborg Amber Kutu', 'fiyat': 29.0}, {'tur': 'bira', 'ad': '50cl Tuborg Gold Depozitosuz Şişe', 'fiyat': 29.0}, {'tur': 'bira', 'ad': '50cl Efes Malt Kutu', 'fiyat': 29.0}, {'tur': 'bira', 'ad': '50cl Efes Extra Kutu', 'fiyat': 29.0}, {'tur': 'bira', 'ad': '50cl Efes Pilsen Kutu', 'fiyat': 29.0}, {'tur': 'bira', 'ad': '33cl Efes Brewmaster Red Ale Depozitosuz Şişe', 'fiyat': 29.5}, {'tur': 'bira', 'ad': '50cl Tuborg Amber Depozitosuz Şişe', 'fiyat': 29.5}, {'tur': 'bira', 'ad': '50cl Efes Pilsen Depozitolu Uzun Şişe', 'fiyat': 29.5}, {'tur': 'bira', 'ad': '33cl Efes Brewmaster White Ale Depozitosuz Şişe', 'fiyat': 29.5}, {'tur': 'bira', 'ad': '50cl Bomonti Filtresiz Depozitosuz Şişe', 'fiyat': 30.0}, {'tur': 'bira', 'ad': '50cl Tuborg Filtresiz Kutu', 'fiyat': 30.0}, {'tur': 'bira', 'ad': '50cl Tuborg Filtresiz Depozitosuz Şişe', 'fiyat': 30.0}, {'tur': 'bira', 'ad': '33cl Grimbergen Double Ambree Depozitosuz Şişe', 'fiyat': 30.0}, {'tur': 'bira', 'ad': '33cl Desperados Depozitosuz Şişe', 'fiyat': 31.0}, {'tur': 'bira', 'ad': '50cl Bomonti Filtresiz Kutu', 'fiyat': 31.0}, {'tur': 'bira', 'ad': '50cl Tuborg Kırmızı Special Kutu', 'fiyat': 31.5}, {'tur': 'bira', 'ad': "50cl Beck's Depozitosuz Şişe", 'fiyat': 32.0}, {'tur': 'bira', 'ad': "50cl Beck's Kutu", 'fiyat': 32.0}, {'tur': 'bira', 'ad': '50cl Efes Pilsen Özel Seri Depozitosuz', 'fiyat': 32.0}, {'tur': 'bira', 'ad': '33cl Weihenstephan Vitus Depozitosuz Şişe', 'fiyat': 32.0}, {'tur': 'bira', 'ad': '50cl Miller Kutu', 'fiyat': 33.0}, {'tur': 'bira', 'ad': '50cl Miller Depozitosuz Şişe', 'fiyat': 33.0}, {'tur': 'bira', 'ad': 'Efes Glutensiz 50cl', 'fiyat': 33.0}, {'tur': 'bira', 'ad': '50cl Efes Fıçı Yüksek Alkollü Kutu', 'fiyat': 33.0}, {'tur': 'bira', 'ad': '50cl Efes Fıçı Yüksek Alkollü Şişe Depozitosuz', 'fiyat': 34.0}, {'tur': 'sarap', 'ad': '75cl Sevilen Agora Beyaz Şarap', 'fiyat': 39.0}, {'tur': 'bira', 'ad': '35,5cl Corona Extra Şişe', 'fiyat': 40.0}, {'tur': 'bira', 'ad': '100cl Skol Bira Depozitosuz Pet Şişe', 'fiyat': 40.0}, {'tur': 'bira', 'ad': '44cl Guinness Kutu', 'fiyat': 40.5}, {'tur': 'sarap', 'ad': '75cl Agora Kırmızı Şarap (Sevilen)', 'fiyat': 41.0}, {'tur': 'sarap', 'ad': '75cl Sevilen Altıntepe Kırmızı Şarap', 'fiyat': 41.5}, {'tur': 'bira', 'ad': '33cl Hoegaarden Depozitosuz Şişe', 'fiyat': 42.0}, {'tur': 'bira', 'ad': '33cl Erdinger Depozitosuz Şişe', 'fiyat': 42.0}, {'tur': 'bira', 'ad': '50cl Amsterdam Navigator Depozitosuz Şişe', 'fiyat': 44.0}, {'tur': 'bira', 'ad': '50cl Amsterdam Navigator Kutu', 'fiyat': 44.0}, {'tur': 'sarap', 'ad': '75cl Sevilen Kalecik Karası Kırmızı Şarap', 'fiyat': 44.9}, {'tur': 'sarap', 'ad': '75cl Sevilen Majestik Gamay Kırmızı Şarap', 'fiyat': 44.9}, {'tur': 'sarap', 'ad': '75cl Sevilen Sultaniye Beyaz Şarap', 'fiyat': 44.9}, {'tur': 'bira', 'ad': '33cl Leffe Brune Blonde Depozitosuz Şişe', 'fiyat': 45.0}, {'tur': 'bira', 'ad': '100cl Marmara Gold Depozitosuz Şişe', 'fiyat': 45.0}, {'tur': 'bira', 'ad': '33cl Leffe Brune Depozitosuz Şişe', 'fiyat': 45.0}, {'tur': 'sarap', 'ad': '75cl Sevilen Majestik Öküzgözü Kırmızı', 'fiyat': 45.9}, {'tur': 'sarap', 'ad': '75cl Sevilen Majestik Gamay Kırmızı Şarap', 'fiyat': 45.9}, {'tur': 'bira', 'ad': '33cl Leffe Radieuse Depozitosuz Şişe', 'fiyat': 48.0}, {'tur': 'kokteyl', 'ad': '14.4 Çilekli Volim', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': '14.4 Volim Redbull', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': '14.4 Volim Limonlu Alkol', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': 'Volim Sade', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': 'Volim Karışık Meyveli', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': 'Volim Karpuz Aromalı', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': 'Volim Kola Aromalı', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': 'Volim Shot Karpuz Çilek', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': 'Volim Shot Votka İçeçeği', 'fiyat': 50.0}, {'tur': 'kokteyl', 'ad': 'Volim Enerji İçeceği Aromalı', 'fiyat': 50.0}, {'tur': 'sarap', 'ad': '18,75cl Villa Doluca Şarap', 'fiyat': 50.0}, {'tur': 'bira', 'ad': '45cl Grolsch Depozitosuz Şişe', 'fiyat': 52.0}, {'tur': 'bira', 'ad': '33cl Duvel Depozitosuz Şişe', 'fiyat': 57.0}, {'tur': 'sarap', 'ad': '75cl Biricik Sek Beyaz Cam Şarap', 'fiyat': 60.0}, {'tur': 'sarap', 'ad': '75cl Biricik Sek Kırmızı CamŞarap', 'fiyat': 60.0}, {'tur': 'sarap', 'ad': '75cl Biricik Sek Kırmızı Cam Şarap', 'fiyat': 60.0}, {'tur': 'sarap', 'ad': '75cl Biricik Sek Beyaz Cam Şarap', 'fiyat': 60.0}, {'tur': 'raki', 'ad': '20cl Saki Rakı Yaş Üzüm', 'fiyat': 64.5}, {'tur': 'sarap', 'ad': '75cl Sevilen İsabey Saublanc (Beyaz)', 'fiyat': 79.0}, {'tur': 'sarap', 'ad': '75cl Sevilen İsabey Merlot Şarap', 'fiyat': 79.5}, {'tur': 'sarap', 'ad': '75cl Sevilen İsabey Narince Beyaz Şarap', 'fiyat': 79.5}, {'tur': 'sarap', 'ad': '75cl Sevilen İsabey Cabarnet', 'fiyat': 79.5}, {'tur': 'sarap', 'ad': '100cl Biricik Sek Kırmızı Cam Şarap', 'fiyat': 80.0}, {'tur': 'sarap', 'ad': '100cl Biricik Sek Kırmızı Cam Şarap', 'fiyat': 80.0}, {'tur': 'sarap', 'ad': '100cl Biricik Sek Beyaz Cam Şarap', 'fiyat': 80.0}, {'tur': 'sarap', 'ad': '75cl Mistik Şarap', 'fiyat': 80.0}, {'tur': 'sarap', 'ad': '100cl Biricik Sek Beyaz Cam Şarap', 'fiyat': 80.0}, {'tur': 'sarap', 'ad': '37,5cl Villa Doluca Şarap', 'fiyat': 80.0}, {'tur': 'sarap', 'ad': '37,5cl Doluca Şarap', 'fiyat': 80.0}, {'tur': 'raki', 'ad': '35cl Saki Ginseng', 'fiyat': 88.5}, {'tur': 'votka', 'ad': '20cl İstanblue Votka', 'fiyat': 91.0}, {'tur': 'likor', 'ad': '50cl Hare Nane Likörü', 'fiyat': 95.0}, {'tur': 'likor', 'ad': '50cl Hare Acıbadem Likörü', 'fiyat': 95.0}, {'tur': 'likor', 'ad': '50cl Hare Muz Likörü', 'fiyat': 95.0}, {'tur': 'likor', 'ad': '50cl Hare Vişne Likörü', 'fiyat': 95.0}, {'tur': 'likor', 'ad': '50cl Hare Hindistan Cevizi Likörü', 'fiyat': 95.0}, {'tur': 'sarap', 'ad': '75cl Crama Regala Sauvignon Blanc', 'fiyat': 99.9}, {'tur': 'sarap', 'ad': '75cl Crama Regala Chardonnay', 'fiyat': 104.9}, {'tur': 'sarap', 'ad': '75cl Crama Regala Merlot', 'fiyat': 104.9}, {'tur': 'sarap', 'ad': '75cl Crama Regala Cabernet Sauvignon', 'fiyat': 104.9}, {'tur': 'sarap', 'ad': 'Biricik Sek Kırmızı-Beyaz-Rose Şarap', 'fiyat': 110.0}, {'tur': 'likor', 'ad': '50cl Hare Portakal Likörü', 'fiyat': 110.0}, {'tur': 'sarap', 'ad': '150cl Biricik Galon Kırmızı Cam Şarap', 'fiyat': 118.0}, {'tur': 'sarap', 'ad': 'Biricik Sek Kırmızı-Beyaz-Blush Şarap', 'fiyat': 118.0}, {'tur': 'sarap', 'ad': '150cl Biricik Galon Beyaz Cam Şarap', 'fiyat': 118.0}, {'tur': 'sarap', 'ad': '150cl Biricik Galon Kırmızı Cam Şarap', 'fiyat': 118.0}, {'tur': 'sarap', 'ad': '150cl Biricik Galon Beyaz Cam Şarap', 'fiyat': 118.0}, {'tur': 'likor', 'ad': '100cl Hare Kahve, Portakal, Kayısı Likörü', 'fiyat': 125.0}, {'tur': 'likor', 'ad': '100cl Hare Çikolata Likörü', 'fiyat': 125.0}, {'tur': 'likor', 'ad': '100cl Hare Acıbadem, Bitter, Nane Likörü', 'fiyat': 125.0}, {'tur': 'likor', 'ad': '100cl Hare Şeftali, Muz, Tropikal Likörü', 'fiyat': 125.0}, {'tur': 'sarap', 'ad': '75cl Dlc Sultaniye Emir Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Shiraz Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Cab. Sauvıgnon-Merlot Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Moskado Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Kalecik Karası Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Öküzgözü Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Boğazkere Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Sauvıgnon Blanc Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Frenache Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Dlc Narince Şarap', 'fiyat': 130.0}, {'tur': 'sarap', 'ad': '75cl Doluca Şarap', 'fiyat': 130.0}, {'tur': 'raki', 'ad': '35cl Anadolu Boğma Rakı', 'fiyat': 130.5}, {'tur': 'likor', 'ad': '35cl Muz Likörü', 'fiyat': 132.0}, {'tur': 'sarap', 'ad': '150cl Biricik Kulplu Kırmızı Şarap', 'fiyat': 132.0}, {'tur': 'sarap', 'ad': '150cl Biricik Kulplu Beyaz Şarap', 'fiyat': 132.0}, {'tur': 'likor', 'ad': '35cl Portakal Likörü', 'fiyat': 132.0}, {'tur': 'likor', 'ad': '35cl Nane Likörü', 'fiyat': 132.0}, {'tur': 'likor', 'ad': '35cl Acıbadem Likörü', 'fiyat': 132.0}, {'tur': 'likor', 'ad': '35cl Ahududu Likörü', 'fiyat': 132.0}, {'tur': 'likor', 'ad': '35cl Vişne Likörü', 'fiyat': 132.0}, {'tur': 'likor', 'ad': '35cl Damla Sakızlı Likör', 'fiyat': 132.0}, {'tur': 'votka', 'ad': '35cl Bazooka Votka', 'fiyat': 139.0}, {'tur': 'sarap', 'ad': '100cl Mistik Şarap', 'fiyat': 140.0}, {'tur': 'votka', 'ad': '35cl İstanblue Votka', 'fiyat': 140.0}, {'tur': 'raki', 'ad': '35cl Ata Rakı', 'fiyat': 140.0}, {'tur': 'sarap', 'ad': '75cl Villa Doluca Şarap', 'fiyat': 140.0}, {'tur': 'votka', 'ad': '20cl Lithuanian Vodka', 'fiyat': 140.9}, {'tur': 'raki', 'ad': '20cl Saki Rakı Klasik', 'fiyat': 145.5}, {'tur': 'raki', 'ad': '35cl Yekta Rakı', 'fiyat': 149.0}, {'tur': 'raki', 'ad': '35cl Burgaz Rakı', 'fiyat': 149.5}, {'tur': 'votka', 'ad': '35cl Wyborowa Votka', 'fiyat': 150.0}, {'tur': 'sarap', 'ad': '75cl Villa Doluca Neo Şarap', 'fiyat': 150.0}, {'tur': 'sarap', 'ad': '200cl Biricik Galon Beyaz Cam Şarap', 'fiyat': 155.0}, {'tur': 'sarap', 'ad': '200cl Biricik Galon Kırmızı Cam Şarap', 'fiyat': 155.0}, {'tur': 'raki', 'ad': '20cl Saki Rakı Altın Seri', 'fiyat': 156.0}, {'tur': 'cin', 'ad': "35cl Gilbey's Cin", 'fiyat': 159.0}, {'tur': 'raki', 'ad': '35cl Tayfa Rakı', 'fiyat': 159.5}, {'tur': 'votka', 'ad': "35cl Gilbey's Votka", 'fiyat': 160.0}, {'tur': 'cin', 'ad': '35cl Stirling Cin', 'fiyat': 160.9}, {'tur': 'viski', 'ad': '35cl Jack Daniels Tennessee Honey Viski', 'fiyat': 163.0}, {'tur': 'viski', 'ad': '35cl Jack Daniels Tennessee Apple Viski', 'fiyat': 163.0}, {'tur': 'raki', 'ad': '70cl Saki Ginseng', 'fiyat': 164.5}, {'tur': 'sarap', 'ad': '100cl Doluca Şarap', 'fiyat': 165.0}, {'tur': 'raki', 'ad': '35cl İzmir Rakısı', 'fiyat': 169.0}, {'tur': 'tekila', 'ad': '35cl Olmeca Blanco Tekila', 'fiyat': 169.0}, {'tur': 'votka', 'ad': '35cl Binboa Votka', 'fiyat': 169.0}, {'tur': 'votka', 'ad': '35cl Stumbra Centenary Vodka', 'fiyat': 170.0}, {'tur': 'viski', 'ad': '35cl Ballantines Finest Viski', 'fiyat': 175.0}, {'tur': 'raki', 'ad': '35cl Saki Rakı Klasik', 'fiyat': 175.2}, {'tur': 'raki', 'ad': '35cl İzmir Rakısı Yaş Üzüm', 'fiyat': 175.5}, {'tur': 'raki', 'ad': '35cl Yeni Rakı', 'fiyat': 176.75}, {'tur': 'viski', 'ad': '20cl Chivas Regal (12 Yıllık) Viski', 'fiyat': 179.0}, {'tur': 'kokteyl', 'ad': '100cl Volim', 'fiyat': 180.0}, {'tur': 'raki', 'ad': '35cl İzmir Rakısı Göbek', 'fiyat': 185.0}, {'tur': 'votka', 'ad': '35cl Smirnoff Red Votka', 'fiyat': 185.0}, {'tur': 'tekila', 'ad': '35cl Olmeca Gold Tekila', 'fiyat': 189.0}, {'tur': 'votka', 'ad': '50cl Bazooka Votka', 'fiyat': 189.0}, {'tur': 'kokteyl', 'ad': 'Kırbıyık Kokteyl Mojito 100cl', 'fiyat': 190.0}, {'tur': 'kokteyl', 'ad': 'Kırbıyık Kokteyl Cosmopolitan 100cl', 'fiyat': 190.0}, {'tur': 'kokteyl', 'ad': 'Kırbıyık Kokteyl Sek On The Beach 100cl', 'fiyat': 190.0}, {'tur': 'kokteyl', 'ad': 'Kırbıyık Kokteyl Orman Meyveli 100cl', 'fiyat': 190.0}, {'tur': 'kokteyl', 'ad': 'Kırbıyık Kokteyl Margarita 100cl', 'fiyat': 190.0}, {'tur': 'kokteyl', 'ad': 'Bue Hawaii 100cl', 'fiyat': 190.0}, {'tur': 'kokteyl', 'ad': 'Kırbıyık Kokteyl Kavun 100cl', 'fiyat': 190.0}, {'tur': 'kokteyl', 'ad': 'Kırbıyık Kokteyl Karpuz Çilek 100cl', 'fiyat': 190.0}, {'tur': 'kokteyl', 'ad': "Harrley's Irish Cream 100cl", 'fiyat': 190.0}, {'tur': 'likor', 'ad': '100cl Hare Portakal Likörü', 'fiyat': 190.0}, {'tur': 'tekila', 'ad': '70cl El Jimador Blanco Tequila', 'fiyat': 195.0}, {'tur': 'votka', 'ad': '50cl İstanblue Votka', 'fiyat': 195.0}, {'tur': 'raki', 'ad': '20cl Saki Rakı Siyah Üzüm', 'fiyat': 195.5}, {'tur': 'raki', 'ad': '35cl Yeni Rakı Yeni Seri', 'fiyat': 199.0}, {'tur': 'raki', 'ad': '35cl Tekirdağ Rakı', 'fiyat': 199.0}, {'tur': 'cin', 'ad': "35cl Gordon's Dry Cin", 'fiyat': 199.0}, {'tur': 'raki', 'ad': '35cl Saki Rakı Altın Seri', 'fiyat': 199.5}, {'tur': 'raki', 'ad': '35cl Tekirdağ Rakı Trakya Serisi', 'fiyat': 199.5}, {'tur': 'votka', 'ad': '35cl Lithuanian Vodka', 'fiyat': 199.9}, {'tur': 'raki', 'ad': '35cl Efe Yaş Üzüm Rakı', 'fiyat': 200.0}, {'tur': 'raki', 'ad': '35cl Tekirdağ Rakı Kavrulmuş Anason', 'fiyat': 200.0}, {'tur': 'raki', 'ad': '35cl Saki Rakı Yaş Üzüm', 'fiyat': 200.5}, {'tur': 'viski', 'ad': '35cl Ballantines 12 Yıl Viski', 'fiyat': 205.0}, {'tur': 'votka', 'ad': '50cl Wyborowa Votka', 'fiyat': 205.0}, {'tur': 'viski', 'ad': '35cl Jack Daniels Old No.7 Viski', 'fiyat': 205.5}, {'tur': 'raki', 'ad': '35cl Tekirdağ Rakı Altın Seri', 'fiyat': 209.0}, {'tur': 'votka', 'ad': '35cl Absolut Vodka', 'fiyat': 209.0}, {'tur': 'raki', 'ad': '35cl Efe Gold Rakı', 'fiyat': 209.5}, {'tur': 'tekila', 'ad': '70cl El Jimador Reposado Tequila', 'fiyat': 210.0}, {'tur': 'cin', 'ad': '35cl Beefeater Cin', 'fiyat': 210.0}, {'tur': 'likor', 'ad': '100cl Garrone Ricard Likör', 'fiyat': 210.0}, {'tur': 'raki', 'ad': '35cl Yeni Rakı Ustaların Karışımı', 'fiyat': 215.5}, {'tur': 'viski', 'ad': "35cl Bell's Viski", 'fiyat': 219.0}, {'tur': 'raki', 'ad': '50cl Tayfa Rakı', 'fiyat': 219.0}, {'tur': 'raki', 'ad': '35cl Efe Çilingir Xtra Rakı', 'fiyat': 220.5}, {'tur': 'likor', 'ad': '100cl Garrone Rosso Likör', 'fiyat': 225.0}, {'tur': 'likor', 'ad': '35cl Jagermeister', 'fiyat': 225.0}, {'tur': 'likor', 'ad': '100cl Garrone Bianco Dry Likör', 'fiyat': 225.0}, {'tur': 'votka', 'ad': '50cl Stumbra Centenary Vodka', 'fiyat': 225.9}, {'tur': 'raki', 'ad': '35cl Efe Tek İmbik Rakı', 'fiyat': 226.0}, {'tur': 'raki', 'ad': '35cl Yeni Rakı Âlâ', 'fiyat': 229.0}, {'tur': 'raki', 'ad': '50cl Burgaz Rakı', 'fiyat': 229.0}, {'tur': 'raki', 'ad': '35cl Kulüp Rakı', 'fiyat': 229.5}, {'tur': 'cin', 'ad': '50cl Stirling Cin', 'fiyat': 230.9}, {'tur': 'sarap', 'ad': '150cl Mistik Şarap', 'fiyat': 235.0}, {'tur': 'tekila', 'ad': '50cl Olmeca Blanco Tekila', 'fiyat': 235.0}, {'tur': 'raki', 'ad': '70cl Anadolu Boğma Rakı', 'fiyat': 235.0}, {'tur': 'raki', 'ad': '35cl Beylerbeyi Göbek Rakısı', 'fiyat': 235.0}, {'tur': 'raki', 'ad': '50cl İzmir Rakısı', 'fiyat': 239.5}, {'tur': 'sarap', 'ad': '300cl Biricik Kulplu Beyaz Şarap', 'fiyat': 240.0}, {'tur': 'sarap', 'ad': 'Biricik Suni Yarı Köpüren Şarap (Beyaz-Rose)', 'fiyat': 240.0}, {'tur': 'raki', 'ad': '35cl Altınbaş Rakı', 'fiyat': 240.0}, {'tur': 'sarap', 'ad': '300cl Biricik Kulplu Kırmızı Şarap', 'fiyat': 240.0}, {'tur': 'viski', 'ad': '50cl Ballantines Finest Viski', 'fiyat': 245.0}, {'tur': 'raki', 'ad': '50cl İzmir Rakısı Yaş Üzüm', 'fiyat': 245.0}, {'tur': 'viski', 'ad': '35cl J&B Viski', 'fiyat': 245.0}, {'tur': 'viski', 'ad': '35cl Johnnie Walker Black Label Viski', 'fiyat': 245.0}, {'tur': 'raki', 'ad': '35cl Saki Rakı Siyah Üzüm', 'fiyat': 245.5}, {'tur': 'raki', 'ad': '35cl Efe Klasik Rakı', 'fiyat': 245.5}, {'tur': 'votka', 'ad': '50cl Smirnoff Red', 'fiyat': 249.5}, {'tur': 'raki', 'ad': '50cl Efe Klasik Rakı', 'fiyat': 249.5}, {'tur': 'raki', 'ad': '35cl Efe Çilingir Xtra Yaş Üzüm Rakı', 'fiyat': 249.9}, {'tur': 'raki', 'ad': '35cl Efe 3 Distile Rakı', 'fiyat': 250.0}, {'tur': 'raki', 'ad': '35cl Efe Geleneksel Rakı', 'fiyat': 250.9}, {'tur': 'raki', 'ad': '50cl Saki Rakı Klasik', 'fiyat': 250.9}, {'tur': 'raki', 'ad': '35cl Efe Çilingir Rakı', 'fiyat': 251.9}, {'tur': 'raki', 'ad': '35cl Efe Sarı Zeybek Rakı', 'fiyat': 257.0}, {'tur': 'votka', 'ad': '70cl Bazooka Votka', 'fiyat': 260.0}, {'tur': 'votka', 'ad': '70cl İstanblue Votka', 'fiyat': 265.5}, {'tur': 'votka', 'ad': '70cl Lithuanian Vodka', 'fiyat': 269.9}, {'tur': 'raki', 'ad': '70cl Ata Rakı', 'fiyat': 271.0}, {'tur': 'raki', 'ad': '50cl Tekirdağ Rakı', 'fiyat': 275.0}, {'tur': 'votka', 'ad': '70cl Wyborowa Votka', 'fiyat': 275.0}, {'tur': 'viski', 'ad': '35cl Johnnie Walker Red Label Viski', 'fiyat': 275.0}, {'tur': 'viski', 'ad': '50cl Jack Daniels Old No.7 Viski', 'fiyat': 279.0}, {'tur': 'viski', 'ad': '35cl Chivas Regal (12 Yıllık) Viski', 'fiyat': 279.4}, {'tur': 'votka', 'ad': '50cl Lithuanian Vodka', 'fiyat': 280.9}, {'tur': 'raki', 'ad': '50cl Efe Yaş Üzüm Rakı', 'fiyat': 281.0}, {'tur': 'viski', 'ad': '50cl Ballantines 12 Yıl Viski', 'fiyat': 285.0}, {'tur': 'viski', 'ad': "50cl Bell's Viski", 'fiyat': 285.9}, {'tur': 'votka', 'ad': '50cl Absolut Vodka', 'fiyat': 288.0}, {'tur': 'raki', 'ad': '50cl Yeni Rakı Yeni Seri', 'fiyat': 289.0}, {'tur': 'raki', 'ad': '50cl Yeni Rakı', 'fiyat': 289.5}, {'tur': 'raki', 'ad': '50cl Efe Gold Rakı', 'fiyat': 295.0}, {'tur': 'votka', 'ad': '70cl Binboa Pier Ginger Votka', 'fiyat': 295.0}, {'tur': 'votka', 'ad': '70cl Binboa Red Orange', 'fiyat': 295.0}, {'tur': 'votka', 'ad': '50cl Binboa Votka', 'fiyat': 295.0}, {'tur': 'votka', 'ad': '70cl Binboa Red Apple', 'fiyat': 295.0}, {'tur': 'votka', 'ad': '70cl Binboa Satsuma Votka', 'fiyat': 295.0}, {'tur': 'votka', 'ad': '70cl Binboa Mojito', 'fiyat': 295.0}, {'tur': 'votka', 'ad': "70cl Gilbey's Votka", 'fiyat': 295.0}, {'tur': 'raki', 'ad': '50cl Tekirdağ Rakı Altın Seri', 'fiyat': 295.0}, {'tur': 'raki', 'ad': '50cl Saki Rakı Yaş Üzüm', 'fiyat': 295.9}, {'tur': 'raki', 'ad': '50cl Saki Rakı Altın Seri', 'fiyat': 295.9}, {'tur': 'raki', 'ad': '70cl Tayfa Rakı', 'fiyat': 299.0}, {'tur': 'raki', 'ad': '70cl Burgaz Rakı', 'fiyat': 300.0}, {'tur': 'viski', 'ad': '70cl Jack Daniels Tennessee Honey Viski', 'fiyat': 300.0}, {'tur': 'viski', 'ad': '70cl Jack Daniels Tennessee Apple Viski', 'fiyat': 300.0}, {'tur': 'cin', 'ad': '75cl Stirling Cin', 'fiyat': 300.9}, {'tur': 'raki', 'ad': '50cl Beylerbeyi Göbek Rakısı', 'fiyat': 305.0}, {'tur': 'votka', 'ad': '70cl Smirnoff North', 'fiyat': 309.0}, {'tur': 'votka', 'ad': '70cl Stumbra Centenary Vodka', 'fiyat': 310.9}, {'tur': 'viski', 'ad': '70cl Jack Daniels Special Edition Viski', 'fiyat': 320.0}, {'tur': 'raki', 'ad': '70cl Yekta Rakı', 'fiyat': 325.0}, {'tur': 'tekila', 'ad': '70cl Olmeca Blanco Tekila', 'fiyat': 325.0}, {'tur': 'tekila', 'ad': '70cl Olmeca Dark Chocolate', 'fiyat': 325.0}, {'tur': 'raki', 'ad': '70cl İzmir Rakısı', 'fiyat': 325.0}, {'tur': 'raki', 'ad': '70cl İzmir Rakısı Yaş Üzüm', 'fiyat': 330.0}, {'tur': 'viski', 'ad': '70cl Ballantines Finest Viski', 'fiyat': 330.0}, {'tur': 'likor', 'ad': '70cl Jagermeister', 'fiyat': 335.0}, {'tur': 'raki', 'ad': '70cl İzmir Rakısı Göbek', 'fiyat': 335.0}, {'tur': 'raki', 'ad': '70cl Saki Rakı Klasik', 'fiyat': 335.5}, {'tur': 'viski', 'ad': '50cl Johnnie Walker Black Label Viski', 'fiyat': 339.0}, {'tur': 'raki', 'ad': '70cl Efe Klasik Rakı', 'fiyat': 339.5}, {'tur': 'raki', 'ad': '70cl Efe 3 Distile Rakı', 'fiyat': 340.5}, {'tur': 'raki', 'ad': '50cl Saki Rakı Siyah Üzüm', 'fiyat': 345.5}, {'tur': 'votka', 'ad': '70cl Smirnoff Red', 'fiyat': 349.0}, {'tur': 'votka', 'ad': '70cl Smirnoff Espresso', 'fiyat': 359.0}, {'tur': 'votka', 'ad': '70cl Smirnoff Green Apple', 'fiyat': 359.0}, {'tur': 'votka', 'ad': '70cl Smirnoff Peppermint (Nane)', 'fiyat': 359.0}, {'tur': 'votka', 'ad': '70cl Smirnoff Citrus (Narenciye)', 'fiyat': 359.0}, {'tur': 'votka', 'ad': '70cl Smirnoff Rasberry (Ahududu)', 'fiyat': 359.0}, {'tur': 'votka', 'ad': '70cl Smirnoff Apple (Elma) Red', 'fiyat': 359.0}, {'tur': 'votka', 'ad': '70cl Smirnoff Vanilla (Vanilya)', 'fiyat': 359.0}, {'tur': 'votka', 'ad': '70cl Smirnoff Orange (Portakal)', 'fiyat': 359.0}, {'tur': 'viski', 'ad': '50cl Chivas Regal (12 Yıllık) Viski', 'fiyat': 359.0}, {'tur': 'tekila', 'ad': '70cl Olmeca Gold Tekila', 'fiyat': 360.0}, {'tur': 'viski', 'ad': "70cl Ballantine's 7 İskoç Viski", 'fiyat': 360.0}, {'tur': 'votka', 'ad': '100cl Bazooka Votka', 'fiyat': 360.0}, {'tur': 'raki', 'ad': '70cl Yeni Rakı Yeni Seri', 'fiyat': 369.0}, {'tur': 'votka', 'ad': '100cl İstanblue Votka', 'fiyat': 370.0}, {'tur': 'raki', 'ad': '70cl Efe Yaş Üzüm Rakı', 'fiyat': 373.0}, {'tur': 'cin', 'ad': "70cl Gilbey's Cin", 'fiyat': 375.0}, {'tur': 'raki', 'ad': '70cl Tekirdağ Rakı', 'fiyat': 375.5}, {'tur': 'raki', 'ad': '70cl Saki Rakı Yaş Üzüm', 'fiyat': 375.5}, {'tur': 'raki', 'ad': '70cl Tekirdağ Rakı Trakya Serisi', 'fiyat': 375.5}, {'tur': 'votka', 'ad': '70cl Absolut Vodka Mandrin', 'fiyat': 377.0}, {'tur': 'votka', 'ad': '70cl Absolut Vodka Vanilia', 'fiyat': 377.0}, {'tur': 'votka', 'ad': '70cl Absolut Vodka Raspberri', 'fiyat': 377.0}, {'tur': 'votka', 'ad': '70cl Absolut Extrakt Vodka', 'fiyat': 377.0}, {'tur': 'votka', 'ad': '70cl Absolut Vodka', 'fiyat': 377.0}, {'tur': 'votka', 'ad': '70cl Absolut Lime Vodka', 'fiyat': 377.0}, {'tur': 'votka', 'ad': '70cl Absolut Vodka Apeach', 'fiyat': 377.0}, {'tur': 'votka', 'ad': '70cl Absolut Citron Vodka', 'fiyat': 377.0}, {'tur': 'votka', 'ad': '70cl Absolut Pears Vodka', 'fiyat': 377.0}, {'tur': 'raki', 'ad': '70cl Yeni Rakı', 'fiyat': 379.5}, {'tur': 'viski', 'ad': '70cl Jack Daniels Old No.7 Viski', 'fiyat': 380.0}, {'tur': 'viski', 'ad': '50cl J&B Viski', 'fiyat': 380.0}, {'tur': 'viski', 'ad': '50cl Johnnie Walker Red Label Viski', 'fiyat': 380.0}, {'tur': 'likor', 'ad': '35cl Cointreau Likör', 'fiyat': 381.0}, {'tur': 'votka', 'ad': '100cl Wyborowa Votka', 'fiyat': 385.0}, {'tur': 'viski', 'ad': '70cl Ballantines 12 Yıl Viski', 'fiyat': 390.0}, {'tur': 'cin', 'ad': '70cl Beefeater Pink Cin', 'fiyat': 395.0}, {'tur': 'raki', 'ad': '70cl Saki Rakı Altın Seri', 'fiyat': 395.9}, {'tur': 'cin', 'ad': '70cl Beefeater Cin', 'fiyat': 396.0}, {'tur': 'viski', 'ad': "70cl Bell's Viski", 'fiyat': 399.0}, {'tur': 'cin', 'ad': "70cl Gordon's Dry Cin", 'fiyat': 399.0}, {'tur': 'raki', 'ad': '70cl Efe Gold Rakı', 'fiyat': 399.0}, {'tur': 'raki', 'ad': '70cl Tekirdağ Rakı Altın Seri', 'fiyat': 399.0}, {'tur': 'raki', 'ad': '70cl Tekirdağ Rakı Kavrulmuş Anason', 'fiyat': 400.0}, {'tur': 'votka', 'ad': '100cl Lithuanian Vodka', 'fiyat': 400.9}, {'tur': 'viski', 'ad': '100cl Jack Daniels Tennessee Honey Viski', 'fiyat': 405.0}, {'tur': 'viski', 'ad': '100cl Jack Daniels Tennessee Apple Viski', 'fiyat': 405.0}, {'tur': 'raki', 'ad': '70cl Yeni Rakı Ustaların Karışımı', 'fiyat': 409.0}, {'tur': 'raki', 'ad': '100cl Tayfa Rakı', 'fiyat': 410.5}, {'tur': 'raki', 'ad': '70cl Efe Tek İmbik Rakı', 'fiyat': 415.0}, {'tur': 'votka', 'ad': '70cl Binboa Votka', 'fiyat': 419.0}, {'tur': 'cin', 'ad': '100cl Stirling Cin', 'fiyat': 419.9}, {'tur': 'votka', 'ad': "100cl Gilbey's Votka", 'fiyat': 420.0}, {'tur': 'raki', 'ad': '70cl Efe Geleneksel Rakı', 'fiyat': 420.5}, {'tur': 'raki', 'ad': '70cl Efe Çilingir Rakı', 'fiyat': 425.5}, {'tur': 'raki', 'ad': '70cl Beylerbeyi Göbek Rakısı', 'fiyat': 429.0}, {'tur': 'raki', 'ad': '70cl Kulüp Rakı', 'fiyat': 430.0}, {'tur': 'raki', 'ad': '70cl Yeni Rakı Âlâ', 'fiyat': 435.0}, {'tur': 'votka', 'ad': '100cl Stumbra Centenary Vodka', 'fiyat': 435.9}, {'tur': 'tekila', 'ad': '70cl Olmeca Altos Plata Tekila', 'fiyat': 440.0}, {'tur': 'raki', 'ad': '70cl Efe Çilingir Xtra Rakı', 'fiyat': 440.9}, {'tur': 'raki', 'ad': '100cl Saki Rakı Klasik', 'fiyat': 440.9}, {'tur': 'raki', 'ad': '70cl Saki Rakı Siyah Üzüm', 'fiyat': 445.5}, {'tur': 'viski', 'ad': '70cl Johnnie Walker Black Label Viski', 'fiyat': 449.0}, {'tur': 'raki', 'ad': '100cl İzmir Rakısı', 'fiyat': 449.5}, {'tur': 'raki', 'ad': '70cl Efe Çilingir Xtra Yaş Üzüm Rakı', 'fiyat': 449.9}, {'tur': 'tekila', 'ad': '70cl Olmeca Altos Reposadd', 'fiyat': 450.0}, {'tur': 'raki', 'ad': '100cl Yekta Rakı', 'fiyat': 450.5}, {'tur': 'likor', 'ad': '100cl Jagermeister', 'fiyat': 452.5}, {'tur': 'viski', 'ad': '100cl Ballantines Finest Viski', 'fiyat': 455.0}, {'tur': 'tekila', 'ad': '100cl Olmeca Blanco Tekila', 'fiyat': 455.0}, {'tur': 'raki', 'ad': '100cl İzmir Rakısı Yaş Üzüm', 'fiyat': 459.5}, {'tur': 'raki', 'ad': '70cl Altınbaş Rakı', 'fiyat': 460.0}, {'tur': 'raki', 'ad': '70cl Efe Sarı Zeybek Rakı', 'fiyat': 469.5}, {'tur': 'cin', 'ad': "70cl Gordon's Pink Cin", 'fiyat': 475.0}, {'tur': 'raki', 'ad': '100cl Efe Klasik Rakı', 'fiyat': 475.5}, {'tur': 'viski', 'ad': '70cl Chivas Regal (12 Yıl) Viski', 'fiyat': 479.0}, {'tur': 'cin', 'ad': "100cl Gilbey's Cin", 'fiyat': 481.0}, {'tur': 'viski', 'ad': '70cl Chivas Regal (13 Yıllık) İskoç Viskisi', 'fiyat': 490.0}, {'tur': 'viski', 'ad': '70cl Jack Daniels Single Barrel Viski', 'fiyat': 495.0}, {'tur': 'votka', 'ad': '100cl Smirnoff Red', 'fiyat': 499.0}, {'tur': 'raki', 'ad': '100cl Yeni Rakı', 'fiyat': 499.5}, {'tur': 'raki', 'ad': '100cl Yeni Rakı Yeni Seri', 'fiyat': 499.5}, {'tur': 'viski', 'ad': '70cl J&B Viski', 'fiyat': 500.0}, {'tur': 'viski', 'ad': '70cl Johnnie Walker Red Label Viski', 'fiyat': 500.0}, {'tur': 'raki', 'ad': '100cl Efe Yaş Üzüm Rakı', 'fiyat': 504.5}, {'tur': 'viski', 'ad': '100cl Jack Daniels Old No.7 Viski', 'fiyat': 515.0}, {'tur': 'raki', 'ad': '100cl Tekirdağ Rakı', 'fiyat': 519.0}, {'tur': 'votka', 'ad': '100cl Absolut Vodka', 'fiyat': 525.0}, {'tur': 'raki', 'ad': '100cl Saki Rakı Yaş Üzüm', 'fiyat': 525.9}, {'tur': 'raki', 'ad': '70cl Tekirdağ Rakı No. 10', 'fiyat': 529.0}, {'tur': 'cin', 'ad': '70cl Malfy Con Limone', 'fiyat': 535.0}, {'tur': 'cin', 'ad': '70cl Malfy Gın Rose', 'fiyat': 535.0}, {'tur': 'cin', 'ad': '70cl Malfy Originale Cin', 'fiyat': 535.0}, {'tur': 'viski', 'ad': '100cl Ballantines 12 Yıl Viski', 'fiyat': 540.0}, {'tur': 'raki', 'ad': '100cl Tekirdağ Rakı Altın Seri', 'fiyat': 549.5}, {'tur': 'raki', 'ad': '100cl Efe Gold Rakı', 'fiyat': 549.5}, {'tur': 'raki', 'ad': '100cl Saki Rakı Altın Seri', 'fiyat': 549.9}, {'tur': 'viski', 'ad': "100cl Bell's Viski", 'fiyat': 550.5}, {'tur': 'raki', 'ad': '100cl Beylerbeyi Göbek Rakısı', 'fiyat': 569.0}, {'tur': 'raki', 'ad': '100cl Efe Çilingir Rakı', 'fiyat': 579.5}, {'tur': 'raki', 'ad': '100cl Efe Tek İmbik Rakı', 'fiyat': 580.5}, {'tur': 'cin', 'ad': '70cl Tanqueray Cin (London Dry Gin)', 'fiyat': 583.0}, {'tur': 'tekila', 'ad': '70cl Avion Silver', 'fiyat': 600.0}, {'tur': 'cin', 'ad': '70cl Tanqueray Flor De Sevilla Cin', 'fiyat': 625.0}, {'tur': 'viski', 'ad': '100cl Johnnie Walker Black Label Viski', 'fiyat': 639.0}, {'tur': 'viski', 'ad': '70cl Chivas Regal (15 Yıllık) Viski', 'fiyat': 649.0}, {'tur': 'tekila', 'ad': '70cl Avion Reposadd', 'fiyat': 650.0}, {'tur': 'viski', 'ad': '70cl Johnnie Walker Double Black Viski', 'fiyat': 650.0}, {'tur': 'viski', 'ad': "70cl Ballantine's 17 İskoç Viski", 'fiyat': 660.0}, {'tur': 'viski', 'ad': '150cl Ballantines Finest Viski', 'fiyat': 685.0}, {'tur': 'viski', 'ad': '100cl Chivas Regal (12 Yıl) Viski', 'fiyat': 690.0}, {'tur': 'viski', 'ad': '175cl Jack Daniels Old No.7 Viski', 'fiyat': 695.0}, {'tur': 'viski', 'ad': '100cl Johnnie Walker Red Label Viski', 'fiyat': 699.0}, {'tur': 'viski', 'ad': '100cl J&B Viski', 'fiyat': 699.0}, {'tur': 'viski', 'ad': '70cl Johnnie Walker Gold Label Reserve Viski', 'fiyat': 699.0}, {'tur': 'likor', 'ad': '50cl Cointreau Likör', 'fiyat': 700.0}, {'tur': 'cin', 'ad': '100cl Bombay Sapphire Cin', 'fiyat': 720.0}, {'tur': 'viski', 'ad': '50cl Chivas Regal (18 Yıllık) Viski', 'fiyat': 750.0}, {'tur': 'tekila', 'ad': '70cl Don Julio Tequila', 'fiyat': 750.0}, {'tur': 'cin', 'ad': '70cl Tanqueray No: 10 Cin', 'fiyat': 760.0}, {'tur': 'raki', 'ad': '150cl Yeni Rakı', 'fiyat': 799.0}, {'tur': 'viski', 'ad': '70cl Jack Daniels No.27 Gold Viski', 'fiyat': 800.0}, {'tur': 'raki', 'ad': '100cl Efe Geleneksel Rakı', 'fiyat': 807.0}, {'tur': 'raki', 'ad': '70cl Efe Organik Rakı', 'fiyat': 840.5}, {'tur': 'raki', 'ad': '100cl Efe Çilingir Xtra Rakı', 'fiyat': 849.5}, {'tur': 'votka', 'ad': '70cl Absolut Elyx Vodka', 'fiyat': 860.0}, {'tur': 'viski', 'ad': '150cl J&B Viski', 'fiyat': 875.0}, {'tur': 'raki', 'ad': '70cl Efe 5 Yıllık Rakı', 'fiyat': 895.0}, {'tur': 'viski', 'ad': '70cl Chivas Mizunara İskoç Viskisi', 'fiyat': 940.0}, {'tur': 'likor', 'ad': '100cl Cointreau Likör', 'fiyat': 951.0}, {'tur': 'viski', 'ad': '70cl Johnnie Walker Green Label 15 Yıllık Viski', 'fiyat': 980.0}, {'tur': 'votka', 'ad': '175cl Absolut Vodka', 'fiyat': 985.0}, {'tur': 'viski', 'ad': '150cl Johnnie Walker Black Label Viski', 'fiyat': 995.0}, {'tur': 'viski', 'ad': '70cl Chivas Regal (18 Yıllık) Viski', 'fiyat': 1000.0}, {'tur': 'viski', 'ad': '70cl Johnnie Walker 18 Yıllık Viski', 'fiyat': 1050.0}, {'tur': 'viski', 'ad': '150cl Johnnie Walker Red Label Viski', 'fiyat': 1075.0}, {'tur': 'viski', 'ad': '300cl Jack Daniels Old No.7 Viski', 'fiyat': 1175.0}, {'tur': 'viski', 'ad': '70cl Ballantines 21 Yıl Viski', 'fiyat': 1250.0}, {'tur': 'raki', 'ad': '70cl Saki Rakı Premium', 'fiyat': 1250.0}, {'tur': 'viski', 'ad': '175cl Chivas Regal (12 Yıl) Viski', 'fiyat': 1250.0}, {'tur': 'viski', 'ad': '100cl Jack Daniels Sinatra Select Viski', 'fiyat': 1300.0}, {'tur': 'viski', 'ad': '300cl Ballantines Finest Viski', 'fiyat': 1600.0}, {'tur': 'viski', 'ad': '300cl Chivas Regal (12 Yıllık) Viski', 'fiyat': 1850.0}, {'tur': 'votka', 'ad': '150cl Absolut Elyx Vodka', 'fiyat': 1860.0}, {'tur': 'viski', 'ad': '300cl Johnnie Walker Black Label Viski', 'fiyat': 1929.0}, {'tur': 'viski', 'ad': '70cl Chivas Regal Royal Salute 21 İskoç Viskisi', 'fiyat': 2150.0}, {'tur': 'viski', 'ad': '300cl Johnnie Walker Red Label Viski', 'fiyat': 2200.0}, {'tur': 'viski', 'ad': '300cl Chivas Regal (12 Yıllık)', 'fiyat': 2229.0}, {'tur': 'votka', 'ad': '450cl Absolut Vodka Blue', 'fiyat': 2725.0}, {'tur': 'tekila', 'ad': '70cl Don Julio 1942 Tequila', 'fiyat': 3000.0}, {'tur': 'votka', 'ad': '300cl Absolut Elyx Vodka', 'fiyat': 3650.0}, {'tur': 'viski', 'ad': '70cl Johnnie Walker Blue Label Viski', 'fiyat': 4000.0}, {'tur': 'viski', 'ad': '70cl Chivas Regal (25 Yıllık) Viski', 'fiyat': 4990.0}, {'tur': 'votka', 'ad': '450cl Absolut Elyx Vodka', 'fiyat': 6000.0}, {'tur': 'viski', 'ad': '70cl Johnnie Walker Sons King George V Viski', 'fiyat': 7000.0}]}
  """

  for urun in piiz.nesne:
    print(urun.ad)
  """
  json verisini python nesnesine dönüştürür.

    33cl Bud Depozitosuz Şişe
    25cl Efes Malt Depozitosuz Şişe
    45cl Varım Kutu
    45cl Varım Limonlu Kutu
    23,7cl Tuborg Kırmızı Shot Special Kutu
    50cl Bud Kutu Şişe
    50cl Bud Depozitosuz Şişe
    33cl Tuborg Gold Depozitosuz Şişe
    33cl Tuborg Gold Kutu
    33cl Tuborg Amber Depozitosuz Şişe
    33cl Efes Pilsen Kutu
    33cl Carlsberg Kutu
    33cl Bomonti Red Ale Depozitosuz Şişe
    33cl Bomonti Black Depozitosuz Şişe
    33cl Miller Depozitosuz Şişe
    33cl Bomonti İpa Depozitosuz Şişe
    50cl Carlsberg Kutu
    33cl Carlsberg Depozitosuz Şişe
    50cl Tuborg Gold Depozitolu Şişe
    50cl Efes Malt Depozitolu Şişe
    35cl Frederic Marzen Lager Şişe
    35cl Frederic India Pale Ale Şişe
    35cl Frederic Brown Ale Şişe
    35cl Frederic White Ipa Şişe
    50cl Carlsberg Depozitolu Şişe
    33cl Grimbergen Blonde Depozitosuz Şişe
    33cl Kronenbourg 1664 Blanc Depozitosuz Şişe
    33cl SOL Cerveza Depozitosuz Şişe
    33cl Weihenstephan Depozitosuz Şişe
    33cl Beck's Depozitosuz Şişe
    50cl Bomonti Depozitolu Şişe
    50cl Tuborg Gold Kutu
    50cl Bomonti Depozitosuz Şişe
    50cl Tuborg Amber Kutu
    50cl Tuborg Gold Depozitosuz Şişe
    50cl Efes Malt Kutu
    50cl Efes Extra Kutu
    50cl Efes Pilsen Kutu
    33cl Efes Brewmaster Red Ale Depozitosuz Şişe
    50cl Tuborg Amber Depozitosuz Şişe
    50cl Efes Pilsen Depozitolu Uzun Şişe
    33cl Efes Brewmaster White Ale Depozitosuz Şişe
    50cl Bomonti Filtresiz Depozitosuz Şişe
    50cl Tuborg Filtresiz Kutu
    50cl Tuborg Filtresiz Depozitosuz Şişe
    33cl Grimbergen Double Ambree Depozitosuz Şişe
    33cl Desperados Depozitosuz Şişe
    50cl Bomonti Filtresiz Kutu
    50cl Tuborg Kırmızı Special Kutu
    50cl Beck's Depozitosuz Şişe
    50cl Beck's Kutu
    50cl Efes Pilsen Özel Seri Depozitosuz
    33cl Weihenstephan Vitus Depozitosuz Şişe
    50cl Miller Kutu
    50cl Miller Depozitosuz Şişe
    Efes Glutensiz 50cl
    50cl Efes Fıçı Yüksek Alkollü Kutu
    50cl Efes Fıçı Yüksek Alkollü Şişe Depozitosuz
    75cl Sevilen Agora Beyaz Şarap
    35,5cl Corona Extra Şişe
    100cl Skol Bira Depozitosuz Pet Şişe
    44cl Guinness Kutu
    75cl Agora Kırmızı Şarap (Sevilen)
    75cl Sevilen Altıntepe Kırmızı Şarap
    33cl Hoegaarden Depozitosuz Şişe
    33cl Erdinger Depozitosuz Şişe
    50cl Amsterdam Navigator Depozitosuz Şişe
    50cl Amsterdam Navigator Kutu
    75cl Sevilen Kalecik Karası Kırmızı Şarap
    75cl Sevilen Majestik Gamay Kırmızı Şarap
    75cl Sevilen Sultaniye Beyaz Şarap
    33cl Leffe Brune Blonde Depozitosuz Şişe
    100cl Marmara Gold Depozitosuz Şişe
    33cl Leffe Brune Depozitosuz Şişe
    75cl Sevilen Majestik Öküzgözü Kırmızı
    75cl Sevilen Majestik Gamay Kırmızı Şarap
    33cl Leffe Radieuse Depozitosuz Şişe
    14.4 Çilekli Volim
    14.4 Volim Redbull
    14.4 Volim Limonlu Alkol
    Volim Sade
    Volim Karışık Meyveli
    Volim Karpuz Aromalı
    Volim Kola Aromalı
    Volim Shot Karpuz Çilek
    Volim Shot Votka İçeçeği
    Volim Enerji İçeceği Aromalı
    18,75cl Villa Doluca Şarap
    45cl Grolsch Depozitosuz Şişe
    33cl Duvel Depozitosuz Şişe
    75cl Biricik Sek Beyaz Cam Şarap
    75cl Biricik Sek Kırmızı CamŞarap
    75cl Biricik Sek Kırmızı Cam Şarap
    75cl Biricik Sek Beyaz Cam Şarap
    20cl Saki Rakı Yaş Üzüm
    75cl Sevilen İsabey Saublanc (Beyaz)
    75cl Sevilen İsabey Merlot Şarap
    75cl Sevilen İsabey Narince Beyaz Şarap
    75cl Sevilen İsabey Cabarnet
    100cl Biricik Sek Kırmızı Cam Şarap
    100cl Biricik Sek Kırmızı Cam Şarap
    100cl Biricik Sek Beyaz Cam Şarap
    75cl Mistik Şarap
    100cl Biricik Sek Beyaz Cam Şarap
    37,5cl Villa Doluca Şarap
    37,5cl Doluca Şarap
    35cl Saki Ginseng
    20cl İstanblue Votka
    50cl Hare Nane Likörü
    50cl Hare Acıbadem Likörü
    50cl Hare Muz Likörü
    50cl Hare Vişne Likörü
    50cl Hare Hindistan Cevizi Likörü
    75cl Crama Regala Sauvignon Blanc
    75cl Crama Regala Chardonnay
    75cl Crama Regala Merlot
    75cl Crama Regala Cabernet Sauvignon
    Biricik Sek Kırmızı-Beyaz-Rose Şarap
    50cl Hare Portakal Likörü
    150cl Biricik Galon Kırmızı Cam Şarap
    Biricik Sek Kırmızı-Beyaz-Blush Şarap
    150cl Biricik Galon Beyaz Cam Şarap
    150cl Biricik Galon Kırmızı Cam Şarap
    150cl Biricik Galon Beyaz Cam Şarap
    100cl Hare Kahve, Portakal, Kayısı Likörü
    100cl Hare Çikolata Likörü
    100cl Hare Acıbadem, Bitter, Nane Likörü
    100cl Hare Şeftali, Muz, Tropikal Likörü
    75cl Dlc Sultaniye Emir Şarap
    75cl Dlc Shiraz Şarap
    75cl Dlc Cab. Sauvıgnon-Merlot Şarap
    75cl Dlc Moskado Şarap
    75cl Dlc Kalecik Karası Şarap
    75cl Dlc Öküzgözü Şarap
    75cl Dlc Boğazkere Şarap
    75cl Dlc Sauvıgnon Blanc Şarap
    75cl Dlc Frenache Şarap
    75cl Dlc Narince Şarap
    75cl Doluca Şarap
    35cl Anadolu Boğma Rakı
    35cl Muz Likörü
    150cl Biricik Kulplu Kırmızı Şarap
    150cl Biricik Kulplu Beyaz Şarap
    35cl Portakal Likörü
    35cl Nane Likörü
    35cl Acıbadem Likörü
    35cl Ahududu Likörü
    35cl Vişne Likörü
    35cl Damla Sakızlı Likör
    35cl Bazooka Votka
    100cl Mistik Şarap
    35cl İstanblue Votka
    35cl Ata Rakı
    75cl Villa Doluca Şarap
    20cl Lithuanian Vodka
    20cl Saki Rakı Klasik
    35cl Yekta Rakı
    35cl Burgaz Rakı
    35cl Wyborowa Votka
    75cl Villa Doluca Neo Şarap
    200cl Biricik Galon Beyaz Cam Şarap
    200cl Biricik Galon Kırmızı Cam Şarap
    20cl Saki Rakı Altın Seri
    35cl Gilbey's Cin
    35cl Tayfa Rakı
    35cl Gilbey's Votka
    35cl Stirling Cin
    35cl Jack Daniels Tennessee Honey Viski
    35cl Jack Daniels Tennessee Apple Viski
    70cl Saki Ginseng
    100cl Doluca Şarap
    35cl İzmir Rakısı
    35cl Olmeca Blanco Tekila
    35cl Binboa Votka
    35cl Stumbra Centenary Vodka
    35cl Ballantines Finest Viski
    35cl Saki Rakı Klasik
    35cl İzmir Rakısı Yaş Üzüm
    35cl Yeni Rakı
    20cl Chivas Regal (12 Yıllık) Viski
    100cl Volim
    35cl İzmir Rakısı Göbek
    35cl Smirnoff Red Votka
    35cl Olmeca Gold Tekila
    50cl Bazooka Votka
    Kırbıyık Kokteyl Mojito 100cl
    Kırbıyık Kokteyl Cosmopolitan 100cl
    Kırbıyık Kokteyl Sek On The Beach 100cl
    Kırbıyık Kokteyl Orman Meyveli 100cl
    Kırbıyık Kokteyl Margarita 100cl
    Bue Hawaii 100cl
    Kırbıyık Kokteyl Kavun 100cl
    Kırbıyık Kokteyl Karpuz Çilek 100cl
    Harrley's Irish Cream 100cl
    100cl Hare Portakal Likörü
    70cl El Jimador Blanco Tequila
    50cl İstanblue Votka
    20cl Saki Rakı Siyah Üzüm
    35cl Yeni Rakı Yeni Seri
    35cl Tekirdağ Rakı
    35cl Gordon's Dry Cin
    35cl Saki Rakı Altın Seri
    35cl Tekirdağ Rakı Trakya Serisi
    35cl Lithuanian Vodka
    35cl Efe Yaş Üzüm Rakı
    35cl Tekirdağ Rakı Kavrulmuş Anason
    35cl Saki Rakı Yaş Üzüm
    35cl Ballantines 12 Yıl Viski
    50cl Wyborowa Votka
    35cl Jack Daniels Old No.7 Viski
    35cl Tekirdağ Rakı Altın Seri
    35cl Absolut Vodka
    35cl Efe Gold Rakı
    70cl El Jimador Reposado Tequila
    35cl Beefeater Cin
    100cl Garrone Ricard Likör
    35cl Yeni Rakı Ustaların Karışımı
    35cl Bell's Viski
    50cl Tayfa Rakı
    35cl Efe Çilingir Xtra Rakı
    100cl Garrone Rosso Likör
    35cl Jagermeister
    100cl Garrone Bianco Dry Likör
    50cl Stumbra Centenary Vodka
    35cl Efe Tek İmbik Rakı
    35cl Yeni Rakı Âlâ
    50cl Burgaz Rakı
    35cl Kulüp Rakı
    50cl Stirling Cin
    150cl Mistik Şarap
    50cl Olmeca Blanco Tekila
    70cl Anadolu Boğma Rakı
    35cl Beylerbeyi Göbek Rakısı
    50cl İzmir Rakısı
    300cl Biricik Kulplu Beyaz Şarap
    Biricik Suni Yarı Köpüren Şarap (Beyaz-Rose)
    35cl Altınbaş Rakı
    300cl Biricik Kulplu Kırmızı Şarap
    50cl Ballantines Finest Viski
    50cl İzmir Rakısı Yaş Üzüm
    35cl J&B Viski
    35cl Johnnie Walker Black Label Viski
    35cl Saki Rakı Siyah Üzüm
    35cl Efe Klasik Rakı
    50cl Smirnoff Red
    50cl Efe Klasik Rakı
    35cl Efe Çilingir Xtra Yaş Üzüm Rakı
    35cl Efe 3 Distile Rakı
    35cl Efe Geleneksel Rakı
    50cl Saki Rakı Klasik
    35cl Efe Çilingir Rakı
    35cl Efe Sarı Zeybek Rakı
    70cl Bazooka Votka
    70cl İstanblue Votka
    70cl Lithuanian Vodka
    70cl Ata Rakı
    50cl Tekirdağ Rakı
    70cl Wyborowa Votka
    35cl Johnnie Walker Red Label Viski
    50cl Jack Daniels Old No.7 Viski
    35cl Chivas Regal (12 Yıllık) Viski
    50cl Lithuanian Vodka
    50cl Efe Yaş Üzüm Rakı
    50cl Ballantines 12 Yıl Viski
    50cl Bell's Viski
    50cl Absolut Vodka
    50cl Yeni Rakı Yeni Seri
    50cl Yeni Rakı
    50cl Efe Gold Rakı
    70cl Binboa Pier Ginger Votka
    70cl Binboa Red Orange
    50cl Binboa Votka
    70cl Binboa Red Apple
    70cl Binboa Satsuma Votka
    70cl Binboa Mojito
    70cl Gilbey's Votka
    50cl Tekirdağ Rakı Altın Seri
    50cl Saki Rakı Yaş Üzüm
    50cl Saki Rakı Altın Seri
    70cl Tayfa Rakı
    70cl Burgaz Rakı
    70cl Jack Daniels Tennessee Honey Viski
    70cl Jack Daniels Tennessee Apple Viski
    75cl Stirling Cin
    50cl Beylerbeyi Göbek Rakısı
    70cl Smirnoff North
    70cl Stumbra Centenary Vodka
    70cl Jack Daniels Special Edition Viski
    70cl Yekta Rakı
    70cl Olmeca Blanco Tekila
    70cl Olmeca Dark Chocolate
    70cl İzmir Rakısı
    70cl İzmir Rakısı Yaş Üzüm
    70cl Ballantines Finest Viski
    70cl Jagermeister
    70cl İzmir Rakısı Göbek
    70cl Saki Rakı Klasik
    50cl Johnnie Walker Black Label Viski
    70cl Efe Klasik Rakı
    70cl Efe 3 Distile Rakı
    50cl Saki Rakı Siyah Üzüm
    70cl Smirnoff Red
    70cl Smirnoff Espresso
    70cl Smirnoff Green Apple
    70cl Smirnoff Peppermint (Nane)
    70cl Smirnoff Citrus (Narenciye)
    70cl Smirnoff Rasberry (Ahududu)
    70cl Smirnoff Apple (Elma) Red
    70cl Smirnoff Vanilla (Vanilya)
    70cl Smirnoff Orange (Portakal)
    50cl Chivas Regal (12 Yıllık) Viski
    70cl Olmeca Gold Tekila
    70cl Ballantine's 7 İskoç Viski
    100cl Bazooka Votka
    70cl Yeni Rakı Yeni Seri
    100cl İstanblue Votka
    70cl Efe Yaş Üzüm Rakı
    70cl Gilbey's Cin
    70cl Tekirdağ Rakı
    70cl Saki Rakı Yaş Üzüm
    70cl Tekirdağ Rakı Trakya Serisi
    70cl Absolut Vodka Mandrin
    70cl Absolut Vodka Vanilia
    70cl Absolut Vodka Raspberri
    70cl Absolut Extrakt Vodka
    70cl Absolut Vodka
    70cl Absolut Lime Vodka
    70cl Absolut Vodka Apeach
    70cl Absolut Citron Vodka
    70cl Absolut Pears Vodka
    70cl Yeni Rakı
    70cl Jack Daniels Old No.7 Viski
    50cl J&B Viski
    50cl Johnnie Walker Red Label Viski
    35cl Cointreau Likör
    100cl Wyborowa Votka
    70cl Ballantines 12 Yıl Viski
    70cl Beefeater Pink Cin
    70cl Saki Rakı Altın Seri
    70cl Beefeater Cin
    70cl Bell's Viski
    70cl Gordon's Dry Cin
    70cl Efe Gold Rakı
    70cl Tekirdağ Rakı Altın Seri
    70cl Tekirdağ Rakı Kavrulmuş Anason
    100cl Lithuanian Vodka
    100cl Jack Daniels Tennessee Honey Viski
    100cl Jack Daniels Tennessee Apple Viski
    70cl Yeni Rakı Ustaların Karışımı
    100cl Tayfa Rakı
    70cl Efe Tek İmbik Rakı
    70cl Binboa Votka
    100cl Stirling Cin
    100cl Gilbey's Votka
    70cl Efe Geleneksel Rakı
    70cl Efe Çilingir Rakı
    70cl Beylerbeyi Göbek Rakısı
    70cl Kulüp Rakı
    70cl Yeni Rakı Âlâ
    100cl Stumbra Centenary Vodka
    70cl Olmeca Altos Plata Tekila
    70cl Efe Çilingir Xtra Rakı
    100cl Saki Rakı Klasik
    70cl Saki Rakı Siyah Üzüm
    70cl Johnnie Walker Black Label Viski
    100cl İzmir Rakısı
    70cl Efe Çilingir Xtra Yaş Üzüm Rakı
    70cl Olmeca Altos Reposadd
    100cl Yekta Rakı
    100cl Jagermeister
    100cl Ballantines Finest Viski
    100cl Olmeca Blanco Tekila
    100cl İzmir Rakısı Yaş Üzüm
    70cl Altınbaş Rakı
    70cl Efe Sarı Zeybek Rakı
    70cl Gordon's Pink Cin
    100cl Efe Klasik Rakı
    70cl Chivas Regal (12 Yıl) Viski
    100cl Gilbey's Cin
    70cl Chivas Regal (13 Yıllık) İskoç Viskisi
    70cl Jack Daniels Single Barrel Viski
    100cl Smirnoff Red
    100cl Yeni Rakı
    100cl Yeni Rakı Yeni Seri
    70cl J&B Viski
    70cl Johnnie Walker Red Label Viski
    100cl Efe Yaş Üzüm Rakı
    100cl Jack Daniels Old No.7 Viski
    100cl Tekirdağ Rakı
    100cl Absolut Vodka
    100cl Saki Rakı Yaş Üzüm
    70cl Tekirdağ Rakı No. 10
    70cl Malfy Con Limone
    70cl Malfy Gın Rose
    70cl Malfy Originale Cin
    100cl Ballantines 12 Yıl Viski
    100cl Tekirdağ Rakı Altın Seri
    100cl Efe Gold Rakı
    100cl Saki Rakı Altın Seri
    100cl Bell's Viski
    100cl Beylerbeyi Göbek Rakısı
    100cl Efe Çilingir Rakı
    100cl Efe Tek İmbik Rakı
    70cl Tanqueray Cin (London Dry Gin)
    70cl Avion Silver
    70cl Tanqueray Flor De Sevilla Cin
    100cl Johnnie Walker Black Label Viski
    70cl Chivas Regal (15 Yıllık) Viski
    70cl Avion Reposadd
    70cl Johnnie Walker Double Black Viski
    70cl Ballantine's 17 İskoç Viski
    150cl Ballantines Finest Viski
    100cl Chivas Regal (12 Yıl) Viski
    175cl Jack Daniels Old No.7 Viski
    100cl Johnnie Walker Red Label Viski
    100cl J&B Viski
    70cl Johnnie Walker Gold Label Reserve Viski
    50cl Cointreau Likör
    100cl Bombay Sapphire Cin
    50cl Chivas Regal (18 Yıllık) Viski
    70cl Don Julio Tequila
    70cl Tanqueray No: 10 Cin
    150cl Yeni Rakı
    70cl Jack Daniels No.27 Gold Viski
    100cl Efe Geleneksel Rakı
    70cl Efe Organik Rakı
    100cl Efe Çilingir Xtra Rakı
    70cl Absolut Elyx Vodka
    150cl J&B Viski
    70cl Efe 5 Yıllık Rakı
    70cl Chivas Mizunara İskoç Viskisi
    100cl Cointreau Likör
    70cl Johnnie Walker Green Label 15 Yıllık Viski
    175cl Absolut Vodka
    150cl Johnnie Walker Black Label Viski
    70cl Chivas Regal (18 Yıllık) Viski
    70cl Johnnie Walker 18 Yıllık Viski
    150cl Johnnie Walker Red Label Viski
    300cl Jack Daniels Old No.7 Viski
    70cl Ballantines 21 Yıl Viski
    70cl Saki Rakı Premium
    175cl Chivas Regal (12 Yıl) Viski
    100cl Jack Daniels Sinatra Select Viski
    300cl Ballantines Finest Viski
    300cl Chivas Regal (12 Yıllık) Viski
    150cl Absolut Elyx Vodka
    300cl Johnnie Walker Black Label Viski
    70cl Chivas Regal Royal Salute 21 İskoç Viskisi
    300cl Johnnie Walker Red Label Viski
    300cl Chivas Regal (12 Yıllık)
    450cl Absolut Vodka Blue
    70cl Don Julio 1942 Tequila
    300cl Absolut Elyx Vodka
    70cl Johnnie Walker Blue Label Viski
    70cl Chivas Regal (25 Yıllık) Viski
    450cl Absolut Elyx Vodka
    70cl Johnnie Walker Sons King George V Viski
  """


  print(piiz.gorsel())
  """
  oluşan json verisini insanın okuyabileceği formatta döndürür.

    {
    "kaynak": "piizapp.com",
    "veri": [
        {
        "tur": "bira",
        "ad": "33cl Bud Depozitosuz Şişe",
        "fiyat": 21.0
        },
        {
        "tur": "bira",
        "ad": "25cl Efes Malt Depozitosuz Şişe",
        "fiyat": 21.0
        },
        {
        "tur": "bira",
        "ad": "45cl Varım Kutu",
        "fiyat": 22.0
        },
        {
        "tur": "bira",
        "ad": "45cl Varım Limonlu Kutu",
        "fiyat": 22.0
        },
        {
        "tur": "bira",
        "ad": "23,7cl Tuborg Kırmızı Shot Special Kutu",
        "fiyat": 22.5
        },
        {
        "tur": "bira",
        "ad": "50cl Bud Kutu Şişe",
        "fiyat": 23.0
        },
        {
        "tur": "bira",
        "ad": "50cl Bud Depozitosuz Şişe",
        "fiyat": 23.0
        },
        {
        "tur": "bira",
        "ad": "33cl Tuborg Gold Depozitosuz Şişe",
        "fiyat": 23.5
        },
        {
        "tur": "bira",
        "ad": "33cl Tuborg Gold Kutu",
        "fiyat": 23.5
        },
        {
        "tur": "bira",
        "ad": "33cl Tuborg Amber Depozitosuz Şişe",
        "fiyat": 23.5
        },
        {
        "tur": "bira",
        "ad": "33cl Efes Pilsen Kutu",
        "fiyat": 25.0
        },
        {
        "tur": "bira",
        "ad": "33cl Carlsberg Kutu",
        "fiyat": 25.5
        },
        {
        "tur": "bira",
        "ad": "33cl Bomonti Red Ale Depozitosuz Şişe",
        "fiyat": 26.0
        },
        {
        "tur": "bira",
        "ad": "33cl Bomonti Black Depozitosuz Şişe",
        "fiyat": 26.0
        },
        {
        "tur": "bira",
        "ad": "33cl Miller Depozitosuz Şişe",
        "fiyat": 26.0
        },
        {
        "tur": "bira",
        "ad": "33cl Bomonti İpa Depozitosuz Şişe",
        "fiyat": 26.5
        },
        {
        "tur": "bira",
        "ad": "50cl Carlsberg Kutu",
        "fiyat": 27.0
        },
        {
        "tur": "bira",
        "ad": "33cl Carlsberg Depozitosuz Şişe",
        "fiyat": 27.0
        },
        {
        "tur": "bira",
        "ad": "50cl Tuborg Gold Depozitolu Şişe",
        "fiyat": 27.5
        },
        {
        "tur": "bira",
        "ad": "50cl Efes Malt Depozitolu Şişe",
        "fiyat": 27.5
        },
        {
        "tur": "bira",
        "ad": "35cl Frederic Marzen Lager Şişe",
        "fiyat": 27.5
        },
        {
        "tur": "bira",
        "ad": "35cl Frederic India Pale Ale Şişe",
        "fiyat": 27.5
        },
        {
        "tur": "bira",
        "ad": "35cl Frederic Brown Ale Şişe",
        "fiyat": 27.5
        },
        {
        "tur": "bira",
        "ad": "35cl Frederic White Ipa Şişe",
        "fiyat": 27.5
        },
        {
        "tur": "bira",
        "ad": "50cl Carlsberg Depozitolu Şişe",
        "fiyat": 27.5
        },
        {
        "tur": "bira",
        "ad": "33cl Grimbergen Blonde Depozitosuz Şişe",
        "fiyat": 28.0
        },
        {
        "tur": "bira",
        "ad": "33cl Kronenbourg 1664 Blanc Depozitosuz Şişe",
        "fiyat": 28.0
        },
        {
        "tur": "bira",
        "ad": "33cl SOL Cerveza Depozitosuz Şişe",
        "fiyat": 28.0
        },
        {
        "tur": "bira",
        "ad": "33cl Weihenstephan Depozitosuz Şişe",
        "fiyat": 28.0
        },
        {
        "tur": "bira",
        "ad": "33cl Beck's Depozitosuz Şişe",
        "fiyat": 28.0
        },
        {
        "tur": "bira",
        "ad": "50cl Bomonti Depozitolu Şişe",
        "fiyat": 28.0
        },
        {
        "tur": "bira",
        "ad": "50cl Tuborg Gold Kutu",
        "fiyat": 28.0
        },
        {
        "tur": "bira",
        "ad": "50cl Bomonti Depozitosuz Şişe",
        "fiyat": 28.5
        },
        {
        "tur": "bira",
        "ad": "50cl Tuborg Amber Kutu",
        "fiyat": 29.0
        },
        {
        "tur": "bira",
        "ad": "50cl Tuborg Gold Depozitosuz Şişe",
        "fiyat": 29.0
        },
        {
        "tur": "bira",
        "ad": "50cl Efes Malt Kutu",
        "fiyat": 29.0
        },
        {
        "tur": "bira",
        "ad": "50cl Efes Extra Kutu",
        "fiyat": 29.0
        },
        {
        "tur": "bira",
        "ad": "50cl Efes Pilsen Kutu",
        "fiyat": 29.0
        },
        {
        "tur": "bira",
        "ad": "33cl Efes Brewmaster Red Ale Depozitosuz Şişe",
        "fiyat": 29.5
        },
        {
        "tur": "bira",
        "ad": "50cl Tuborg Amber Depozitosuz Şişe",
        "fiyat": 29.5
        },
        {
        "tur": "bira",
        "ad": "50cl Efes Pilsen Depozitolu Uzun Şişe",
        "fiyat": 29.5
        },
        {
        "tur": "bira",
        "ad": "33cl Efes Brewmaster White Ale Depozitosuz Şişe",
        "fiyat": 29.5
        },
        {
        "tur": "bira",
        "ad": "50cl Bomonti Filtresiz Depozitosuz Şişe",
        "fiyat": 30.0
        },
        {
        "tur": "bira",
        "ad": "50cl Tuborg Filtresiz Kutu",
        "fiyat": 30.0
        },
        {
        "tur": "bira",
        "ad": "50cl Tuborg Filtresiz Depozitosuz Şişe",
        "fiyat": 30.0
        },
        {
        "tur": "bira",
        "ad": "33cl Grimbergen Double Ambree Depozitosuz Şişe",
        "fiyat": 30.0
        },
        {
        "tur": "bira",
        "ad": "33cl Desperados Depozitosuz Şişe",
        "fiyat": 31.0
        },
        {
        "tur": "bira",
        "ad": "50cl Bomonti Filtresiz Kutu",
        "fiyat": 31.0
        },
        {
        "tur": "bira",
        "ad": "50cl Tuborg Kırmızı Special Kutu",
        "fiyat": 31.5
        },
        {
        "tur": "bira",
        "ad": "50cl Beck's Depozitosuz Şişe",
        "fiyat": 32.0
        },
        {
        "tur": "bira",
        "ad": "50cl Beck's Kutu",
        "fiyat": 32.0
        },
        {
        "tur": "bira",
        "ad": "50cl Efes Pilsen Özel Seri Depozitosuz",
        "fiyat": 32.0
        },
        {
        "tur": "bira",
        "ad": "33cl Weihenstephan Vitus Depozitosuz Şişe",
        "fiyat": 32.0
        },
        {
        "tur": "bira",
        "ad": "50cl Miller Kutu",
        "fiyat": 33.0
        },
        {
        "tur": "bira",
        "ad": "50cl Miller Depozitosuz Şişe",
        "fiyat": 33.0
        },
        {
        "tur": "bira",
        "ad": "Efes Glutensiz 50cl",
        "fiyat": 33.0
        },
        {
        "tur": "bira",
        "ad": "50cl Efes Fıçı Yüksek Alkollü Kutu",
        "fiyat": 33.0
        },
        {
        "tur": "bira",
        "ad": "50cl Efes Fıçı Yüksek Alkollü Şişe Depozitosuz",
        "fiyat": 34.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen Agora Beyaz Şarap",
        "fiyat": 39.0
        },
        {
        "tur": "bira",
        "ad": "35,5cl Corona Extra Şişe",
        "fiyat": 40.0
        },
        {
        "tur": "bira",
        "ad": "100cl Skol Bira Depozitosuz Pet Şişe",
        "fiyat": 40.0
        },
        {
        "tur": "bira",
        "ad": "44cl Guinness Kutu",
        "fiyat": 40.5
        },
        {
        "tur": "sarap",
        "ad": "75cl Agora Kırmızı Şarap (Sevilen)",
        "fiyat": 41.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen Altıntepe Kırmızı Şarap",
        "fiyat": 41.5
        },
        {
        "tur": "bira",
        "ad": "33cl Hoegaarden Depozitosuz Şişe",
        "fiyat": 42.0
        },
        {
        "tur": "bira",
        "ad": "33cl Erdinger Depozitosuz Şişe",
        "fiyat": 42.0
        },
        {
        "tur": "bira",
        "ad": "50cl Amsterdam Navigator Depozitosuz Şişe",
        "fiyat": 44.0
        },
        {
        "tur": "bira",
        "ad": "50cl Amsterdam Navigator Kutu",
        "fiyat": 44.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen Kalecik Karası Kırmızı Şarap",
        "fiyat": 44.9
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen Majestik Gamay Kırmızı Şarap",
        "fiyat": 44.9
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen Sultaniye Beyaz Şarap",
        "fiyat": 44.9
        },
        {
        "tur": "bira",
        "ad": "33cl Leffe Brune Blonde Depozitosuz Şişe",
        "fiyat": 45.0
        },
        {
        "tur": "bira",
        "ad": "100cl Marmara Gold Depozitosuz Şişe",
        "fiyat": 45.0
        },
        {
        "tur": "bira",
        "ad": "33cl Leffe Brune Depozitosuz Şişe",
        "fiyat": 45.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen Majestik Öküzgözü Kırmızı",
        "fiyat": 45.9
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen Majestik Gamay Kırmızı Şarap",
        "fiyat": 45.9
        },
        {
        "tur": "bira",
        "ad": "33cl Leffe Radieuse Depozitosuz Şişe",
        "fiyat": 48.0
        },
        {
        "tur": "kokteyl",
        "ad": "14.4 Çilekli Volim",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "14.4 Volim Redbull",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "14.4 Volim Limonlu Alkol",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "Volim Sade",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "Volim Karışık Meyveli",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "Volim Karpuz Aromalı",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "Volim Kola Aromalı",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "Volim Shot Karpuz Çilek",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "Volim Shot Votka İçeçeği",
        "fiyat": 50.0
        },
        {
        "tur": "kokteyl",
        "ad": "Volim Enerji İçeceği Aromalı",
        "fiyat": 50.0
        },
        {
        "tur": "sarap",
        "ad": "18,75cl Villa Doluca Şarap",
        "fiyat": 50.0
        },
        {
        "tur": "bira",
        "ad": "45cl Grolsch Depozitosuz Şişe",
        "fiyat": 52.0
        },
        {
        "tur": "bira",
        "ad": "33cl Duvel Depozitosuz Şişe",
        "fiyat": 57.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Biricik Sek Beyaz Cam Şarap",
        "fiyat": 60.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Biricik Sek Kırmızı CamŞarap",
        "fiyat": 60.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Biricik Sek Kırmızı Cam Şarap",
        "fiyat": 60.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Biricik Sek Beyaz Cam Şarap",
        "fiyat": 60.0
        },
        {
        "tur": "raki",
        "ad": "20cl Saki Rakı Yaş Üzüm",
        "fiyat": 64.5
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen İsabey Saublanc (Beyaz)",
        "fiyat": 79.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen İsabey Merlot Şarap",
        "fiyat": 79.5
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen İsabey Narince Beyaz Şarap",
        "fiyat": 79.5
        },
        {
        "tur": "sarap",
        "ad": "75cl Sevilen İsabey Cabarnet",
        "fiyat": 79.5
        },
        {
        "tur": "sarap",
        "ad": "100cl Biricik Sek Kırmızı Cam Şarap",
        "fiyat": 80.0
        },
        {
        "tur": "sarap",
        "ad": "100cl Biricik Sek Kırmızı Cam Şarap",
        "fiyat": 80.0
        },
        {
        "tur": "sarap",
        "ad": "100cl Biricik Sek Beyaz Cam Şarap",
        "fiyat": 80.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Mistik Şarap",
        "fiyat": 80.0
        },
        {
        "tur": "sarap",
        "ad": "100cl Biricik Sek Beyaz Cam Şarap",
        "fiyat": 80.0
        },
        {
        "tur": "sarap",
        "ad": "37,5cl Villa Doluca Şarap",
        "fiyat": 80.0
        },
        {
        "tur": "sarap",
        "ad": "37,5cl Doluca Şarap",
        "fiyat": 80.0
        },
        {
        "tur": "raki",
        "ad": "35cl Saki Ginseng",
        "fiyat": 88.5
        },
        {
        "tur": "votka",
        "ad": "20cl İstanblue Votka",
        "fiyat": 91.0
        },
        {
        "tur": "likor",
        "ad": "50cl Hare Nane Likörü",
        "fiyat": 95.0
        },
        {
        "tur": "likor",
        "ad": "50cl Hare Acıbadem Likörü",
        "fiyat": 95.0
        },
        {
        "tur": "likor",
        "ad": "50cl Hare Muz Likörü",
        "fiyat": 95.0
        },
        {
        "tur": "likor",
        "ad": "50cl Hare Vişne Likörü",
        "fiyat": 95.0
        },
        {
        "tur": "likor",
        "ad": "50cl Hare Hindistan Cevizi Likörü",
        "fiyat": 95.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Crama Regala Sauvignon Blanc",
        "fiyat": 99.9
        },
        {
        "tur": "sarap",
        "ad": "75cl Crama Regala Chardonnay",
        "fiyat": 104.9
        },
        {
        "tur": "sarap",
        "ad": "75cl Crama Regala Merlot",
        "fiyat": 104.9
        },
        {
        "tur": "sarap",
        "ad": "75cl Crama Regala Cabernet Sauvignon",
        "fiyat": 104.9
        },
        {
        "tur": "sarap",
        "ad": "Biricik Sek Kırmızı-Beyaz-Rose Şarap",
        "fiyat": 110.0
        },
        {
        "tur": "likor",
        "ad": "50cl Hare Portakal Likörü",
        "fiyat": 110.0
        },
        {
        "tur": "sarap",
        "ad": "150cl Biricik Galon Kırmızı Cam Şarap",
        "fiyat": 118.0
        },
        {
        "tur": "sarap",
        "ad": "Biricik Sek Kırmızı-Beyaz-Blush Şarap",
        "fiyat": 118.0
        },
        {
        "tur": "sarap",
        "ad": "150cl Biricik Galon Beyaz Cam Şarap",
        "fiyat": 118.0
        },
        {
        "tur": "sarap",
        "ad": "150cl Biricik Galon Kırmızı Cam Şarap",
        "fiyat": 118.0
        },
        {
        "tur": "sarap",
        "ad": "150cl Biricik Galon Beyaz Cam Şarap",
        "fiyat": 118.0
        },
        {
        "tur": "likor",
        "ad": "100cl Hare Kahve, Portakal, Kayısı Likörü",
        "fiyat": 125.0
        },
        {
        "tur": "likor",
        "ad": "100cl Hare Çikolata Likörü",
        "fiyat": 125.0
        },
        {
        "tur": "likor",
        "ad": "100cl Hare Acıbadem, Bitter, Nane Likörü",
        "fiyat": 125.0
        },
        {
        "tur": "likor",
        "ad": "100cl Hare Şeftali, Muz, Tropikal Likörü",
        "fiyat": 125.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Sultaniye Emir Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Shiraz Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Cab. Sauvıgnon-Merlot Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Moskado Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Kalecik Karası Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Öküzgözü Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Boğazkere Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Sauvıgnon Blanc Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Frenache Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Dlc Narince Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Doluca Şarap",
        "fiyat": 130.0
        },
        {
        "tur": "raki",
        "ad": "35cl Anadolu Boğma Rakı",
        "fiyat": 130.5
        },
        {
        "tur": "likor",
        "ad": "35cl Muz Likörü",
        "fiyat": 132.0
        },
        {
        "tur": "sarap",
        "ad": "150cl Biricik Kulplu Kırmızı Şarap",
        "fiyat": 132.0
        },
        {
        "tur": "sarap",
        "ad": "150cl Biricik Kulplu Beyaz Şarap",
        "fiyat": 132.0
        },
        {
        "tur": "likor",
        "ad": "35cl Portakal Likörü",
        "fiyat": 132.0
        },
        {
        "tur": "likor",
        "ad": "35cl Nane Likörü",
        "fiyat": 132.0
        },
        {
        "tur": "likor",
        "ad": "35cl Acıbadem Likörü",
        "fiyat": 132.0
        },
        {
        "tur": "likor",
        "ad": "35cl Ahududu Likörü",
        "fiyat": 132.0
        },
        {
        "tur": "likor",
        "ad": "35cl Vişne Likörü",
        "fiyat": 132.0
        },
        {
        "tur": "likor",
        "ad": "35cl Damla Sakızlı Likör",
        "fiyat": 132.0
        },
        {
        "tur": "votka",
        "ad": "35cl Bazooka Votka",
        "fiyat": 139.0
        },
        {
        "tur": "sarap",
        "ad": "100cl Mistik Şarap",
        "fiyat": 140.0
        },
        {
        "tur": "votka",
        "ad": "35cl İstanblue Votka",
        "fiyat": 140.0
        },
        {
        "tur": "raki",
        "ad": "35cl Ata Rakı",
        "fiyat": 140.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Villa Doluca Şarap",
        "fiyat": 140.0
        },
        {
        "tur": "votka",
        "ad": "20cl Lithuanian Vodka",
        "fiyat": 140.9
        },
        {
        "tur": "raki",
        "ad": "20cl Saki Rakı Klasik",
        "fiyat": 145.5
        },
        {
        "tur": "raki",
        "ad": "35cl Yekta Rakı",
        "fiyat": 149.0
        },
        {
        "tur": "raki",
        "ad": "35cl Burgaz Rakı",
        "fiyat": 149.5
        },
        {
        "tur": "votka",
        "ad": "35cl Wyborowa Votka",
        "fiyat": 150.0
        },
        {
        "tur": "sarap",
        "ad": "75cl Villa Doluca Neo Şarap",
        "fiyat": 150.0
        },
        {
        "tur": "sarap",
        "ad": "200cl Biricik Galon Beyaz Cam Şarap",
        "fiyat": 155.0
        },
        {
        "tur": "sarap",
        "ad": "200cl Biricik Galon Kırmızı Cam Şarap",
        "fiyat": 155.0
        },
        {
        "tur": "raki",
        "ad": "20cl Saki Rakı Altın Seri",
        "fiyat": 156.0
        },
        {
        "tur": "cin",
        "ad": "35cl Gilbey's Cin",
        "fiyat": 159.0
        },
        {
        "tur": "raki",
        "ad": "35cl Tayfa Rakı",
        "fiyat": 159.5
        },
        {
        "tur": "votka",
        "ad": "35cl Gilbey's Votka",
        "fiyat": 160.0
        },
        {
        "tur": "cin",
        "ad": "35cl Stirling Cin",
        "fiyat": 160.9
        },
        {
        "tur": "viski",
        "ad": "35cl Jack Daniels Tennessee Honey Viski",
        "fiyat": 163.0
        },
        {
        "tur": "viski",
        "ad": "35cl Jack Daniels Tennessee Apple Viski",
        "fiyat": 163.0
        },
        {
        "tur": "raki",
        "ad": "70cl Saki Ginseng",
        "fiyat": 164.5
        },
        {
        "tur": "sarap",
        "ad": "100cl Doluca Şarap",
        "fiyat": 165.0
        },
        {
        "tur": "raki",
        "ad": "35cl İzmir Rakısı",
        "fiyat": 169.0
        },
        {
        "tur": "tekila",
        "ad": "35cl Olmeca Blanco Tekila",
        "fiyat": 169.0
        },
        {
        "tur": "votka",
        "ad": "35cl Binboa Votka",
        "fiyat": 169.0
        },
        {
        "tur": "votka",
        "ad": "35cl Stumbra Centenary Vodka",
        "fiyat": 170.0
        },
        {
        "tur": "viski",
        "ad": "35cl Ballantines Finest Viski",
        "fiyat": 175.0
        },
        {
        "tur": "raki",
        "ad": "35cl Saki Rakı Klasik",
        "fiyat": 175.2
        },
        {
        "tur": "raki",
        "ad": "35cl İzmir Rakısı Yaş Üzüm",
        "fiyat": 175.5
        },
        {
        "tur": "raki",
        "ad": "35cl Yeni Rakı",
        "fiyat": 176.75
        },
        {
        "tur": "viski",
        "ad": "20cl Chivas Regal (12 Yıllık) Viski",
        "fiyat": 179.0
        },
        {
        "tur": "kokteyl",
        "ad": "100cl Volim",
        "fiyat": 180.0
        },
        {
        "tur": "raki",
        "ad": "35cl İzmir Rakısı Göbek",
        "fiyat": 185.0
        },
        {
        "tur": "votka",
        "ad": "35cl Smirnoff Red Votka",
        "fiyat": 185.0
        },
        {
        "tur": "tekila",
        "ad": "35cl Olmeca Gold Tekila",
        "fiyat": 189.0
        },
        {
        "tur": "votka",
        "ad": "50cl Bazooka Votka",
        "fiyat": 189.0
        },
        {
        "tur": "kokteyl",
        "ad": "Kırbıyık Kokteyl Mojito 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "kokteyl",
        "ad": "Kırbıyık Kokteyl Cosmopolitan 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "kokteyl",
        "ad": "Kırbıyık Kokteyl Sek On The Beach 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "kokteyl",
        "ad": "Kırbıyık Kokteyl Orman Meyveli 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "kokteyl",
        "ad": "Kırbıyık Kokteyl Margarita 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "kokteyl",
        "ad": "Bue Hawaii 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "kokteyl",
        "ad": "Kırbıyık Kokteyl Kavun 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "kokteyl",
        "ad": "Kırbıyık Kokteyl Karpuz Çilek 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "kokteyl",
        "ad": "Harrley's Irish Cream 100cl",
        "fiyat": 190.0
        },
        {
        "tur": "likor",
        "ad": "100cl Hare Portakal Likörü",
        "fiyat": 190.0
        },
        {
        "tur": "tekila",
        "ad": "70cl El Jimador Blanco Tequila",
        "fiyat": 195.0
        },
        {
        "tur": "votka",
        "ad": "50cl İstanblue Votka",
        "fiyat": 195.0
        },
        {
        "tur": "raki",
        "ad": "20cl Saki Rakı Siyah Üzüm",
        "fiyat": 195.5
        },
        {
        "tur": "raki",
        "ad": "35cl Yeni Rakı Yeni Seri",
        "fiyat": 199.0
        },
        {
        "tur": "raki",
        "ad": "35cl Tekirdağ Rakı",
        "fiyat": 199.0
        },
        {
        "tur": "cin",
        "ad": "35cl Gordon's Dry Cin",
        "fiyat": 199.0
        },
        {
        "tur": "raki",
        "ad": "35cl Saki Rakı Altın Seri",
        "fiyat": 199.5
        },
        {
        "tur": "raki",
        "ad": "35cl Tekirdağ Rakı Trakya Serisi",
        "fiyat": 199.5
        },
        {
        "tur": "votka",
        "ad": "35cl Lithuanian Vodka",
        "fiyat": 199.9
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Yaş Üzüm Rakı",
        "fiyat": 200.0
        },
        {
        "tur": "raki",
        "ad": "35cl Tekirdağ Rakı Kavrulmuş Anason",
        "fiyat": 200.0
        },
        {
        "tur": "raki",
        "ad": "35cl Saki Rakı Yaş Üzüm",
        "fiyat": 200.5
        },
        {
        "tur": "viski",
        "ad": "35cl Ballantines 12 Yıl Viski",
        "fiyat": 205.0
        },
        {
        "tur": "votka",
        "ad": "50cl Wyborowa Votka",
        "fiyat": 205.0
        },
        {
        "tur": "viski",
        "ad": "35cl Jack Daniels Old No.7 Viski",
        "fiyat": 205.5
        },
        {
        "tur": "raki",
        "ad": "35cl Tekirdağ Rakı Altın Seri",
        "fiyat": 209.0
        },
        {
        "tur": "votka",
        "ad": "35cl Absolut Vodka",
        "fiyat": 209.0
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Gold Rakı",
        "fiyat": 209.5
        },
        {
        "tur": "tekila",
        "ad": "70cl El Jimador Reposado Tequila",
        "fiyat": 210.0
        },
        {
        "tur": "cin",
        "ad": "35cl Beefeater Cin",
        "fiyat": 210.0
        },
        {
        "tur": "likor",
        "ad": "100cl Garrone Ricard Likör",
        "fiyat": 210.0
        },
        {
        "tur": "raki",
        "ad": "35cl Yeni Rakı Ustaların Karışımı",
        "fiyat": 215.5
        },
        {
        "tur": "viski",
        "ad": "35cl Bell's Viski",
        "fiyat": 219.0
        },
        {
        "tur": "raki",
        "ad": "50cl Tayfa Rakı",
        "fiyat": 219.0
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Çilingir Xtra Rakı",
        "fiyat": 220.5
        },
        {
        "tur": "likor",
        "ad": "100cl Garrone Rosso Likör",
        "fiyat": 225.0
        },
        {
        "tur": "likor",
        "ad": "35cl Jagermeister",
        "fiyat": 225.0
        },
        {
        "tur": "likor",
        "ad": "100cl Garrone Bianco Dry Likör",
        "fiyat": 225.0
        },
        {
        "tur": "votka",
        "ad": "50cl Stumbra Centenary Vodka",
        "fiyat": 225.9
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Tek İmbik Rakı",
        "fiyat": 226.0
        },
        {
        "tur": "raki",
        "ad": "35cl Yeni Rakı Âlâ",
        "fiyat": 229.0
        },
        {
        "tur": "raki",
        "ad": "50cl Burgaz Rakı",
        "fiyat": 229.0
        },
        {
        "tur": "raki",
        "ad": "35cl Kulüp Rakı",
        "fiyat": 229.5
        },
        {
        "tur": "cin",
        "ad": "50cl Stirling Cin",
        "fiyat": 230.9
        },
        {
        "tur": "sarap",
        "ad": "150cl Mistik Şarap",
        "fiyat": 235.0
        },
        {
        "tur": "tekila",
        "ad": "50cl Olmeca Blanco Tekila",
        "fiyat": 235.0
        },
        {
        "tur": "raki",
        "ad": "70cl Anadolu Boğma Rakı",
        "fiyat": 235.0
        },
        {
        "tur": "raki",
        "ad": "35cl Beylerbeyi Göbek Rakısı",
        "fiyat": 235.0
        },
        {
        "tur": "raki",
        "ad": "50cl İzmir Rakısı",
        "fiyat": 239.5
        },
        {
        "tur": "sarap",
        "ad": "300cl Biricik Kulplu Beyaz Şarap",
        "fiyat": 240.0
        },
        {
        "tur": "sarap",
        "ad": "Biricik Suni Yarı Köpüren Şarap (Beyaz-Rose)",
        "fiyat": 240.0
        },
        {
        "tur": "raki",
        "ad": "35cl Altınbaş Rakı",
        "fiyat": 240.0
        },
        {
        "tur": "sarap",
        "ad": "300cl Biricik Kulplu Kırmızı Şarap",
        "fiyat": 240.0
        },
        {
        "tur": "viski",
        "ad": "50cl Ballantines Finest Viski",
        "fiyat": 245.0
        },
        {
        "tur": "raki",
        "ad": "50cl İzmir Rakısı Yaş Üzüm",
        "fiyat": 245.0
        },
        {
        "tur": "viski",
        "ad": "35cl J&B Viski",
        "fiyat": 245.0
        },
        {
        "tur": "viski",
        "ad": "35cl Johnnie Walker Black Label Viski",
        "fiyat": 245.0
        },
        {
        "tur": "raki",
        "ad": "35cl Saki Rakı Siyah Üzüm",
        "fiyat": 245.5
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Klasik Rakı",
        "fiyat": 245.5
        },
        {
        "tur": "votka",
        "ad": "50cl Smirnoff Red",
        "fiyat": 249.5
        },
        {
        "tur": "raki",
        "ad": "50cl Efe Klasik Rakı",
        "fiyat": 249.5
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Çilingir Xtra Yaş Üzüm Rakı",
        "fiyat": 249.9
        },
        {
        "tur": "raki",
        "ad": "35cl Efe 3 Distile Rakı",
        "fiyat": 250.0
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Geleneksel Rakı",
        "fiyat": 250.9
        },
        {
        "tur": "raki",
        "ad": "50cl Saki Rakı Klasik",
        "fiyat": 250.9
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Çilingir Rakı",
        "fiyat": 251.9
        },
        {
        "tur": "raki",
        "ad": "35cl Efe Sarı Zeybek Rakı",
        "fiyat": 257.0
        },
        {
        "tur": "votka",
        "ad": "70cl Bazooka Votka",
        "fiyat": 260.0
        },
        {
        "tur": "votka",
        "ad": "70cl İstanblue Votka",
        "fiyat": 265.5
        },
        {
        "tur": "votka",
        "ad": "70cl Lithuanian Vodka",
        "fiyat": 269.9
        },
        {
        "tur": "raki",
        "ad": "70cl Ata Rakı",
        "fiyat": 271.0
        },
        {
        "tur": "raki",
        "ad": "50cl Tekirdağ Rakı",
        "fiyat": 275.0
        },
        {
        "tur": "votka",
        "ad": "70cl Wyborowa Votka",
        "fiyat": 275.0
        },
        {
        "tur": "viski",
        "ad": "35cl Johnnie Walker Red Label Viski",
        "fiyat": 275.0
        },
        {
        "tur": "viski",
        "ad": "50cl Jack Daniels Old No.7 Viski",
        "fiyat": 279.0
        },
        {
        "tur": "viski",
        "ad": "35cl Chivas Regal (12 Yıllık) Viski",
        "fiyat": 279.4
        },
        {
        "tur": "votka",
        "ad": "50cl Lithuanian Vodka",
        "fiyat": 280.9
        },
        {
        "tur": "raki",
        "ad": "50cl Efe Yaş Üzüm Rakı",
        "fiyat": 281.0
        },
        {
        "tur": "viski",
        "ad": "50cl Ballantines 12 Yıl Viski",
        "fiyat": 285.0
        },
        {
        "tur": "viski",
        "ad": "50cl Bell's Viski",
        "fiyat": 285.9
        },
        {
        "tur": "votka",
        "ad": "50cl Absolut Vodka",
        "fiyat": 288.0
        },
        {
        "tur": "raki",
        "ad": "50cl Yeni Rakı Yeni Seri",
        "fiyat": 289.0
        },
        {
        "tur": "raki",
        "ad": "50cl Yeni Rakı",
        "fiyat": 289.5
        },
        {
        "tur": "raki",
        "ad": "50cl Efe Gold Rakı",
        "fiyat": 295.0
        },
        {
        "tur": "votka",
        "ad": "70cl Binboa Pier Ginger Votka",
        "fiyat": 295.0
        },
        {
        "tur": "votka",
        "ad": "70cl Binboa Red Orange",
        "fiyat": 295.0
        },
        {
        "tur": "votka",
        "ad": "50cl Binboa Votka",
        "fiyat": 295.0
        },
        {
        "tur": "votka",
        "ad": "70cl Binboa Red Apple",
        "fiyat": 295.0
        },
        {
        "tur": "votka",
        "ad": "70cl Binboa Satsuma Votka",
        "fiyat": 295.0
        },
        {
        "tur": "votka",
        "ad": "70cl Binboa Mojito",
        "fiyat": 295.0
        },
        {
        "tur": "votka",
        "ad": "70cl Gilbey's Votka",
        "fiyat": 295.0
        },
        {
        "tur": "raki",
        "ad": "50cl Tekirdağ Rakı Altın Seri",
        "fiyat": 295.0
        },
        {
        "tur": "raki",
        "ad": "50cl Saki Rakı Yaş Üzüm",
        "fiyat": 295.9
        },
        {
        "tur": "raki",
        "ad": "50cl Saki Rakı Altın Seri",
        "fiyat": 295.9
        },
        {
        "tur": "raki",
        "ad": "70cl Tayfa Rakı",
        "fiyat": 299.0
        },
        {
        "tur": "raki",
        "ad": "70cl Burgaz Rakı",
        "fiyat": 300.0
        },
        {
        "tur": "viski",
        "ad": "70cl Jack Daniels Tennessee Honey Viski",
        "fiyat": 300.0
        },
        {
        "tur": "viski",
        "ad": "70cl Jack Daniels Tennessee Apple Viski",
        "fiyat": 300.0
        },
        {
        "tur": "cin",
        "ad": "75cl Stirling Cin",
        "fiyat": 300.9
        },
        {
        "tur": "raki",
        "ad": "50cl Beylerbeyi Göbek Rakısı",
        "fiyat": 305.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff North",
        "fiyat": 309.0
        },
        {
        "tur": "votka",
        "ad": "70cl Stumbra Centenary Vodka",
        "fiyat": 310.9
        },
        {
        "tur": "viski",
        "ad": "70cl Jack Daniels Special Edition Viski",
        "fiyat": 320.0
        },
        {
        "tur": "raki",
        "ad": "70cl Yekta Rakı",
        "fiyat": 325.0
        },
        {
        "tur": "tekila",
        "ad": "70cl Olmeca Blanco Tekila",
        "fiyat": 325.0
        },
        {
        "tur": "tekila",
        "ad": "70cl Olmeca Dark Chocolate",
        "fiyat": 325.0
        },
        {
        "tur": "raki",
        "ad": "70cl İzmir Rakısı",
        "fiyat": 325.0
        },
        {
        "tur": "raki",
        "ad": "70cl İzmir Rakısı Yaş Üzüm",
        "fiyat": 330.0
        },
        {
        "tur": "viski",
        "ad": "70cl Ballantines Finest Viski",
        "fiyat": 330.0
        },
        {
        "tur": "likor",
        "ad": "70cl Jagermeister",
        "fiyat": 335.0
        },
        {
        "tur": "raki",
        "ad": "70cl İzmir Rakısı Göbek",
        "fiyat": 335.0
        },
        {
        "tur": "raki",
        "ad": "70cl Saki Rakı Klasik",
        "fiyat": 335.5
        },
        {
        "tur": "viski",
        "ad": "50cl Johnnie Walker Black Label Viski",
        "fiyat": 339.0
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Klasik Rakı",
        "fiyat": 339.5
        },
        {
        "tur": "raki",
        "ad": "70cl Efe 3 Distile Rakı",
        "fiyat": 340.5
        },
        {
        "tur": "raki",
        "ad": "50cl Saki Rakı Siyah Üzüm",
        "fiyat": 345.5
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Red",
        "fiyat": 349.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Espresso",
        "fiyat": 359.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Green Apple",
        "fiyat": 359.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Peppermint (Nane)",
        "fiyat": 359.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Citrus (Narenciye)",
        "fiyat": 359.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Rasberry (Ahududu)",
        "fiyat": 359.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Apple (Elma) Red",
        "fiyat": 359.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Vanilla (Vanilya)",
        "fiyat": 359.0
        },
        {
        "tur": "votka",
        "ad": "70cl Smirnoff Orange (Portakal)",
        "fiyat": 359.0
        },
        {
        "tur": "viski",
        "ad": "50cl Chivas Regal (12 Yıllık) Viski",
        "fiyat": 359.0
        },
        {
        "tur": "tekila",
        "ad": "70cl Olmeca Gold Tekila",
        "fiyat": 360.0
        },
        {
        "tur": "viski",
        "ad": "70cl Ballantine's 7 İskoç Viski",
        "fiyat": 360.0
        },
        {
        "tur": "votka",
        "ad": "100cl Bazooka Votka",
        "fiyat": 360.0
        },
        {
        "tur": "raki",
        "ad": "70cl Yeni Rakı Yeni Seri",
        "fiyat": 369.0
        },
        {
        "tur": "votka",
        "ad": "100cl İstanblue Votka",
        "fiyat": 370.0
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Yaş Üzüm Rakı",
        "fiyat": 373.0
        },
        {
        "tur": "cin",
        "ad": "70cl Gilbey's Cin",
        "fiyat": 375.0
        },
        {
        "tur": "raki",
        "ad": "70cl Tekirdağ Rakı",
        "fiyat": 375.5
        },
        {
        "tur": "raki",
        "ad": "70cl Saki Rakı Yaş Üzüm",
        "fiyat": 375.5
        },
        {
        "tur": "raki",
        "ad": "70cl Tekirdağ Rakı Trakya Serisi",
        "fiyat": 375.5
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Vodka Mandrin",
        "fiyat": 377.0
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Vodka Vanilia",
        "fiyat": 377.0
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Vodka Raspberri",
        "fiyat": 377.0
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Extrakt Vodka",
        "fiyat": 377.0
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Vodka",
        "fiyat": 377.0
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Lime Vodka",
        "fiyat": 377.0
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Vodka Apeach",
        "fiyat": 377.0
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Citron Vodka",
        "fiyat": 377.0
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Pears Vodka",
        "fiyat": 377.0
        },
        {
        "tur": "raki",
        "ad": "70cl Yeni Rakı",
        "fiyat": 379.5
        },
        {
        "tur": "viski",
        "ad": "70cl Jack Daniels Old No.7 Viski",
        "fiyat": 380.0
        },
        {
        "tur": "viski",
        "ad": "50cl J&B Viski",
        "fiyat": 380.0
        },
        {
        "tur": "viski",
        "ad": "50cl Johnnie Walker Red Label Viski",
        "fiyat": 380.0
        },
        {
        "tur": "likor",
        "ad": "35cl Cointreau Likör",
        "fiyat": 381.0
        },
        {
        "tur": "votka",
        "ad": "100cl Wyborowa Votka",
        "fiyat": 385.0
        },
        {
        "tur": "viski",
        "ad": "70cl Ballantines 12 Yıl Viski",
        "fiyat": 390.0
        },
        {
        "tur": "cin",
        "ad": "70cl Beefeater Pink Cin",
        "fiyat": 395.0
        },
        {
        "tur": "raki",
        "ad": "70cl Saki Rakı Altın Seri",
        "fiyat": 395.9
        },
        {
        "tur": "cin",
        "ad": "70cl Beefeater Cin",
        "fiyat": 396.0
        },
        {
        "tur": "viski",
        "ad": "70cl Bell's Viski",
        "fiyat": 399.0
        },
        {
        "tur": "cin",
        "ad": "70cl Gordon's Dry Cin",
        "fiyat": 399.0
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Gold Rakı",
        "fiyat": 399.0
        },
        {
        "tur": "raki",
        "ad": "70cl Tekirdağ Rakı Altın Seri",
        "fiyat": 399.0
        },
        {
        "tur": "raki",
        "ad": "70cl Tekirdağ Rakı Kavrulmuş Anason",
        "fiyat": 400.0
        },
        {
        "tur": "votka",
        "ad": "100cl Lithuanian Vodka",
        "fiyat": 400.9
        },
        {
        "tur": "viski",
        "ad": "100cl Jack Daniels Tennessee Honey Viski",
        "fiyat": 405.0
        },
        {
        "tur": "viski",
        "ad": "100cl Jack Daniels Tennessee Apple Viski",
        "fiyat": 405.0
        },
        {
        "tur": "raki",
        "ad": "70cl Yeni Rakı Ustaların Karışımı",
        "fiyat": 409.0
        },
        {
        "tur": "raki",
        "ad": "100cl Tayfa Rakı",
        "fiyat": 410.5
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Tek İmbik Rakı",
        "fiyat": 415.0
        },
        {
        "tur": "votka",
        "ad": "70cl Binboa Votka",
        "fiyat": 419.0
        },
        {
        "tur": "cin",
        "ad": "100cl Stirling Cin",
        "fiyat": 419.9
        },
        {
        "tur": "votka",
        "ad": "100cl Gilbey's Votka",
        "fiyat": 420.0
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Geleneksel Rakı",
        "fiyat": 420.5
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Çilingir Rakı",
        "fiyat": 425.5
        },
        {
        "tur": "raki",
        "ad": "70cl Beylerbeyi Göbek Rakısı",
        "fiyat": 429.0
        },
        {
        "tur": "raki",
        "ad": "70cl Kulüp Rakı",
        "fiyat": 430.0
        },
        {
        "tur": "raki",
        "ad": "70cl Yeni Rakı Âlâ",
        "fiyat": 435.0
        },
        {
        "tur": "votka",
        "ad": "100cl Stumbra Centenary Vodka",
        "fiyat": 435.9
        },
        {
        "tur": "tekila",
        "ad": "70cl Olmeca Altos Plata Tekila",
        "fiyat": 440.0
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Çilingir Xtra Rakı",
        "fiyat": 440.9
        },
        {
        "tur": "raki",
        "ad": "100cl Saki Rakı Klasik",
        "fiyat": 440.9
        },
        {
        "tur": "raki",
        "ad": "70cl Saki Rakı Siyah Üzüm",
        "fiyat": 445.5
        },
        {
        "tur": "viski",
        "ad": "70cl Johnnie Walker Black Label Viski",
        "fiyat": 449.0
        },
        {
        "tur": "raki",
        "ad": "100cl İzmir Rakısı",
        "fiyat": 449.5
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Çilingir Xtra Yaş Üzüm Rakı",
        "fiyat": 449.9
        },
        {
        "tur": "tekila",
        "ad": "70cl Olmeca Altos Reposadd",
        "fiyat": 450.0
        },
        {
        "tur": "raki",
        "ad": "100cl Yekta Rakı",
        "fiyat": 450.5
        },
        {
        "tur": "likor",
        "ad": "100cl Jagermeister",
        "fiyat": 452.5
        },
        {
        "tur": "viski",
        "ad": "100cl Ballantines Finest Viski",
        "fiyat": 455.0
        },
        {
        "tur": "tekila",
        "ad": "100cl Olmeca Blanco Tekila",
        "fiyat": 455.0
        },
        {
        "tur": "raki",
        "ad": "100cl İzmir Rakısı Yaş Üzüm",
        "fiyat": 459.5
        },
        {
        "tur": "raki",
        "ad": "70cl Altınbaş Rakı",
        "fiyat": 460.0
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Sarı Zeybek Rakı",
        "fiyat": 469.5
        },
        {
        "tur": "cin",
        "ad": "70cl Gordon's Pink Cin",
        "fiyat": 475.0
        },
        {
        "tur": "raki",
        "ad": "100cl Efe Klasik Rakı",
        "fiyat": 475.5
        },
        {
        "tur": "viski",
        "ad": "70cl Chivas Regal (12 Yıl) Viski",
        "fiyat": 479.0
        },
        {
        "tur": "cin",
        "ad": "100cl Gilbey's Cin",
        "fiyat": 481.0
        },
        {
        "tur": "viski",
        "ad": "70cl Chivas Regal (13 Yıllık) İskoç Viskisi",
        "fiyat": 490.0
        },
        {
        "tur": "viski",
        "ad": "70cl Jack Daniels Single Barrel Viski",
        "fiyat": 495.0
        },
        {
        "tur": "votka",
        "ad": "100cl Smirnoff Red",
        "fiyat": 499.0
        },
        {
        "tur": "raki",
        "ad": "100cl Yeni Rakı",
        "fiyat": 499.5
        },
        {
        "tur": "raki",
        "ad": "100cl Yeni Rakı Yeni Seri",
        "fiyat": 499.5
        },
        {
        "tur": "viski",
        "ad": "70cl J&B Viski",
        "fiyat": 500.0
        },
        {
        "tur": "viski",
        "ad": "70cl Johnnie Walker Red Label Viski",
        "fiyat": 500.0
        },
        {
        "tur": "raki",
        "ad": "100cl Efe Yaş Üzüm Rakı",
        "fiyat": 504.5
        },
        {
        "tur": "viski",
        "ad": "100cl Jack Daniels Old No.7 Viski",
        "fiyat": 515.0
        },
        {
        "tur": "raki",
        "ad": "100cl Tekirdağ Rakı",
        "fiyat": 519.0
        },
        {
        "tur": "votka",
        "ad": "100cl Absolut Vodka",
        "fiyat": 525.0
        },
        {
        "tur": "raki",
        "ad": "100cl Saki Rakı Yaş Üzüm",
        "fiyat": 525.9
        },
        {
        "tur": "raki",
        "ad": "70cl Tekirdağ Rakı No. 10",
        "fiyat": 529.0
        },
        {
        "tur": "cin",
        "ad": "70cl Malfy Con Limone",
        "fiyat": 535.0
        },
        {
        "tur": "cin",
        "ad": "70cl Malfy Gın Rose",
        "fiyat": 535.0
        },
        {
        "tur": "cin",
        "ad": "70cl Malfy Originale Cin",
        "fiyat": 535.0
        },
        {
        "tur": "viski",
        "ad": "100cl Ballantines 12 Yıl Viski",
        "fiyat": 540.0
        },
        {
        "tur": "raki",
        "ad": "100cl Tekirdağ Rakı Altın Seri",
        "fiyat": 549.5
        },
        {
        "tur": "raki",
        "ad": "100cl Efe Gold Rakı",
        "fiyat": 549.5
        },
        {
        "tur": "raki",
        "ad": "100cl Saki Rakı Altın Seri",
        "fiyat": 549.9
        },
        {
        "tur": "viski",
        "ad": "100cl Bell's Viski",
        "fiyat": 550.5
        },
        {
        "tur": "raki",
        "ad": "100cl Beylerbeyi Göbek Rakısı",
        "fiyat": 569.0
        },
        {
        "tur": "raki",
        "ad": "100cl Efe Çilingir Rakı",
        "fiyat": 579.5
        },
        {
        "tur": "raki",
        "ad": "100cl Efe Tek İmbik Rakı",
        "fiyat": 580.5
        },
        {
        "tur": "cin",
        "ad": "70cl Tanqueray Cin (London Dry Gin)",
        "fiyat": 583.0
        },
        {
        "tur": "tekila",
        "ad": "70cl Avion Silver",
        "fiyat": 600.0
        },
        {
        "tur": "cin",
        "ad": "70cl Tanqueray Flor De Sevilla Cin",
        "fiyat": 625.0
        },
        {
        "tur": "viski",
        "ad": "100cl Johnnie Walker Black Label Viski",
        "fiyat": 639.0
        },
        {
        "tur": "viski",
        "ad": "70cl Chivas Regal (15 Yıllık) Viski",
        "fiyat": 649.0
        },
        {
        "tur": "tekila",
        "ad": "70cl Avion Reposadd",
        "fiyat": 650.0
        },
        {
        "tur": "viski",
        "ad": "70cl Johnnie Walker Double Black Viski",
        "fiyat": 650.0
        },
        {
        "tur": "viski",
        "ad": "70cl Ballantine's 17 İskoç Viski",
        "fiyat": 660.0
        },
        {
        "tur": "viski",
        "ad": "150cl Ballantines Finest Viski",
        "fiyat": 685.0
        },
        {
        "tur": "viski",
        "ad": "100cl Chivas Regal (12 Yıl) Viski",
        "fiyat": 690.0
        },
        {
        "tur": "viski",
        "ad": "175cl Jack Daniels Old No.7 Viski",
        "fiyat": 695.0
        },
        {
        "tur": "viski",
        "ad": "100cl Johnnie Walker Red Label Viski",
        "fiyat": 699.0
        },
        {
        "tur": "viski",
        "ad": "100cl J&B Viski",
        "fiyat": 699.0
        },
        {
        "tur": "viski",
        "ad": "70cl Johnnie Walker Gold Label Reserve Viski",
        "fiyat": 699.0
        },
        {
        "tur": "likor",
        "ad": "50cl Cointreau Likör",
        "fiyat": 700.0
        },
        {
        "tur": "cin",
        "ad": "100cl Bombay Sapphire Cin",
        "fiyat": 720.0
        },
        {
        "tur": "viski",
        "ad": "50cl Chivas Regal (18 Yıllık) Viski",
        "fiyat": 750.0
        },
        {
        "tur": "tekila",
        "ad": "70cl Don Julio Tequila",
        "fiyat": 750.0
        },
        {
        "tur": "cin",
        "ad": "70cl Tanqueray No: 10 Cin",
        "fiyat": 760.0
        },
        {
        "tur": "raki",
        "ad": "150cl Yeni Rakı",
        "fiyat": 799.0
        },
        {
        "tur": "viski",
        "ad": "70cl Jack Daniels No.27 Gold Viski",
        "fiyat": 800.0
        },
        {
        "tur": "raki",
        "ad": "100cl Efe Geleneksel Rakı",
        "fiyat": 807.0
        },
        {
        "tur": "raki",
        "ad": "70cl Efe Organik Rakı",
        "fiyat": 840.5
        },
        {
        "tur": "raki",
        "ad": "100cl Efe Çilingir Xtra Rakı",
        "fiyat": 849.5
        },
        {
        "tur": "votka",
        "ad": "70cl Absolut Elyx Vodka",
        "fiyat": 860.0
        },
        {
        "tur": "viski",
        "ad": "150cl J&B Viski",
        "fiyat": 875.0
        },
        {
        "tur": "raki",
        "ad": "70cl Efe 5 Yıllık Rakı",
        "fiyat": 895.0
        },
        {
        "tur": "viski",
        "ad": "70cl Chivas Mizunara İskoç Viskisi",
        "fiyat": 940.0
        },
        {
        "tur": "likor",
        "ad": "100cl Cointreau Likör",
        "fiyat": 951.0
        },
        {
        "tur": "viski",
        "ad": "70cl Johnnie Walker Green Label 15 Yıllık Viski",
        "fiyat": 980.0
        },
        {
        "tur": "votka",
        "ad": "175cl Absolut Vodka",
        "fiyat": 985.0
        },
        {
        "tur": "viski",
        "ad": "150cl Johnnie Walker Black Label Viski",
        "fiyat": 995.0
        },
        {
        "tur": "viski",
        "ad": "70cl Chivas Regal (18 Yıllık) Viski",
        "fiyat": 1000.0
        },
        {
        "tur": "viski",
        "ad": "70cl Johnnie Walker 18 Yıllık Viski",
        "fiyat": 1050.0
        },
        {
        "tur": "viski",
        "ad": "150cl Johnnie Walker Red Label Viski",
        "fiyat": 1075.0
        },
        {
        "tur": "viski",
        "ad": "300cl Jack Daniels Old No.7 Viski",
        "fiyat": 1175.0
        },
        {
        "tur": "viski",
        "ad": "70cl Ballantines 21 Yıl Viski",
        "fiyat": 1250.0
        },
        {
        "tur": "raki",
        "ad": "70cl Saki Rakı Premium",
        "fiyat": 1250.0
        },
        {
        "tur": "viski",
        "ad": "175cl Chivas Regal (12 Yıl) Viski",
        "fiyat": 1250.0
        },
        {
        "tur": "viski",
        "ad": "100cl Jack Daniels Sinatra Select Viski",
        "fiyat": 1300.0
        },
        {
        "tur": "viski",
        "ad": "300cl Ballantines Finest Viski",
        "fiyat": 1600.0
        },
        {
        "tur": "viski",
        "ad": "300cl Chivas Regal (12 Yıllık) Viski",
        "fiyat": 1850.0
        },
        {
        "tur": "votka",
        "ad": "150cl Absolut Elyx Vodka",
        "fiyat": 1860.0
        },
        {
        "tur": "viski",
        "ad": "300cl Johnnie Walker Black Label Viski",
        "fiyat": 1929.0
        },
        {
        "tur": "viski",
        "ad": "70cl Chivas Regal Royal Salute 21 İskoç Viskisi",
        "fiyat": 2150.0
        },
        {
        "tur": "viski",
        "ad": "300cl Johnnie Walker Red Label Viski",
        "fiyat": 2200.0
        },
        {
        "tur": "viski",
        "ad": "300cl Chivas Regal (12 Yıllık)",
        "fiyat": 2229.0
        },
        {
        "tur": "votka",
        "ad": "450cl Absolut Vodka Blue",
        "fiyat": 2725.0
        },
        {
        "tur": "tekila",
        "ad": "70cl Don Julio 1942 Tequila",
        "fiyat": 3000.0
        },
        {
        "tur": "votka",
        "ad": "300cl Absolut Elyx Vodka",
        "fiyat": 3650.0
        },
        {
        "tur": "viski",
        "ad": "70cl Johnnie Walker Blue Label Viski",
        "fiyat": 4000.0
        },
        {
        "tur": "viski",
        "ad": "70cl Chivas Regal (25 Yıllık) Viski",
        "fiyat": 4990.0
        },
        {
        "tur": "votka",
        "ad": "450cl Absolut Elyx Vodka",
        "fiyat": 6000.0
        },
        {
        "tur": "viski",
        "ad": "70cl Johnnie Walker Sons King George V Viski",
        "fiyat": 7000.0
        }
    ]
    }
  """

  print(piiz.tablo())
  """
  tabulate verisi döndürür.

    +---------+-------------------------------------------------+---------+
    | tur     | ad                                              |   fiyat |
    |---------+-------------------------------------------------+---------|
    | bira    | 33cl Bud Depozitosuz Şişe                       |   21    |
    | bira    | 25cl Efes Malt Depozitosuz Şişe                 |   21    |
    | bira    | 45cl Varım Kutu                                 |   22    |
    | bira    | 45cl Varım Limonlu Kutu                         |   22    |
    | bira    | 23,7cl Tuborg Kırmızı Shot Special Kutu         |   22.5  |
    | bira    | 50cl Bud Kutu Şişe                              |   23    |
    | bira    | 50cl Bud Depozitosuz Şişe                       |   23    |
    | bira    | 33cl Tuborg Gold Depozitosuz Şişe               |   23.5  |
    | bira    | 33cl Tuborg Gold Kutu                           |   23.5  |
    | bira    | 33cl Tuborg Amber Depozitosuz Şişe              |   23.5  |
    | bira    | 33cl Efes Pilsen Kutu                           |   25    |
    | bira    | 33cl Carlsberg Kutu                             |   25.5  |
    | bira    | 33cl Bomonti Red Ale Depozitosuz Şişe           |   26    |
    | bira    | 33cl Bomonti Black Depozitosuz Şişe             |   26    |
    | bira    | 33cl Miller Depozitosuz Şişe                    |   26    |
    | bira    | 33cl Bomonti İpa Depozitosuz Şişe               |   26.5  |
    | bira    | 50cl Carlsberg Kutu                             |   27    |
    | bira    | 33cl Carlsberg Depozitosuz Şişe                 |   27    |
    | bira    | 50cl Tuborg Gold Depozitolu Şişe                |   27.5  |
    | bira    | 50cl Efes Malt Depozitolu Şişe                  |   27.5  |
    | bira    | 35cl Frederic Marzen Lager Şişe                 |   27.5  |
    | bira    | 35cl Frederic India Pale Ale Şişe               |   27.5  |
    | bira    | 35cl Frederic Brown Ale Şişe                    |   27.5  |
    | bira    | 35cl Frederic White Ipa Şişe                    |   27.5  |
    | bira    | 50cl Carlsberg Depozitolu Şişe                  |   27.5  |
    | bira    | 33cl Grimbergen Blonde Depozitosuz Şişe         |   28    |
    | bira    | 33cl Kronenbourg 1664 Blanc Depozitosuz Şişe    |   28    |
    | bira    | 33cl SOL Cerveza Depozitosuz Şişe               |   28    |
    | bira    | 33cl Weihenstephan Depozitosuz Şişe             |   28    |
    | bira    | 33cl Beck's Depozitosuz Şişe                    |   28    |
    | bira    | 50cl Bomonti Depozitolu Şişe                    |   28    |
    | bira    | 50cl Tuborg Gold Kutu                           |   28    |
    | bira    | 50cl Bomonti Depozitosuz Şişe                   |   28.5  |
    | bira    | 50cl Tuborg Amber Kutu                          |   29    |
    | bira    | 50cl Tuborg Gold Depozitosuz Şişe               |   29    |
    | bira    | 50cl Efes Malt Kutu                             |   29    |
    | bira    | 50cl Efes Extra Kutu                            |   29    |
    | bira    | 50cl Efes Pilsen Kutu                           |   29    |
    | bira    | 33cl Efes Brewmaster Red Ale Depozitosuz Şişe   |   29.5  |
    | bira    | 50cl Tuborg Amber Depozitosuz Şişe              |   29.5  |
    | bira    | 50cl Efes Pilsen Depozitolu Uzun Şişe           |   29.5  |
    | bira    | 33cl Efes Brewmaster White Ale Depozitosuz Şişe |   29.5  |
    | bira    | 50cl Bomonti Filtresiz Depozitosuz Şişe         |   30    |
    | bira    | 50cl Tuborg Filtresiz Kutu                      |   30    |
    | bira    | 50cl Tuborg Filtresiz Depozitosuz Şişe          |   30    |
    | bira    | 33cl Grimbergen Double Ambree Depozitosuz Şişe  |   30    |
    | bira    | 33cl Desperados Depozitosuz Şişe                |   31    |
    | bira    | 50cl Bomonti Filtresiz Kutu                     |   31    |
    | bira    | 50cl Tuborg Kırmızı Special Kutu                |   31.5  |
    | bira    | 50cl Beck's Depozitosuz Şişe                    |   32    |
    | bira    | 50cl Beck's Kutu                                |   32    |
    | bira    | 50cl Efes Pilsen Özel Seri Depozitosuz          |   32    |
    | bira    | 33cl Weihenstephan Vitus Depozitosuz Şişe       |   32    |
    | bira    | 50cl Miller Kutu                                |   33    |
    | bira    | 50cl Miller Depozitosuz Şişe                    |   33    |
    | bira    | Efes Glutensiz 50cl                             |   33    |
    | bira    | 50cl Efes Fıçı Yüksek Alkollü Kutu              |   33    |
    | bira    | 50cl Efes Fıçı Yüksek Alkollü Şişe Depozitosuz  |   34    |
    | sarap   | 75cl Sevilen Agora Beyaz Şarap                  |   39    |
    | bira    | 35,5cl Corona Extra Şişe                        |   40    |
    | bira    | 100cl Skol Bira Depozitosuz Pet Şişe            |   40    |
    | bira    | 44cl Guinness Kutu                              |   40.5  |
    | sarap   | 75cl Agora Kırmızı Şarap (Sevilen)              |   41    |
    | sarap   | 75cl Sevilen Altıntepe Kırmızı Şarap            |   41.5  |
    | bira    | 33cl Hoegaarden Depozitosuz Şişe                |   42    |
    | bira    | 33cl Erdinger Depozitosuz Şişe                  |   42    |
    | bira    | 50cl Amsterdam Navigator Depozitosuz Şişe       |   44    |
    | bira    | 50cl Amsterdam Navigator Kutu                   |   44    |
    | sarap   | 75cl Sevilen Kalecik Karası Kırmızı Şarap       |   44.9  |
    | sarap   | 75cl Sevilen Majestik Gamay Kırmızı Şarap       |   44.9  |
    | sarap   | 75cl Sevilen Sultaniye Beyaz Şarap              |   44.9  |
    | bira    | 33cl Leffe Brune Blonde Depozitosuz Şişe        |   45    |
    | bira    | 100cl Marmara Gold Depozitosuz Şişe             |   45    |
    | bira    | 33cl Leffe Brune Depozitosuz Şişe               |   45    |
    | sarap   | 75cl Sevilen Majestik Öküzgözü Kırmızı          |   45.9  |
    | sarap   | 75cl Sevilen Majestik Gamay Kırmızı Şarap       |   45.9  |
    | bira    | 33cl Leffe Radieuse Depozitosuz Şişe            |   48    |
    | kokteyl | 14.4 Çilekli Volim                              |   50    |
    | kokteyl | 14.4 Volim Redbull                              |   50    |
    | kokteyl | 14.4 Volim Limonlu Alkol                        |   50    |
    | kokteyl | Volim Sade                                      |   50    |
    | kokteyl | Volim Karışık Meyveli                           |   50    |
    | kokteyl | Volim Karpuz Aromalı                            |   50    |
    | kokteyl | Volim Kola Aromalı                              |   50    |
    | kokteyl | Volim Shot Karpuz Çilek                         |   50    |
    | kokteyl | Volim Shot Votka İçeçeği                        |   50    |
    | kokteyl | Volim Enerji İçeceği Aromalı                    |   50    |
    | sarap   | 18,75cl Villa Doluca Şarap                      |   50    |
    | bira    | 45cl Grolsch Depozitosuz Şişe                   |   52    |
    | bira    | 33cl Duvel Depozitosuz Şişe                     |   57    |
    | sarap   | 75cl Biricik Sek Beyaz Cam Şarap                |   60    |
    | sarap   | 75cl Biricik Sek Kırmızı CamŞarap               |   60    |
    | sarap   | 75cl Biricik Sek Kırmızı Cam Şarap              |   60    |
    | sarap   | 75cl Biricik Sek Beyaz Cam Şarap                |   60    |
    | raki    | 20cl Saki Rakı Yaş Üzüm                         |   64.5  |
    | sarap   | 75cl Sevilen İsabey Saublanc (Beyaz)            |   79    |
    | sarap   | 75cl Sevilen İsabey Merlot Şarap                |   79.5  |
    | sarap   | 75cl Sevilen İsabey Narince Beyaz Şarap         |   79.5  |
    | sarap   | 75cl Sevilen İsabey Cabarnet                    |   79.5  |
    | sarap   | 100cl Biricik Sek Kırmızı Cam Şarap             |   80    |
    | sarap   | 100cl Biricik Sek Kırmızı Cam Şarap             |   80    |
    | sarap   | 100cl Biricik Sek Beyaz Cam Şarap               |   80    |
    | sarap   | 75cl Mistik Şarap                               |   80    |
    | sarap   | 100cl Biricik Sek Beyaz Cam Şarap               |   80    |
    | sarap   | 37,5cl Villa Doluca Şarap                       |   80    |
    | sarap   | 37,5cl Doluca Şarap                             |   80    |
    | raki    | 35cl Saki Ginseng                               |   88.5  |
    | votka   | 20cl İstanblue Votka                            |   91    |
    | likor   | 50cl Hare Nane Likörü                           |   95    |
    | likor   | 50cl Hare Acıbadem Likörü                       |   95    |
    | likor   | 50cl Hare Muz Likörü                            |   95    |
    | likor   | 50cl Hare Vişne Likörü                          |   95    |
    | likor   | 50cl Hare Hindistan Cevizi Likörü               |   95    |
    | sarap   | 75cl Crama Regala Sauvignon Blanc               |   99.9  |
    | sarap   | 75cl Crama Regala Chardonnay                    |  104.9  |
    | sarap   | 75cl Crama Regala Merlot                        |  104.9  |
    | sarap   | 75cl Crama Regala Cabernet Sauvignon            |  104.9  |
    | sarap   | Biricik Sek Kırmızı-Beyaz-Rose Şarap            |  110    |
    | likor   | 50cl Hare Portakal Likörü                       |  110    |
    | sarap   | 150cl Biricik Galon Kırmızı Cam Şarap           |  118    |
    | sarap   | Biricik Sek Kırmızı-Beyaz-Blush Şarap           |  118    |
    | sarap   | 150cl Biricik Galon Beyaz Cam Şarap             |  118    |
    | sarap   | 150cl Biricik Galon Kırmızı Cam Şarap           |  118    |
    | sarap   | 150cl Biricik Galon Beyaz Cam Şarap             |  118    |
    | likor   | 100cl Hare Kahve, Portakal, Kayısı Likörü       |  125    |
    | likor   | 100cl Hare Çikolata Likörü                      |  125    |
    | likor   | 100cl Hare Acıbadem, Bitter, Nane Likörü        |  125    |
    | likor   | 100cl Hare Şeftali, Muz, Tropikal Likörü        |  125    |
    | sarap   | 75cl Dlc Sultaniye Emir Şarap                   |  130    |
    | sarap   | 75cl Dlc Shiraz Şarap                           |  130    |
    | sarap   | 75cl Dlc Cab. Sauvıgnon-Merlot Şarap            |  130    |
    | sarap   | 75cl Dlc Moskado Şarap                          |  130    |
    | sarap   | 75cl Dlc Kalecik Karası Şarap                   |  130    |
    | sarap   | 75cl Dlc Öküzgözü Şarap                         |  130    |
    | sarap   | 75cl Dlc Boğazkere Şarap                        |  130    |
    | sarap   | 75cl Dlc Sauvıgnon Blanc Şarap                  |  130    |
    | sarap   | 75cl Dlc Frenache Şarap                         |  130    |
    | sarap   | 75cl Dlc Narince Şarap                          |  130    |
    | sarap   | 75cl Doluca Şarap                               |  130    |
    | raki    | 35cl Anadolu Boğma Rakı                         |  130.5  |
    | likor   | 35cl Muz Likörü                                 |  132    |
    | sarap   | 150cl Biricik Kulplu Kırmızı Şarap              |  132    |
    | sarap   | 150cl Biricik Kulplu Beyaz Şarap                |  132    |
    | likor   | 35cl Portakal Likörü                            |  132    |
    | likor   | 35cl Nane Likörü                                |  132    |
    | likor   | 35cl Acıbadem Likörü                            |  132    |
    | likor   | 35cl Ahududu Likörü                             |  132    |
    | likor   | 35cl Vişne Likörü                               |  132    |
    | likor   | 35cl Damla Sakızlı Likör                        |  132    |
    | votka   | 35cl Bazooka Votka                              |  139    |
    | sarap   | 100cl Mistik Şarap                              |  140    |
    | votka   | 35cl İstanblue Votka                            |  140    |
    | raki    | 35cl Ata Rakı                                   |  140    |
    | sarap   | 75cl Villa Doluca Şarap                         |  140    |
    | votka   | 20cl Lithuanian Vodka                           |  140.9  |
    | raki    | 20cl Saki Rakı Klasik                           |  145.5  |
    | raki    | 35cl Yekta Rakı                                 |  149    |
    | raki    | 35cl Burgaz Rakı                                |  149.5  |
    | votka   | 35cl Wyborowa Votka                             |  150    |
    | sarap   | 75cl Villa Doluca Neo Şarap                     |  150    |
    | sarap   | 200cl Biricik Galon Beyaz Cam Şarap             |  155    |
    | sarap   | 200cl Biricik Galon Kırmızı Cam Şarap           |  155    |
    | raki    | 20cl Saki Rakı Altın Seri                       |  156    |
    | cin     | 35cl Gilbey's Cin                               |  159    |
    | raki    | 35cl Tayfa Rakı                                 |  159.5  |
    | votka   | 35cl Gilbey's Votka                             |  160    |
    | cin     | 35cl Stirling Cin                               |  160.9  |
    | viski   | 35cl Jack Daniels Tennessee Honey Viski         |  163    |
    | viski   | 35cl Jack Daniels Tennessee Apple Viski         |  163    |
    | raki    | 70cl Saki Ginseng                               |  164.5  |
    | sarap   | 100cl Doluca Şarap                              |  165    |
    | raki    | 35cl İzmir Rakısı                               |  169    |
    | tekila  | 35cl Olmeca Blanco Tekila                       |  169    |
    | votka   | 35cl Binboa Votka                               |  169    |
    | votka   | 35cl Stumbra Centenary Vodka                    |  170    |
    | viski   | 35cl Ballantines Finest Viski                   |  175    |
    | raki    | 35cl Saki Rakı Klasik                           |  175.2  |
    | raki    | 35cl İzmir Rakısı Yaş Üzüm                      |  175.5  |
    | raki    | 35cl Yeni Rakı                                  |  176.75 |
    | viski   | 20cl Chivas Regal (12 Yıllık) Viski             |  179    |
    | kokteyl | 100cl Volim                                     |  180    |
    | raki    | 35cl İzmir Rakısı Göbek                         |  185    |
    | votka   | 35cl Smirnoff Red Votka                         |  185    |
    | tekila  | 35cl Olmeca Gold Tekila                         |  189    |
    | votka   | 50cl Bazooka Votka                              |  189    |
    | kokteyl | Kırbıyık Kokteyl Mojito 100cl                   |  190    |
    | kokteyl | Kırbıyık Kokteyl Cosmopolitan 100cl             |  190    |
    | kokteyl | Kırbıyık Kokteyl Sek On The Beach 100cl         |  190    |
    | kokteyl | Kırbıyık Kokteyl Orman Meyveli 100cl            |  190    |
    | kokteyl | Kırbıyık Kokteyl Margarita 100cl                |  190    |
    | kokteyl | Bue Hawaii 100cl                                |  190    |
    | kokteyl | Kırbıyık Kokteyl Kavun 100cl                    |  190    |
    | kokteyl | Kırbıyık Kokteyl Karpuz Çilek 100cl             |  190    |
    | kokteyl | Harrley's Irish Cream 100cl                     |  190    |
    | likor   | 100cl Hare Portakal Likörü                      |  190    |
    | tekila  | 70cl El Jimador Blanco Tequila                  |  195    |
    | votka   | 50cl İstanblue Votka                            |  195    |
    | raki    | 20cl Saki Rakı Siyah Üzüm                       |  195.5  |
    | raki    | 35cl Yeni Rakı Yeni Seri                        |  199    |
    | raki    | 35cl Tekirdağ Rakı                              |  199    |
    | cin     | 35cl Gordon's Dry Cin                           |  199    |
    | raki    | 35cl Saki Rakı Altın Seri                       |  199.5  |
    | raki    | 35cl Tekirdağ Rakı Trakya Serisi                |  199.5  |
    | votka   | 35cl Lithuanian Vodka                           |  199.9  |
    | raki    | 35cl Efe Yaş Üzüm Rakı                          |  200    |
    | raki    | 35cl Tekirdağ Rakı Kavrulmuş Anason             |  200    |
    | raki    | 35cl Saki Rakı Yaş Üzüm                         |  200.5  |
    | viski   | 35cl Ballantines 12 Yıl Viski                   |  205    |
    | votka   | 50cl Wyborowa Votka                             |  205    |
    | viski   | 35cl Jack Daniels Old No.7 Viski                |  205.5  |
    | raki    | 35cl Tekirdağ Rakı Altın Seri                   |  209    |
    | votka   | 35cl Absolut Vodka                              |  209    |
    | raki    | 35cl Efe Gold Rakı                              |  209.5  |
    | tekila  | 70cl El Jimador Reposado Tequila                |  210    |
    | cin     | 35cl Beefeater Cin                              |  210    |
    | likor   | 100cl Garrone Ricard Likör                      |  210    |
    | raki    | 35cl Yeni Rakı Ustaların Karışımı               |  215.5  |
    | viski   | 35cl Bell's Viski                               |  219    |
    | raki    | 50cl Tayfa Rakı                                 |  219    |
    | raki    | 35cl Efe Çilingir Xtra Rakı                     |  220.5  |
    | likor   | 100cl Garrone Rosso Likör                       |  225    |
    | likor   | 35cl Jagermeister                               |  225    |
    | likor   | 100cl Garrone Bianco Dry Likör                  |  225    |
    | votka   | 50cl Stumbra Centenary Vodka                    |  225.9  |
    | raki    | 35cl Efe Tek İmbik Rakı                         |  226    |
    | raki    | 35cl Yeni Rakı Âlâ                              |  229    |
    | raki    | 50cl Burgaz Rakı                                |  229    |
    | raki    | 35cl Kulüp Rakı                                 |  229.5  |
    | cin     | 50cl Stirling Cin                               |  230.9  |
    | sarap   | 150cl Mistik Şarap                              |  235    |
    | tekila  | 50cl Olmeca Blanco Tekila                       |  235    |
    | raki    | 70cl Anadolu Boğma Rakı                         |  235    |
    | raki    | 35cl Beylerbeyi Göbek Rakısı                    |  235    |
    | raki    | 50cl İzmir Rakısı                               |  239.5  |
    | sarap   | 300cl Biricik Kulplu Beyaz Şarap                |  240    |
    | sarap   | Biricik Suni Yarı Köpüren Şarap (Beyaz-Rose)    |  240    |
    | raki    | 35cl Altınbaş Rakı                              |  240    |
    | sarap   | 300cl Biricik Kulplu Kırmızı Şarap              |  240    |
    | viski   | 50cl Ballantines Finest Viski                   |  245    |
    | raki    | 50cl İzmir Rakısı Yaş Üzüm                      |  245    |
    | viski   | 35cl J&B Viski                                  |  245    |
    | viski   | 35cl Johnnie Walker Black Label Viski           |  245    |
    | raki    | 35cl Saki Rakı Siyah Üzüm                       |  245.5  |
    | raki    | 35cl Efe Klasik Rakı                            |  245.5  |
    | votka   | 50cl Smirnoff Red                               |  249.5  |
    | raki    | 50cl Efe Klasik Rakı                            |  249.5  |
    | raki    | 35cl Efe Çilingir Xtra Yaş Üzüm Rakı            |  249.9  |
    | raki    | 35cl Efe 3 Distile Rakı                         |  250    |
    | raki    | 35cl Efe Geleneksel Rakı                        |  250.9  |
    | raki    | 50cl Saki Rakı Klasik                           |  250.9  |
    | raki    | 35cl Efe Çilingir Rakı                          |  251.9  |
    | raki    | 35cl Efe Sarı Zeybek Rakı                       |  257    |
    | votka   | 70cl Bazooka Votka                              |  260    |
    | votka   | 70cl İstanblue Votka                            |  265.5  |
    | votka   | 70cl Lithuanian Vodka                           |  269.9  |
    | raki    | 70cl Ata Rakı                                   |  271    |
    | raki    | 50cl Tekirdağ Rakı                              |  275    |
    | votka   | 70cl Wyborowa Votka                             |  275    |
    | viski   | 35cl Johnnie Walker Red Label Viski             |  275    |
    | viski   | 50cl Jack Daniels Old No.7 Viski                |  279    |
    | viski   | 35cl Chivas Regal (12 Yıllık) Viski             |  279.4  |
    | votka   | 50cl Lithuanian Vodka                           |  280.9  |
    | raki    | 50cl Efe Yaş Üzüm Rakı                          |  281    |
    | viski   | 50cl Ballantines 12 Yıl Viski                   |  285    |
    | viski   | 50cl Bell's Viski                               |  285.9  |
    | votka   | 50cl Absolut Vodka                              |  288    |
    | raki    | 50cl Yeni Rakı Yeni Seri                        |  289    |
    | raki    | 50cl Yeni Rakı                                  |  289.5  |
    | raki    | 50cl Efe Gold Rakı                              |  295    |
    | votka   | 70cl Binboa Pier Ginger Votka                   |  295    |
    | votka   | 70cl Binboa Red Orange                          |  295    |
    | votka   | 50cl Binboa Votka                               |  295    |
    | votka   | 70cl Binboa Red Apple                           |  295    |
    | votka   | 70cl Binboa Satsuma Votka                       |  295    |
    | votka   | 70cl Binboa Mojito                              |  295    |
    | votka   | 70cl Gilbey's Votka                             |  295    |
    | raki    | 50cl Tekirdağ Rakı Altın Seri                   |  295    |
    | raki    | 50cl Saki Rakı Yaş Üzüm                         |  295.9  |
    | raki    | 50cl Saki Rakı Altın Seri                       |  295.9  |
    | raki    | 70cl Tayfa Rakı                                 |  299    |
    | raki    | 70cl Burgaz Rakı                                |  300    |
    | viski   | 70cl Jack Daniels Tennessee Honey Viski         |  300    |
    | viski   | 70cl Jack Daniels Tennessee Apple Viski         |  300    |
    | cin     | 75cl Stirling Cin                               |  300.9  |
    | raki    | 50cl Beylerbeyi Göbek Rakısı                    |  305    |
    | votka   | 70cl Smirnoff North                             |  309    |
    | votka   | 70cl Stumbra Centenary Vodka                    |  310.9  |
    | viski   | 70cl Jack Daniels Special Edition Viski         |  320    |
    | raki    | 70cl Yekta Rakı                                 |  325    |
    | tekila  | 70cl Olmeca Blanco Tekila                       |  325    |
    | tekila  | 70cl Olmeca Dark Chocolate                      |  325    |
    | raki    | 70cl İzmir Rakısı                               |  325    |
    | raki    | 70cl İzmir Rakısı Yaş Üzüm                      |  330    |
    | viski   | 70cl Ballantines Finest Viski                   |  330    |
    | likor   | 70cl Jagermeister                               |  335    |
    | raki    | 70cl İzmir Rakısı Göbek                         |  335    |
    | raki    | 70cl Saki Rakı Klasik                           |  335.5  |
    | viski   | 50cl Johnnie Walker Black Label Viski           |  339    |
    | raki    | 70cl Efe Klasik Rakı                            |  339.5  |
    | raki    | 70cl Efe 3 Distile Rakı                         |  340.5  |
    | raki    | 50cl Saki Rakı Siyah Üzüm                       |  345.5  |
    | votka   | 70cl Smirnoff Red                               |  349    |
    | votka   | 70cl Smirnoff Espresso                          |  359    |
    | votka   | 70cl Smirnoff Green Apple                       |  359    |
    | votka   | 70cl Smirnoff Peppermint (Nane)                 |  359    |
    | votka   | 70cl Smirnoff Citrus (Narenciye)                |  359    |
    | votka   | 70cl Smirnoff Rasberry (Ahududu)                |  359    |
    | votka   | 70cl Smirnoff Apple (Elma) Red                  |  359    |
    | votka   | 70cl Smirnoff Vanilla (Vanilya)                 |  359    |
    | votka   | 70cl Smirnoff Orange (Portakal)                 |  359    |
    | viski   | 50cl Chivas Regal (12 Yıllık) Viski             |  359    |
    | tekila  | 70cl Olmeca Gold Tekila                         |  360    |
    | viski   | 70cl Ballantine's 7 İskoç Viski                 |  360    |
    | votka   | 100cl Bazooka Votka                             |  360    |
    | raki    | 70cl Yeni Rakı Yeni Seri                        |  369    |
    | votka   | 100cl İstanblue Votka                           |  370    |
    | raki    | 70cl Efe Yaş Üzüm Rakı                          |  373    |
    | cin     | 70cl Gilbey's Cin                               |  375    |
    | raki    | 70cl Tekirdağ Rakı                              |  375.5  |
    | raki    | 70cl Saki Rakı Yaş Üzüm                         |  375.5  |
    | raki    | 70cl Tekirdağ Rakı Trakya Serisi                |  375.5  |
    | votka   | 70cl Absolut Vodka Mandrin                      |  377    |
    | votka   | 70cl Absolut Vodka Vanilia                      |  377    |
    | votka   | 70cl Absolut Vodka Raspberri                    |  377    |
    | votka   | 70cl Absolut Extrakt Vodka                      |  377    |
    | votka   | 70cl Absolut Vodka                              |  377    |
    | votka   | 70cl Absolut Lime Vodka                         |  377    |
    | votka   | 70cl Absolut Vodka Apeach                       |  377    |
    | votka   | 70cl Absolut Citron Vodka                       |  377    |
    | votka   | 70cl Absolut Pears Vodka                        |  377    |
    | raki    | 70cl Yeni Rakı                                  |  379.5  |
    | viski   | 70cl Jack Daniels Old No.7 Viski                |  380    |
    | viski   | 50cl J&B Viski                                  |  380    |
    | viski   | 50cl Johnnie Walker Red Label Viski             |  380    |
    | likor   | 35cl Cointreau Likör                            |  381    |
    | votka   | 100cl Wyborowa Votka                            |  385    |
    | viski   | 70cl Ballantines 12 Yıl Viski                   |  390    |
    | cin     | 70cl Beefeater Pink Cin                         |  395    |
    | raki    | 70cl Saki Rakı Altın Seri                       |  395.9  |
    | cin     | 70cl Beefeater Cin                              |  396    |
    | viski   | 70cl Bell's Viski                               |  399    |
    | cin     | 70cl Gordon's Dry Cin                           |  399    |
    | raki    | 70cl Efe Gold Rakı                              |  399    |
    | raki    | 70cl Tekirdağ Rakı Altın Seri                   |  399    |
    | raki    | 70cl Tekirdağ Rakı Kavrulmuş Anason             |  400    |
    | votka   | 100cl Lithuanian Vodka                          |  400.9  |
    | viski   | 100cl Jack Daniels Tennessee Honey Viski        |  405    |
    | viski   | 100cl Jack Daniels Tennessee Apple Viski        |  405    |
    | raki    | 70cl Yeni Rakı Ustaların Karışımı               |  409    |
    | raki    | 100cl Tayfa Rakı                                |  410.5  |
    | raki    | 70cl Efe Tek İmbik Rakı                         |  415    |
    | votka   | 70cl Binboa Votka                               |  419    |
    | cin     | 100cl Stirling Cin                              |  419.9  |
    | votka   | 100cl Gilbey's Votka                            |  420    |
    | raki    | 70cl Efe Geleneksel Rakı                        |  420.5  |
    | raki    | 70cl Efe Çilingir Rakı                          |  425.5  |
    | raki    | 70cl Beylerbeyi Göbek Rakısı                    |  429    |
    | raki    | 70cl Kulüp Rakı                                 |  430    |
    | raki    | 70cl Yeni Rakı Âlâ                              |  435    |
    | votka   | 100cl Stumbra Centenary Vodka                   |  435.9  |
    | tekila  | 70cl Olmeca Altos Plata Tekila                  |  440    |
    | raki    | 70cl Efe Çilingir Xtra Rakı                     |  440.9  |
    | raki    | 100cl Saki Rakı Klasik                          |  440.9  |
    | raki    | 70cl Saki Rakı Siyah Üzüm                       |  445.5  |
    | viski   | 70cl Johnnie Walker Black Label Viski           |  449    |
    | raki    | 100cl İzmir Rakısı                              |  449.5  |
    | raki    | 70cl Efe Çilingir Xtra Yaş Üzüm Rakı            |  449.9  |
    | tekila  | 70cl Olmeca Altos Reposadd                      |  450    |
    | raki    | 100cl Yekta Rakı                                |  450.5  |
    | likor   | 100cl Jagermeister                              |  452.5  |
    | viski   | 100cl Ballantines Finest Viski                  |  455    |
    | tekila  | 100cl Olmeca Blanco Tekila                      |  455    |
    | raki    | 100cl İzmir Rakısı Yaş Üzüm                     |  459.5  |
    | raki    | 70cl Altınbaş Rakı                              |  460    |
    | raki    | 70cl Efe Sarı Zeybek Rakı                       |  469.5  |
    | cin     | 70cl Gordon's Pink Cin                          |  475    |
    | raki    | 100cl Efe Klasik Rakı                           |  475.5  |
    | viski   | 70cl Chivas Regal (12 Yıl) Viski                |  479    |
    | cin     | 100cl Gilbey's Cin                              |  481    |
    | viski   | 70cl Chivas Regal (13 Yıllık) İskoç Viskisi     |  490    |
    | viski   | 70cl Jack Daniels Single Barrel Viski           |  495    |
    | votka   | 100cl Smirnoff Red                              |  499    |
    | raki    | 100cl Yeni Rakı                                 |  499.5  |
    | raki    | 100cl Yeni Rakı Yeni Seri                       |  499.5  |
    | viski   | 70cl J&B Viski                                  |  500    |
    | viski   | 70cl Johnnie Walker Red Label Viski             |  500    |
    | raki    | 100cl Efe Yaş Üzüm Rakı                         |  504.5  |
    | viski   | 100cl Jack Daniels Old No.7 Viski               |  515    |
    | raki    | 100cl Tekirdağ Rakı                             |  519    |
    | votka   | 100cl Absolut Vodka                             |  525    |
    | raki    | 100cl Saki Rakı Yaş Üzüm                        |  525.9  |
    | raki    | 70cl Tekirdağ Rakı No. 10                       |  529    |
    | cin     | 70cl Malfy Con Limone                           |  535    |
    | cin     | 70cl Malfy Gın Rose                             |  535    |
    | cin     | 70cl Malfy Originale Cin                        |  535    |
    | viski   | 100cl Ballantines 12 Yıl Viski                  |  540    |
    | raki    | 100cl Tekirdağ Rakı Altın Seri                  |  549.5  |
    | raki    | 100cl Efe Gold Rakı                             |  549.5  |
    | raki    | 100cl Saki Rakı Altın Seri                      |  549.9  |
    | viski   | 100cl Bell's Viski                              |  550.5  |
    | raki    | 100cl Beylerbeyi Göbek Rakısı                   |  569    |
    | raki    | 100cl Efe Çilingir Rakı                         |  579.5  |
    | raki    | 100cl Efe Tek İmbik Rakı                        |  580.5  |
    | cin     | 70cl Tanqueray Cin (London Dry Gin)             |  583    |
    | tekila  | 70cl Avion Silver                               |  600    |
    | cin     | 70cl Tanqueray Flor De Sevilla Cin              |  625    |
    | viski   | 100cl Johnnie Walker Black Label Viski          |  639    |
    | viski   | 70cl Chivas Regal (15 Yıllık) Viski             |  649    |
    | tekila  | 70cl Avion Reposadd                             |  650    |
    | viski   | 70cl Johnnie Walker Double Black Viski          |  650    |
    | viski   | 70cl Ballantine's 17 İskoç Viski                |  660    |
    | viski   | 150cl Ballantines Finest Viski                  |  685    |
    | viski   | 100cl Chivas Regal (12 Yıl) Viski               |  690    |
    | viski   | 175cl Jack Daniels Old No.7 Viski               |  695    |
    | viski   | 100cl Johnnie Walker Red Label Viski            |  699    |
    | viski   | 100cl J&B Viski                                 |  699    |
    | viski   | 70cl Johnnie Walker Gold Label Reserve Viski    |  699    |
    | likor   | 50cl Cointreau Likör                            |  700    |
    | cin     | 100cl Bombay Sapphire Cin                       |  720    |
    | viski   | 50cl Chivas Regal (18 Yıllık) Viski             |  750    |
    | tekila  | 70cl Don Julio Tequila                          |  750    |
    | cin     | 70cl Tanqueray No: 10 Cin                       |  760    |
    | raki    | 150cl Yeni Rakı                                 |  799    |
    | viski   | 70cl Jack Daniels No.27 Gold Viski              |  800    |
    | raki    | 100cl Efe Geleneksel Rakı                       |  807    |
    | raki    | 70cl Efe Organik Rakı                           |  840.5  |
    | raki    | 100cl Efe Çilingir Xtra Rakı                    |  849.5  |
    | votka   | 70cl Absolut Elyx Vodka                         |  860    |
    | viski   | 150cl J&B Viski                                 |  875    |
    | raki    | 70cl Efe 5 Yıllık Rakı                          |  895    |
    | viski   | 70cl Chivas Mizunara İskoç Viskisi              |  940    |
    | likor   | 100cl Cointreau Likör                           |  951    |
    | viski   | 70cl Johnnie Walker Green Label 15 Yıllık Viski |  980    |
    | votka   | 175cl Absolut Vodka                             |  985    |
    | viski   | 150cl Johnnie Walker Black Label Viski          |  995    |
    | viski   | 70cl Chivas Regal (18 Yıllık) Viski             | 1000    |
    | viski   | 70cl Johnnie Walker 18 Yıllık Viski             | 1050    |
    | viski   | 150cl Johnnie Walker Red Label Viski            | 1075    |
    | viski   | 300cl Jack Daniels Old No.7 Viski               | 1175    |
    | viski   | 70cl Ballantines 21 Yıl Viski                   | 1250    |
    | raki    | 70cl Saki Rakı Premium                          | 1250    |
    | viski   | 175cl Chivas Regal (12 Yıl) Viski               | 1250    |
    | viski   | 100cl Jack Daniels Sinatra Select Viski         | 1300    |
    | viski   | 300cl Ballantines Finest Viski                  | 1600    |
    | viski   | 300cl Chivas Regal (12 Yıllık) Viski            | 1850    |
    | votka   | 150cl Absolut Elyx Vodka                        | 1860    |
    | viski   | 300cl Johnnie Walker Black Label Viski          | 1929    |
    | viski   | 70cl Chivas Regal Royal Salute 21 İskoç Viskisi | 2150    |
    | viski   | 300cl Johnnie Walker Red Label Viski            | 2200    |
    | viski   | 300cl Chivas Regal (12 Yıllık)                  | 2229    |
    | votka   | 450cl Absolut Vodka Blue                        | 2725    |
    | tekila  | 70cl Don Julio 1942 Tequila                     | 3000    |
    | votka   | 300cl Absolut Elyx Vodka                        | 3650    |
    | viski   | 70cl Johnnie Walker Blue Label Viski            | 4000    |
    | viski   | 70cl Chivas Regal (25 Yıllık) Viski             | 4990    |
    | votka   | 450cl Absolut Elyx Vodka                        | 6000    |
    | viski   | 70cl Johnnie Walker Sons King George V Viski    | 7000    |
    +---------+-------------------------------------------------+---------+
  """

  print(piiz.anahtarlar)
  """
  kullanılan anahtar listesini döndürür.

  ['tur', 'adprint(piiz.tablo())', 'fiyat']
  """