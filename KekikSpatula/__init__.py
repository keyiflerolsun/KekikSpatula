# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

YAZAR       = 'keyiflerolsun'
YAZAR_POSTA = 'keyiflerolsun@gmail.com'

PAKET       = 'KekikSpatula'
VERSIYON    = '0.2.1'

REPO        = 'https://github.com/keyiflerolsun/KekikSpatula'
ACIKLAMA    = 'Siz uğraşmayın diye biz uğraştık.. ~ dızz 🐍'
ANAHTAR_KLM = [PAKET, 'KekikAkademi', 'keyiflerolsun']

with open(f'{PAKET}/requirements.txt') as dosya:
    GEREKSINIM = dosya.read().splitlines()

####
from KekikSpatula._Statik import Statik
from KekikSpatula.nobetciEczane import NobetciEczane
from KekikSpatula.akaryakit import Akaryakit
from KekikSpatula.doviz import Doviz
from KekikSpatula.deprem import SonDepremler
from KekikSpatula.bim import BimAktuel
from KekikSpatula.haber import SonDakika
from KekikSpatula.havaDurumu import HavaDurumu
from KekikSpatula.ezan import Ezan
from KekikSpatula.discudemy import DiscUdemy
####