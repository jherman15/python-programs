from PIL import Image
from pathlib import Path

if __name__ == '__main__':

    from os import listdir
    dir_path = Path(r'C:\python_lab_jh')
    a = Path('image2.jpg')
    b = a.with_suffix('.png')

    im1 = Image.open(dir_path / 'JPGs' / a)
    im1.save(dir_path / 'PNGs' / b)

    print('\nConverted.')

    #funkcja do konwersji, np. source destination -> zbiorowe konwertowanie
