import os
import importlib
from fastapi import APIRouter
import sys

sys.path.append("..")

api_router = APIRouter()

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and file != "router.py":
        module_name = file[:-3]
        module = importlib.import_module(f".{module_name}", package="routes")
        if hasattr(module, "router"):
            api_router.include_router(module.router, tags=[module_name])
        