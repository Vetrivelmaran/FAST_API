from datetime import datetime
from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel
from sqlalchemy.orm import Session

# local script file
import models
from database import engine,SessionLocal

app =FastAPI()
models.Base.metadata.create_all(bind=engine)
class StuBase(BaseModel):
    id:int
    name:str
    section:str
    
def get_db()->Session:
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency =Depends(get_db)


@app.get('/')
async def hello():
    return ['hello world']


@app.post('/addstu')
async def create_stu(student:StuBase,db:Session=db_dependency):
    db_stu=models.Student(id=student.id,name=student.name,section=student.section)
    db.add(db_stu)
    db.commit()
    return 'added succesfully'
# get by id
@app.get('/getbyid/{stu_id}')
async def get_by_id(stu_id:int,db:Session=db_dependency):
    db_stu=db.query(models.Student).filter(models.Student.id==stu_id).order_by(models.Student.id).first()
    if db_stu is None:
        raise HTTPException(status_code=404,detail="user not fond")
    return db_stu

#update
@app.put('/stu/{stu_id}',status_code=status.HTTP_200_OK)
async def update_stu(stu_id:int,student:StuBase,db:Session=db_dependency):
    db_stu=db.query(models.Student).filter(models.Student.id==stu_id).first()
    if db_stu is None:
        raise HTTPException(status_code=404,detail="student not found")
    db_stu.name=student.name
    db_stu.section=student.section
    db.commit()
    db.refresh(db_stu)
    
    return db_stu


    
@app.get('/getall')
async def get_all_students(db: Session =db_dependency):
    db_stu = db.query(models.Student).all()
    return db_stu


@app.delete('/delete_stu/{stu_id}', status_code=status.HTTP_200_OK)
async def delete_stu(stu_id: int, db: Session = db_dependency):
    # Fetch the student from the database
    db_stu = db.query(models.Student).filter(models.Student.id == stu_id).first()

    # Check if the student exists
    if db_stu is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # "Soft delete" by updating the deleted_at field
    db_stu.deleted_at = datetime.utcnow()
    db.commit()
    db.refresh(db_stu)

    return {'message': 'Student deleted successfully'}