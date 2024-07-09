from __future__ import annotations
import logging
import os
import sys
from typing import Optional


def get_logger(
    *,
    type_: str = 'stream',
    logs_path: str = None,
    filename: str = None,
    process_id: str | None = None
) -> logging.Logger:
    if type_ == 'file' and logs_path is not None and filename is not None:
        if not os.path.exists(logs_path):
            os.makedirs(logs_path, exist_ok=True)

        logs_output = os.path.join(logs_path, filename)
        if not os.path.isfile(logs_output):
            with open(logs_output, "w") as file:
                file.write("")
            file.close()

        logging.basicConfig(
            filename=os.path.join(logs_path, filename),
            filemode='w',
            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True,
            encoding='utf-8'
        )
    elif type_ == 'stream':
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
            stream=sys.stdout,
            force=True,
            encoding='utf-8'
        )
    else:
        raise Exception("Type of logger not supported or unknown")

    name = f"src-{process_id}" if process_id else "src"
    return logging.getLogger(name)


logger = get_logger(type_='stream')
