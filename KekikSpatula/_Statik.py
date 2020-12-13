# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import json
from tabulate import tabulate
from attrdict import AttrDict
from typing import Any

class KekikSpatula(object):
    def __init__(self, kekik_json) -> None:
        super().__init__()
        self.kekik_json = kekik_json

    @property
    def veri(self) -> Any:
        "json verisi döndürür."
        return self.kekik_json or None

    @property
    def nesne(self) -> AttrDict:
        "json verisini python nesnesine dönüştürür"
        return AttrDict(self.kekik_json['veri'][0]) if len(self.kekik_json['veri']) == 1 else [obje for obje in AttrDict(self.kekik_json).veri]

    def gorsel(self, girinti:int=2, alfabetik:bool=False) -> Any:
        "oluşan json verisini insanın okuyabileceği formatta döndürür."
        return json.dumps(self.kekik_json, indent=girinti, sort_keys=alfabetik, ensure_ascii=False) if self.kekik_json else None

    def tablo(self, tablo_turu:str='psql') -> Any:
        "tabulate verisi döndürür."
        return tabulate(self.kekik_json['veri'], headers='keys', tablefmt=tablo_turu) if self.kekik_json else None

    @property
    def anahtarlar(self) -> Any:
        "kullanılan anahtar listesini döndürür."
        return [anahtar for anahtar in self.kekik_json['veri'][0].keys()] if self.kekik_json else None