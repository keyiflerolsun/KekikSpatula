# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

python setup.py bdist_wheel sdist
twine check dist/*
python -m twine upload dist/*
rm -rf build/
rm -rf dist/
rm -rf -- *.egg-info/