from fastapi import FastAPI
from .cors import register_cors_middleware


def register_middlewares(app: FastAPI):
    register_cors_middleware(app)
