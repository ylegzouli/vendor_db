from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from lib import models, crud, database
# from . import models, database, crud
# from lib import models

app = FastAPI()

@app.on_event("startup")
def startup():
    database.init_db()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/stores/")
def read_stores(db: Session = Depends(get_db)):
    return crud.get_stores(db)
