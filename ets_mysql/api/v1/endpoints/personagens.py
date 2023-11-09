from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.personagem_model import PersonagemModel
from schemas.personagem_schema import PersonagemSchema
from core.deps import get_session

router = APIRouter()

# POST Personagem
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PersonagemSchema)
async def post_personagem(personagem: PersonagemSchema, db: AsyncSession = Depends(get_session)):
    novo_personagem: PersonagemModel = PersonagemModel(nome=personagem.nome, 
                                                       nacionalidade=personagem.nacionalidade, 
                                                       nascimento=personagem.nascimento, 
                                                       genero=personagem.genero, 
                                                       organizacao_id=personagem.organizacao_id)
    
    db.add(novo_personagem)
    await db.commit()

    return novo_personagem

# GET Personagens
@router.get('/', response_model=List[PersonagemSchema])
async def get_personagens(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagemModel)
        result = await session.execute(query)
        personagens: List[PersonagemModel] = result.scalars().unique().all()

        return personagens
    
# GET Personagem
@router.get('/{personagem_id}', response_model=PersonagemSchema, status_code=status.HTTP_200_OK)
async def get_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagemModel).filter(PersonagemModel.id == personagem_id)
        result = await session.execute(query)
        personagem: PersonagemModel = result.scalars().unique().one_or_none()

        if personagem:
            return personagem
        else:
            raise HTTPException(detail='Personagem não encontrado', status_code=status.HTTP_404_NOT_FOUND)
        
# PUT Personagem
@router.put('/{personagem_id}', response_model=PersonagemSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagemSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagemModel).filter(PersonagemModel.id == personagem_id)
        result = await session.execute(query)
        personagem_up: PersonagemModel = result.scalars().unique().one_or_none()

        if personagem_up:
            personagem_up.nome = personagem.nome
            personagem_up.nacionalidade = personagem.nacionalidade
            personagem_up.nascimento = personagem.nascimento
            personagem_up.genero = personagem.genero
            personagem_up.organizacao_id = personagem.organizacao_id
        
            await session.commit()

            return personagem_up
        else:
            raise HTTPException(detail='Personagem não encontrado', status_code=status.HTTP_404_NOT_FOUND)
        
# DELETE Personagem
@router.delete('/{personagem_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagemModel).filter(PersonagemModel.id == personagem_id)
        result = await session.execute(query)
        personagem_del: PersonagemModel = result.scalars().unique().one_or_none()

    if personagem_del:
        await session.delete(personagem_del)
        await session.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(detail='Personagem não encontrado', status_code=status.HTTP_404_NOT_FOUND)