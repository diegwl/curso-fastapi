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

# GET Organizações
@router.get('/', response_model=List[OrganizacaoSchemaBase])
async def get_organizacoes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OrganizacaoModel)
        result = await session.execute(query)
        organizacoes: List[OrganizacaoSchemaBase] = result.scalars().unique().all()

        return organizacoes

# GET Organização
@router.get('/{organizacao_id}', response_model=OrganizacaoSchemaMembros)
async def get_organizacao(organizacao_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OrganizacaoModel).filter(OrganizacaoModel.id == organizacao_id)
        result = await session.execute(query)
        organizacao = result.scalars().unique().one_or_none()
        print(organizacao)

        if organizacao:
            return organizacao
        else:
            raise HTTPException(detail='Organização não encontrada.', status_code=status.HTTP_404_NOT_FOUND)
        
# PUT Organização
@router.put('/{organizacao_id}', response_model=OrganizacaoSchemaBase)
async def put_organizacao(organizacao_id: int, organizacao: OrganizacaoSchemaBase, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OrganizacaoModel).filter(OrganizacaoModel.id == organizacao_id)
        result = await session.execute(query)
        organizacao_up = result.scalars().unique().one_or_none()

        if organizacao_up:
            organizacao_up.nome = organizacao.nome
            organizacao_up.localidade = organizacao.localidade

            await session.commit()

            return organizacao_up
        else:
            raise HTTPException(detail='Organização não encontrada.', status_code=status.HTTP_404_NOT_FOUND)
        
# DELETE Organização
@router.delete('/{organizacao_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_oganizacao(organizacao_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OrganizacaoModel).filter(OrganizacaoModel.id == organizacao_id)
        result = await session.execute(query)
        organizacao_del = result.scalars().unique().one_or_none()

        if organizacao_del:
            await session.delete(organizacao_del)

            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Organização não encontrada.', status_code=status.HTTP_404_NOT_FOUND)