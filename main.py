from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from contextlib import asynccontextmanager

app = FastAPI()