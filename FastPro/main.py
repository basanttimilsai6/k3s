from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from db import Base, check_connection, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok", "db_connected": check_connection()}


@app.get("/sum")
def sum():
    return {"sum": 4}


# Example of using the session in an endpoint:
@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    return {"db_session": "active"}
