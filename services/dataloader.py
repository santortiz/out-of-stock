import os
from pathlib import Path
import urllib.request
from zipfile import ZipFile
from typing import NoReturn

from src.logging import get_logger

DATASET = "out-of-stock"
DATA_PATH = f"./datalake/{DATASET}/"

logger = get_logger()


def load_dataset(dataset: str) -> NoReturn:
    zipfile_path = Path(os.path.join(DATA_PATH, f"{dataset}.zip"))
    if not zipfile_path.is_file():
        Path(DATA_PATH).mkdir(parents=True, exist_ok=True)
        url = f"https://github.com/joefavergel/datasets/blob/main/{dataset}.zip?raw=true"
        urllib.request.urlretrieve(url, zipfile_path)
    Path(DATA_PATH).mkdir(parents=True, exist_ok=True)
    try:
        ZipFile(zipfile_path).extractall(os.path.join(DATA_PATH, f"{dataset}"))
        logger.info(f"Dataset \'{dataset}\' downloaded and uncompressed correctly!")
    except Exception as e:
        logger.error(f"There's been a problem: {e}")


def main() -> NoReturn:
    load_dataset(dataset=DATASET)


if __name__ == '__main__':
    main()
