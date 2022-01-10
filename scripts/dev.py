import os

def start():
    os.system("uvicorn fastapi_adapter.main:app --reload --reload-dir ./ --app-dir ./")

def mock():
    os.system("./scripts/whatsapp-business-api-mock --configfile scripts/config.json")