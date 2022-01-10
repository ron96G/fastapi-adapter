import os

def generate_models():
    os.system("datamodel-codegen --input docs/openapi.yaml --output fastapi_whatsapp/models.py")

def generate_fastapi():
    os.system("fastapi-codegen --input docs/openapi.yaml --output fastapi_adapter")