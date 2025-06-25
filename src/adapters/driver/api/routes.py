from fastapi import APIRouter

# Rotas FastAPI para filmes
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}
