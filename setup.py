# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io import open

from KekikSpatula import YAZAR, YAZAR_POSTA, PAKET, VERSIYON, REPO, ACIKLAMA, ANAHTAR_KLM

with open(f'{PAKET}/requirements.txt') as dosya:
    GEREKSINIM = dosya.read().splitlines()

setup(
    author       = YAZAR,
    author_email = YAZAR_POSTA,

    packages     = [PAKET],

    name         = PAKET,
    version      = VERSIYON,
    url          = REPO,
    description  = ACIKLAMA,
    keywords     = ANAHTAR_KLM,

    long_description_content_type   = "text/markdown",
    long_description                = "".join(open("README.md", encoding="utf-8").readlines()),
    include_package_data            = True,

    license     = 'GPLv3+',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3'
    ],

    python_requires     = '>=3.6',
    install_requires    = GEREKSINIM
)
