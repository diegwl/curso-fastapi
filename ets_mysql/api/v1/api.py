from fastapi import APIRouter

from api.v1.endpoints import organizacoes, personagens

api_router = APIRouter()

api_router.include_router(organizacoes.router, prefix='/organizacoes', tags=['organizacoes'])