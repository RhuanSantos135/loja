from fastapi import APIRouter, Depends
from .schemaproduto import Produto

router = APIRouter()



@router.post("/produto/cadastro")
def cadastrar_produto(new_produto: Produto):
    None