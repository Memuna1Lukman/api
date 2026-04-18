from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,utils



router = APIRouter(
    prefix= "/signup",
    tags= ['Sign Up']
)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponseApi)
def create_user_api(message:schemas.UserApi,db:Session=Depends(get_db)):
    generate_keys = utils.generate()
    hash_keys = utils.generate_api_keys(generate_keys)
    
    new_log = models.User(id= message.id,api_keys=hash_keys,name=message.name) 

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log


