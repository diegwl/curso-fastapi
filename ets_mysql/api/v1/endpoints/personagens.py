from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.personagem_model import PersonagemModel
from schemas.personagem_schema import PersonagemSchema
from core.deps import get_session

router = APIRouter()
