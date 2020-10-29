# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
rm -rf build/
rm -rf dist/
rm -rf -- *.egg-info/
