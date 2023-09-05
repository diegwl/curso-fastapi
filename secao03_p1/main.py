from fastapi import FastAPI, status, HTTPException, Response, Path, Query, Header, Depends
from typing import Optional, Any, Dict, List
from models import Curso, cursos
from time import sleep

def fake_db():
    try: 
        print('Abrindo conexão com Banco de dados...')
        sleep(0.5)
    finally:
        print('Fechando conexão com Banco de dados...')
        sleep(0.5)

app = FastAPI(title="API de cursos da Geek University", version='0.0.1', description="Uma API para estudo do FastAPI")

@app.get('/cursos', 
        description='Retorna todos os cursos ou uma lista vazia.', 
        summary='Retorna todos os cursos', response_model=List[Curso], 
        response_description='Cursos encontrados com sucesso')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id :int = Path(title='ID do curso', 
                                        description=f'Deve estar entre 1 e 3', gt=0, lt=4), 
                                        db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    
@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso
    
@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}.')
    
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}')
    
@app.get('/calculadora')
async def calcular(a: int = Query(gt=0), b: int = Query(lt=200), c: Optional[int] = Query(default=0), x_geek: str = Header(default=None)):
    soma = a + b + c
    print(x_geek)

    return {"resultado": soma}

if __name__ == "__main__":
    import uvicorn 

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)