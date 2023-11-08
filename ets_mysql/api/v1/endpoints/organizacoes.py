from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from models.organizacao_model import OrganizacaoModel
from schemas.organizacao_schema import OrganizacaoSchemaBase, OrganizacaoSchemaMembros
from core.deps import get_session

router = APIRouter()

# POST Organização
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OrganizacaoSchemaBase)
async def post_organizacao(organizacao: OrganizacaoSchemaBase, db: AsyncSession = Depends(get_session)):
    nova_organizacao: OrganizacaoModel = OrganizacaoModel(nome=organizacao.nome, localidade=organizacao.localidade)

    db.add(nova_organizacao)
    await db.commit()

    return nova_organizacao

# POST Organização
@router.get('/', response_model=List[OrganizacaoSchemaBase])
async def get_organizacoes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OrganizacaoModel)
        result = await session.execute(query)
        organizacoes: List[OrganizacaoSchemaBase] = result.scalars().unique().all()

        return organizacoes