# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

YAZAR       = 'keyiflerolsun'
YAZAR_POSTA = 'keyiflerolsun@gmail.com'

PAKET       = 'KekikSpatula'
VERSIYON    = '0.1.9'

REPO        = 'https://github.com/keyiflerolsun/KekikSpatula'
ACIKLAMA    = 'Siz uğraşmayın diye biz uğraştık.. ~ dızz 🐍'
ANAHTAR_KLM = ['KekikSpatula', 'KekikAkademi', 'keyiflerolsun']

GEREKSINIM  = [
    "requests==2.24.0",
    "tabulate==0.8.7",
    "beautifulsoup4==4.9.3",
    "lxml==4.6.1",
    "pandas==1.1.4"
]

from KekikSpatula.nobetciEczane import NobetciEczane
from KekikSpatula.akaryakit import Akaryakit
from KekikSpatula.doviz import Doviz
from KekikSpatula.deprem import SonDepremler
from KekikSpatula.bim import BimAktuel
from KekikSpatula.haber import SonDakika
from KekikSpatula.havaDurumu import HavaDurumu
from KekikSpatula.ezan import Ezan
from KekikSpatula.discudemy import DiscUdemy