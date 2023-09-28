from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title="CURSO API - SEGURANÇA")
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
    
"""
{
    "acess_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2OTY1MjU2OTksImlhdCI6MTY5NTkyMDg5OSwic3ViIjoiNSJ9.rHX2znj1chmzX7cSFXyl11GgXhTvH7BSWJ4WMLHTNPE",
    "token_type": "bearer"
}
"""