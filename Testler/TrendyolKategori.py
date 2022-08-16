from KekikSpatula import TrendyolKategori

trendyol_kategori = TrendyolKategori(kategori_adi="Taşınabilir Disk", sayfa_sayisi=1)

print(trendyol_kategori.veri)
"""
json verisi döndürür

{'kaynak': 'trendyol.com', 'veri': [{'link': 'https://www.trendyol.com/quantum/rdx-320-gb-2-5-usb-3-0-kirmizi-tasinabilir-disk-p-35426025', 'marka': 'Quantum', 'yildiz': 3, 'baslik': 'Rdx 320 Gb 2.5" Usb 3.0 Kırmızı Taşınabilir Disk', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '149 TL', 'fiyat': '144,53 TL'}, {'link': 'https://www.trendyol.com/realindirim/2-5-usb-3-0-harici-harddisk-hdd-kutusu-sata-disk-ssd-veri-aktarma-5-gbps-aluminyum-govde-p-33685614', 'marka': 'Realindirim', 'yildiz': 2, 'baslik': '2.5 Usb 3.0 Harici Harddisk Hdd Kutusu Sata Disk Ssd Veri Aktarma 5 Gbps Aluminyum Gövde', 'indirim': None, 'indirimsiz': None, 'fiyat': '46,50 TL'}, {'link': 'https://www.trendyol.com/kingston/datatraveler-g4-usb-3-0-bellek-32gb-dtig4-32gb-p-2516328', 'marka': 'Kingston', 'yildiz': 4, 'baslik': 'DataTraveler G4 Usb 3.0 Bellek 32GB DTIG4/32GB', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '52,41 TL', 'fiyat': '50,84 TL'}, {'link': 'https://www.trendyol.com/zore/3-0-lightning-metal-otg-64-gb-iphone-veri-ve-fotograf-depolama-kopyalama-flash-disc-p-102334392', 'marka': 'zore', 'yildiz': 0, 'baslik': '3.0 Lightning Metal Otg 64 Gb Iphone Veri Ve Fotoğraf Depolama Kopyalama Flash Disc', 'indirim': None, 'indirimsiz': None, 'fiyat': '141,55 TL'}, {'link': 'https://www.trendyol.com/zore/3-0-lightning-metal-otg-32-gb-iphone-veri-ve-fotograf-depolama-kopyalama-flash-disc-p-102333696', 'marka': 'zore', 'yildiz': 5, 'baslik': '3.0 Lightning Metal Otg 32 Gb Iphone Veri Ve Fotoğraf Depolama Kopyalama Flash Disc', 'indirim': None, 'indirimsiz': None, 'fiyat': '113,05 TL'}, {'link': 'https://www.trendyol.com/wd/3-5-8tb-elements-usb-3-0-siyah-tasinabilir-disk-wdbwlg0080hbk-eesn-p-6018856', 'marka': 'WD', 'yildiz': 4, 'baslik': "3.5'' 8TB Elements USB 3.0 Siyah Taşınabilir Disk WDBWLG0080HBK-EESN", 'indirim': None, 'indirimsiz': None, 'fiyat': '2.399,99 TL'}, {'link': 'https://www.trendyol.com/wd/my-passport-2tb-2-5-usb-3-0-siyah-backup-tasinabilir-disk-wdbs4b0020bbk-wesn-p-4066211', 'marka': 'WD', 'yildiz': 4, 'baslik': 'My Passport 2TB 2.5" USB 3.0 Siyah Backup Taşınabilir Disk WDBS4B0020BBK-WESN', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '700 TL', 'fiyat': '679 TL'}, {'link': 'https://www.trendyol.com/wd/my-passport-black-worldwide-5tb-2-5-tasinabilir-disk-wdbpkj0050bbk-wesn-p-37040645', 'marka': 'WD', 'yildiz': 4, 'baslik': 'My Passport Black Worldwide 5TB 2.5" Taşınabilir Disk WDBPKJ0050BBK-WESN', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '1.348 TL', 'fiyat': '1.307,56 TL'}, {'link': 'https://www.trendyol.com/appa/2-5-usb-3-0-sata-seffaf-harddisk-kutusu-srf-814-hdd-p-36339629', 'marka': 'Appa', 'yildiz': 4, 'baslik': '2.5" Usb 3.0 Sata Şeffaf Harddisk Kutusu Srf-814-hdd', 'indirim': None, 'indirimsiz': None, 'fiyat': '75 TL'}, {'link': 'https://www.trendyol.com/wd/purple-3-5-1tb-7200rpm-64mb-sata-3-6gb-s-7-24-wd10purz-p-2925859', 'marka': 'WD', 'yildiz': 3, 'baslik': 'Purple 3.5 1TB 7200Rpm 64Mb Sata 3 6Gb/s 7/24 WD10PURZ', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '481 TL', 'fiyat': '466,57 TL'}, {'link': 'https://www.trendyol.com/techmaster/aluminyum-hdd-caddy-notebook-pc-dvd-to-ssd-kutu-sata-9-5mm-db-095-p-48603988', 'marka': 'Techmaster', 'yildiz': 4, 'baslik': 'Alüminyum Hdd Caddy Notebook Pc Dvd To Ssd Kutu Sata 9.5mm Db-095', 'indirim': None, 'indirimsiz': None, 'fiyat': '28,40 TL'}, {'link': 'https://www.trendyol.com/wd/my-passport-2tb-2-5-inc-usb-3-2-mavi-tasinabilir-disk-byvg0020bbl-wesn-p-34888668', 'marka': 'WD', 'yildiz': 4, 'baslik': 'My Passport 2tb 2.5 Inc Usb 3.2 Mavi Taşınabilir Disk Byvg0020bbl-wesn', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '699 TL', 'fiyat': '678,03 TL'}, {'link': 'https://www.trendyol.com/sandisk/ultra-sdhc-80mb-s-class-10-uhs-i-hafiza-karti-64-gb-sdsdunc-064g-gn6in-p-2695265', 'marka': 'SanDisk', 'yildiz': 4, 'baslik': 'Ultra SDHC 80MB/s Class 10 UHS-I Hafıza Kartı 64 GB SDSDUNC-064G-GN6IN', 'indirim': None, 'indirimsiz': None, 'fiyat': '88,90 TL'}, {'link': 'https://www.trendyol.com/compaxe/2-5-hdd-external-case-usb-2-0-p-49809949', 'marka': 'COMPAXE', 'yildiz': 4, 'baslik': '2.5 Hdd External Case Usb 2.0', 'indirim': None, 'indirimsiz': None, 'fiyat': '50,66 TL'}, {'link': 'https://www.trendyol.com/maxtor/m3-1tb-2-5-usb-3-0-tasinabilir-harddisk-p-34204470', 'marka': 'Maxtor', 'yildiz': 4, 'baslik': 'M3 1tb 2.5" Usb 3.0 Taşınabilir Harddisk', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '499 TL', 'fiyat': '484,03 TL'}, {'link': 'https://www.trendyol.com/hadron/hd4631-500-usb-3-0-hdd-kablosu-50-cm-p-31651466', 'marka': 'HADRON', 'yildiz': 4, 'baslik': 'Hd4631/500 Usb 3.0 Hdd Kablosu 50 cm', 'indirim': None, 'indirimsiz': None, 'fiyat': '43,16 TL'}, {'link': 'https://www.trendyol.com/wozlo/jonsbo-m-2-ssd-aluminyum-isi-emici-termal-pedli-sogutucu-rgb-p-102090261', 'marka': 'WOZLO', 'yildiz': 0, 'baslik': 'Jonsbo M.2 Ssd Alüminyum Isı Emici Termal Pedli Soğutucu Rgb', 'indirim': None, 'indirimsiz': None, 'fiyat': '154,90 TL'}, {'link': 'https://www.trendyol.com/platoon/m-sata-ssd-hardisk-kutusu-usb-3-0-msata-to-usb-m-sata-usb-3-0-kutu-p-99227691', 'marka': 'Platoon', 'yildiz': 0, 'baslik': 'M Sata Ssd Hardisk Kutusu Usb 3.0 Msata To Usb M-sata Usb 3.0 Kutu', 'indirim': None, 'indirimsiz': None, 'fiyat': '83,60 TL'}, {'link': 'https://www.trendyol.com/wozlo/msata-ssd-to-2-5-inc-sata-6gbps-disk-donusturucu-p-92567404', 'marka': 'WOZLO', 'yildiz': 0, 'baslik': 'Msata Ssd To 2.5 Inç Sata 6gbps Disk Dönüştürücü', 'indirim': None, 'indirimsiz': None, 'fiyat': '54,90 TL'}, {'link': 'https://www.trendyol.com/intenso/siyah-tasinabilir-hard-disk-4tb-2-5-usb-3-0-p-52475114', 'marka': 'Intenso', 'yildiz': 4, 'baslik': 'Siyah Taşınabilir Hard Disk 4tb 2.5" Usb 3.0', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '914 TL', 'fiyat': '886,58 TL'}, {'link': 'https://www.trendyol.com/toshiba/toshiba-canvio-basic-2-5-1tb-usb3-0-siyah-p-2824316', 'marka': 'Toshiba', 'yildiz': 5, 'baslik': 'Toshıba Canvıo Basıc 2.5" 1Tb Usb3.0-Siyah', 'indirim': None, 'indirimsiz': None, 'fiyat': '407 TL'}, {'link': 'https://www.trendyol.com/seagate/6tb-3-5-backup-plus-hub-stel6000200-usb-3-0-harici-harddisk-siyah-p-2925770', 'marka': 'Seagate', 'yildiz': 4, 'baslik': '6tb 3.5" Backup Plus Hub Stel6000200 Usb 3.0 Harici Harddisk Siyah', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '1.599,99 TL', 'fiyat': '1.551,99 TL'}, {'link': 'https://www.trendyol.com/intenso/siyah-tasinabilir-harddisk-2tb-2-5-usb-3-0-p-40177524', 'marka': 'Intenso', 'yildiz': 4, 'baslik': 'Siyah Taşınabilir Harddisk 2tb 2.5" Usb 3.0', 'indirim': 'Sepette %3 İndirim', 'indirimsiz': '557,90 TL', 'fiyat': '541,16 TL'}, {'link': 'https://www.trendyol.com/asus/wsd-a1-32gb-ssd-usb-2-0-wi-fi-harici-disk-p-2826731', 'marka': 'ASUS', 'yildiz': 4, 'baslik': 'WSD-A1-32GB SSD USB 2.0 WI-FI HARICI DISK', 'indirim': None, 'indirimsiz': None, 'fiyat': '1.052,55 TL'}]}
"""

print(trendyol_kategori.gorsel())
"""
oluşan json verisini insanın okuyabileceği formatta döndürür.

{
  "kaynak": "trendyol.com",
  "veri": [
    {
      "link": "https://www.trendyol.com/quantum/rdx-320-gb-2-5-usb-3-0-kirmizi-tasinabilir-disk-p-35426025",
      "marka": "Quantum",
      "yildiz": 3,
      "baslik": "Rdx 320 Gb 2.5\" Usb 3.0 Kırmızı Taşınabilir Disk",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "149 TL",
      "fiyat": "144,53 TL"
    },
    {
      "link": "https://www.trendyol.com/realindirim/2-5-usb-3-0-harici-harddisk-hdd-kutusu-sata-disk-ssd-veri-aktarma-5-gbps-aluminyum-govde-p-33685614",
      "marka": "Realindirim",
      "yildiz": 2,
      "baslik": "2.5 Usb 3.0 Harici Harddisk Hdd Kutusu Sata Disk Ssd Veri Aktarma 5 Gbps Aluminyum Gövde",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "46,50 TL"
    },
    {
      "link": "https://www.trendyol.com/kingston/datatraveler-g4-usb-3-0-bellek-32gb-dtig4-32gb-p-2516328",
      "marka": "Kingston",
      "yildiz": 4,
      "baslik": "DataTraveler G4 Usb 3.0 Bellek 32GB DTIG4/32GB",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "52,41 TL",
      "fiyat": "50,84 TL"
    },
    {
      "link": "https://www.trendyol.com/zore/3-0-lightning-metal-otg-64-gb-iphone-veri-ve-fotograf-depolama-kopyalama-flash-disc-p-102334392",
      "marka": "zore",
      "yildiz": 0,
      "baslik": "3.0 Lightning Metal Otg 64 Gb Iphone Veri Ve Fotoğraf Depolama Kopyalama Flash Disc",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "141,55 TL"
    },
    {
      "link": "https://www.trendyol.com/zore/3-0-lightning-metal-otg-32-gb-iphone-veri-ve-fotograf-depolama-kopyalama-flash-disc-p-102333696",
      "marka": "zore",
      "yildiz": 5,
      "baslik": "3.0 Lightning Metal Otg 32 Gb Iphone Veri Ve Fotoğraf Depolama Kopyalama Flash Disc",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "113,05 TL"
    },
    {
      "link": "https://www.trendyol.com/wd/3-5-8tb-elements-usb-3-0-siyah-tasinabilir-disk-wdbwlg0080hbk-eesn-p-6018856",
      "marka": "WD",
      "yildiz": 4,
      "baslik": "3.5'' 8TB Elements USB 3.0 Siyah Taşınabilir Disk WDBWLG0080HBK-EESN",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "2.399,99 TL"
    },
    {
      "link": "https://www.trendyol.com/wd/my-passport-2tb-2-5-usb-3-0-siyah-backup-tasinabilir-disk-wdbs4b0020bbk-wesn-p-4066211",
      "marka": "WD",
      "yildiz": 4,
      "baslik": "My Passport 2TB 2.5\" USB 3.0 Siyah Backup Taşınabilir Disk WDBS4B0020BBK-WESN",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "700 TL",
      "fiyat": "679 TL"
    },
    {
      "link": "https://www.trendyol.com/wd/my-passport-black-worldwide-5tb-2-5-tasinabilir-disk-wdbpkj0050bbk-wesn-p-37040645",
      "marka": "WD",
      "yildiz": 4,
      "baslik": "My Passport Black Worldwide 5TB 2.5\" Taşınabilir Disk WDBPKJ0050BBK-WESN",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "1.348 TL",
      "fiyat": "1.307,56 TL"
    },
    {
      "link": "https://www.trendyol.com/appa/2-5-usb-3-0-sata-seffaf-harddisk-kutusu-srf-814-hdd-p-36339629",
      "marka": "Appa",
      "yildiz": 4,
      "baslik": "2.5\" Usb 3.0 Sata Şeffaf Harddisk Kutusu Srf-814-hdd",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "75 TL"
    },
    {
      "link": "https://www.trendyol.com/wd/purple-3-5-1tb-7200rpm-64mb-sata-3-6gb-s-7-24-wd10purz-p-2925859",
      "marka": "WD",
      "yildiz": 3,
      "baslik": "Purple 3.5 1TB 7200Rpm 64Mb Sata 3 6Gb/s 7/24 WD10PURZ",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "481 TL",
      "fiyat": "466,57 TL"
    },
    {
      "link": "https://www.trendyol.com/techmaster/aluminyum-hdd-caddy-notebook-pc-dvd-to-ssd-kutu-sata-9-5mm-db-095-p-48603988",
      "marka": "Techmaster",
      "yildiz": 4,
      "baslik": "Alüminyum Hdd Caddy Notebook Pc Dvd To Ssd Kutu Sata 9.5mm Db-095",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "28,40 TL"
    },
    {
      "link": "https://www.trendyol.com/wd/my-passport-2tb-2-5-inc-usb-3-2-mavi-tasinabilir-disk-byvg0020bbl-wesn-p-34888668",
      "marka": "WD",
      "yildiz": 4,
      "baslik": "My Passport 2tb 2.5 Inc Usb 3.2 Mavi Taşınabilir Disk Byvg0020bbl-wesn",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "699 TL",
      "fiyat": "678,03 TL"
    },
    {
      "link": "https://www.trendyol.com/sandisk/ultra-sdhc-80mb-s-class-10-uhs-i-hafiza-karti-64-gb-sdsdunc-064g-gn6in-p-2695265",
      "marka": "SanDisk",
      "yildiz": 4,
      "baslik": "Ultra SDHC 80MB/s Class 10 UHS-I Hafıza Kartı 64 GB SDSDUNC-064G-GN6IN",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "88,90 TL"
    },
    {
      "link": "https://www.trendyol.com/compaxe/2-5-hdd-external-case-usb-2-0-p-49809949",
      "marka": "COMPAXE",
      "yildiz": 4,
      "baslik": "2.5 Hdd External Case Usb 2.0",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "50,66 TL"
    },
    {
      "link": "https://www.trendyol.com/maxtor/m3-1tb-2-5-usb-3-0-tasinabilir-harddisk-p-34204470",
      "marka": "Maxtor",
      "yildiz": 4,
      "baslik": "M3 1tb 2.5\" Usb 3.0 Taşınabilir Harddisk",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "499 TL",
      "fiyat": "484,03 TL"
    },
    {
      "link": "https://www.trendyol.com/hadron/hd4631-500-usb-3-0-hdd-kablosu-50-cm-p-31651466",
      "marka": "HADRON",
      "yildiz": 4,
      "baslik": "Hd4631/500 Usb 3.0 Hdd Kablosu 50 cm",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "43,16 TL"
    },
    {
      "link": "https://www.trendyol.com/wozlo/jonsbo-m-2-ssd-aluminyum-isi-emici-termal-pedli-sogutucu-rgb-p-102090261",
      "marka": "WOZLO",
      "yildiz": 0,
      "baslik": "Jonsbo M.2 Ssd Alüminyum Isı Emici Termal Pedli Soğutucu Rgb",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "154,90 TL"
    },
    {
      "link": "https://www.trendyol.com/platoon/m-sata-ssd-hardisk-kutusu-usb-3-0-msata-to-usb-m-sata-usb-3-0-kutu-p-99227691",
      "marka": "Platoon",
      "yildiz": 0,
      "baslik": "M Sata Ssd Hardisk Kutusu Usb 3.0 Msata To Usb M-sata Usb 3.0 Kutu",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "83,60 TL"
    },
    {
      "link": "https://www.trendyol.com/wozlo/msata-ssd-to-2-5-inc-sata-6gbps-disk-donusturucu-p-92567404",
      "marka": "WOZLO",
      "yildiz": 0,
      "baslik": "Msata Ssd To 2.5 Inç Sata 6gbps Disk Dönüştürücü",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "54,90 TL"
    },
    {
      "link": "https://www.trendyol.com/intenso/siyah-tasinabilir-hard-disk-4tb-2-5-usb-3-0-p-52475114",
      "marka": "Intenso",
      "yildiz": 4,
      "baslik": "Siyah Taşınabilir Hard Disk 4tb 2.5\" Usb 3.0",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "914 TL",
      "fiyat": "886,58 TL"
    },
    {
      "link": "https://www.trendyol.com/toshiba/toshiba-canvio-basic-2-5-1tb-usb3-0-siyah-p-2824316",
      "marka": "Toshiba",
      "yildiz": 5,
      "baslik": "Toshıba Canvıo Basıc 2.5\" 1Tb Usb3.0-Siyah",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "407 TL"
    },
    {
      "link": "https://www.trendyol.com/seagate/6tb-3-5-backup-plus-hub-stel6000200-usb-3-0-harici-harddisk-siyah-p-2925770",
      "marka": "Seagate",
      "yildiz": 4,
      "baslik": "6tb 3.5\" Backup Plus Hub Stel6000200 Usb 3.0 Harici Harddisk Siyah",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "1.599,99 TL",
      "fiyat": "1.551,99 TL"
    },
    {
      "link": "https://www.trendyol.com/intenso/siyah-tasinabilir-harddisk-2tb-2-5-usb-3-0-p-40177524",
      "marka": "Intenso",
      "yildiz": 4,
      "baslik": "Siyah Taşınabilir Harddisk 2tb 2.5\" Usb 3.0",
      "indirim": "Sepette %3 İndirim",
      "indirimsiz": "557,90 TL",
      "fiyat": "541,16 TL"
    },
    {
      "link": "https://www.trendyol.com/asus/wsd-a1-32gb-ssd-usb-2-0-wi-fi-harici-disk-p-2826731",
      "marka": "ASUS",
      "yildiz": 4,
      "baslik": "WSD-A1-32GB SSD USB 2.0 WI-FI HARICI DISK",
      "indirim": null,
      "indirimsiz": null,
      "fiyat": "1.052,55 TL"
    }
  ]
}
"""

print(trendyol_kategori.tablo())
"""
tabulate verisi döndürür.

+------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------+------------------------------------------------------------------------------------------+--------------------+--------------+-------------+
| link                                                                                                                                     | marka       |   yildiz | baslik                                                                                   | indirim            | indirimsiz   | fiyat       |
|------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------+------------------------------------------------------------------------------------------+--------------------+--------------+-------------|
| https://www.trendyol.com/quantum/rdx-320-gb-2-5-usb-3-0-kirmizi-tasinabilir-disk-p-35426025                                              | Quantum     |        3 | Rdx 320 Gb 2.5" Usb 3.0 Kırmızı Taşınabilir Disk                                         | Sepette %3 İndirim | 149 TL       | 144,53 TL   |
| https://www.trendyol.com/realindirim/2-5-usb-3-0-harici-harddisk-hdd-kutusu-sata-disk-ssd-veri-aktarma-5-gbps-aluminyum-govde-p-33685614 | Realindirim |        2 | 2.5 Usb 3.0 Harici Harddisk Hdd Kutusu Sata Disk Ssd Veri Aktarma 5 Gbps Aluminyum Gövde |                    |              | 46,50 TL    |
| https://www.trendyol.com/kingston/datatraveler-g4-usb-3-0-bellek-32gb-dtig4-32gb-p-2516328                                               | Kingston    |        4 | DataTraveler G4 Usb 3.0 Bellek 32GB DTIG4/32GB                                           | Sepette %3 İndirim | 52,41 TL     | 50,84 TL    |
| https://www.trendyol.com/zore/3-0-lightning-metal-otg-64-gb-iphone-veri-ve-fotograf-depolama-kopyalama-flash-disc-p-102334392            | zore        |        0 | 3.0 Lightning Metal Otg 64 Gb Iphone Veri Ve Fotoğraf Depolama Kopyalama Flash Disc      |                    |              | 141,55 TL   |
| https://www.trendyol.com/zore/3-0-lightning-metal-otg-32-gb-iphone-veri-ve-fotograf-depolama-kopyalama-flash-disc-p-102333696            | zore        |        5 | 3.0 Lightning Metal Otg 32 Gb Iphone Veri Ve Fotoğraf Depolama Kopyalama Flash Disc      |                    |              | 113,05 TL   |
| https://www.trendyol.com/wd/3-5-8tb-elements-usb-3-0-siyah-tasinabilir-disk-wdbwlg0080hbk-eesn-p-6018856                                 | WD          |        4 | 3.5'' 8TB Elements USB 3.0 Siyah Taşınabilir Disk WDBWLG0080HBK-EESN                     |                    |              | 2.399,99 TL |
| https://www.trendyol.com/wd/my-passport-2tb-2-5-usb-3-0-siyah-backup-tasinabilir-disk-wdbs4b0020bbk-wesn-p-4066211                       | WD          |        4 | My Passport 2TB 2.5" USB 3.0 Siyah Backup Taşınabilir Disk WDBS4B0020BBK-WESN            | Sepette %3 İndirim | 700 TL       | 679 TL      |
| https://www.trendyol.com/wd/my-passport-black-worldwide-5tb-2-5-tasinabilir-disk-wdbpkj0050bbk-wesn-p-37040645                           | WD          |        4 | My Passport Black Worldwide 5TB 2.5" Taşınabilir Disk WDBPKJ0050BBK-WESN                 | Sepette %3 İndirim | 1.348 TL     | 1.307,56 TL |
| https://www.trendyol.com/appa/2-5-usb-3-0-sata-seffaf-harddisk-kutusu-srf-814-hdd-p-36339629                                             | Appa        |        4 | 2.5" Usb 3.0 Sata Şeffaf Harddisk Kutusu Srf-814-hdd                                     |                    |              | 75 TL       |
| https://www.trendyol.com/wd/purple-3-5-1tb-7200rpm-64mb-sata-3-6gb-s-7-24-wd10purz-p-2925859                                             | WD          |        3 | Purple 3.5 1TB 7200Rpm 64Mb Sata 3 6Gb/s 7/24 WD10PURZ                                   | Sepette %3 İndirim | 481 TL       | 466,57 TL   |
| https://www.trendyol.com/techmaster/aluminyum-hdd-caddy-notebook-pc-dvd-to-ssd-kutu-sata-9-5mm-db-095-p-48603988                         | Techmaster  |        4 | Alüminyum Hdd Caddy Notebook Pc Dvd To Ssd Kutu Sata 9.5mm Db-095                        |                    |              | 28,40 TL    |
| https://www.trendyol.com/wd/my-passport-2tb-2-5-inc-usb-3-2-mavi-tasinabilir-disk-byvg0020bbl-wesn-p-34888668                            | WD          |        4 | My Passport 2tb 2.5 Inc Usb 3.2 Mavi Taşınabilir Disk Byvg0020bbl-wesn                   | Sepette %3 İndirim | 699 TL       | 678,03 TL   |
| https://www.trendyol.com/sandisk/ultra-sdhc-80mb-s-class-10-uhs-i-hafiza-karti-64-gb-sdsdunc-064g-gn6in-p-2695265                        | SanDisk     |        4 | Ultra SDHC 80MB/s Class 10 UHS-I Hafıza Kartı 64 GB SDSDUNC-064G-GN6IN                   |                    |              | 88,90 TL    |
| https://www.trendyol.com/compaxe/2-5-hdd-external-case-usb-2-0-p-49809949                                                                | COMPAXE     |        4 | 2.5 Hdd External Case Usb 2.0                                                            |                    |              | 50,66 TL    |
| https://www.trendyol.com/maxtor/m3-1tb-2-5-usb-3-0-tasinabilir-harddisk-p-34204470                                                       | Maxtor      |        4 | M3 1tb 2.5" Usb 3.0 Taşınabilir Harddisk                                                 | Sepette %3 İndirim | 499 TL       | 484,03 TL   |
| https://www.trendyol.com/hadron/hd4631-500-usb-3-0-hdd-kablosu-50-cm-p-31651466                                                          | HADRON      |        4 | Hd4631/500 Usb 3.0 Hdd Kablosu 50 cm                                                     |                    |              | 43,16 TL    |
| https://www.trendyol.com/wozlo/jonsbo-m-2-ssd-aluminyum-isi-emici-termal-pedli-sogutucu-rgb-p-102090261                                  | WOZLO       |        0 | Jonsbo M.2 Ssd Alüminyum Isı Emici Termal Pedli Soğutucu Rgb                             |                    |              | 154,90 TL   |
| https://www.trendyol.com/platoon/m-sata-ssd-hardisk-kutusu-usb-3-0-msata-to-usb-m-sata-usb-3-0-kutu-p-99227691                           | Platoon     |        0 | M Sata Ssd Hardisk Kutusu Usb 3.0 Msata To Usb M-sata Usb 3.0 Kutu                       |                    |              | 83,60 TL    |
| https://www.trendyol.com/wozlo/msata-ssd-to-2-5-inc-sata-6gbps-disk-donusturucu-p-92567404                                               | WOZLO       |        0 | Msata Ssd To 2.5 Inç Sata 6gbps Disk Dönüştürücü                                         |                    |              | 54,90 TL    |
| https://www.trendyol.com/intenso/siyah-tasinabilir-hard-disk-4tb-2-5-usb-3-0-p-52475114                                                  | Intenso     |        4 | Siyah Taşınabilir Hard Disk 4tb 2.5" Usb 3.0                                             | Sepette %3 İndirim | 914 TL       | 886,58 TL   |
| https://www.trendyol.com/toshiba/toshiba-canvio-basic-2-5-1tb-usb3-0-siyah-p-2824316                                                     | Toshiba     |        5 | Toshıba Canvıo Basıc 2.5" 1Tb Usb3.0-Siyah                                               |                    |              | 407 TL      |
| https://www.trendyol.com/seagate/6tb-3-5-backup-plus-hub-stel6000200-usb-3-0-harici-harddisk-siyah-p-2925770                             | Seagate     |        4 | 6tb 3.5" Backup Plus Hub Stel6000200 Usb 3.0 Harici Harddisk Siyah                       | Sepette %3 İndirim | 1.599,99 TL  | 1.551,99 TL |
| https://www.trendyol.com/intenso/siyah-tasinabilir-harddisk-2tb-2-5-usb-3-0-p-40177524                                                   | Intenso     |        4 | Siyah Taşınabilir Harddisk 2tb 2.5" Usb 3.0                                              | Sepette %3 İndirim | 557,90 TL    | 541,16 TL   |
| https://www.trendyol.com/asus/wsd-a1-32gb-ssd-usb-2-0-wi-fi-harici-disk-p-2826731                                                        | ASUS        |        4 | WSD-A1-32GB SSD USB 2.0 WI-FI HARICI DISK                                                |                    |              | 1.052,55 TL |
+------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------+------------------------------------------------------------------------------------------+--------------------+--------------+-------------+
"""