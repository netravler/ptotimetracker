from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas, auth, database
from sqlalchemy.orm import Session
from datetime import date

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
def login(user: schemas.UserLogin):
    if auth.authenticate_user(user.username, user.password):
        return {"username": user.username}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/requests")
def get_requests(db: Session = Depends(get_db)):
    return db.query(models.TimeOffRequest).all()

@app.post("/requests")
def add_request(req: schemas.PTORequest, db: Session = Depends(get_db)):
    db_req = models.TimeOffRequest(user_id=1, date=req.date, type=req.type)
    db.add(db_req)
    db.commit()
    db.refresh(db_req)
    return db_req
