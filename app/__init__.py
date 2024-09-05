from fastapi import FastAPI
from config import Text

fun = FastAPI(title=Text.TITLE, version=Text.VERSION, description=Text.DESCRIPTION)
