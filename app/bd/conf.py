from sqlalchemy import create_engine

DATABASE_URL =   "postgresql://rhuan:AxR256396dd@localhost:5432/loja_db"

engine = create_engine(DATABASE_URL)

try:
    engine.connect()
    print("Conexão realizada com suceso")
except Exception as e:
    raise("Erro ao conectar: {e}")