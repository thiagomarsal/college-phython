# IT 280 – Lab #10: File Compression Instructions
from pathlib import Path
from zipfile import ZipFile


def main():
    files = ['./randomValues_1.txt', './randomValues_2.txt']
    path = Path('./zip', 'all_files.zip')

    if path.parent.exists() is False:
        path.parent.mkdir()

    with ZipFile(path, 'w') as zip:
        for file in files:
            if Path(file).exists:
                zip.write(file)


main()