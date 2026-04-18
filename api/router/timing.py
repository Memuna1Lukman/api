from fastapi import APIRouter,Depends,HTTPException,status
from .. import models,schemas,utils
from ..database import get_db
from sqlalchemy.orm import Session
from datetime import datetime,timedelta

router = APIRouter(
    prefix= "/timing",
    tags= ['Timing']
)


@router.post("/")
def rate_timing(user: schemas.TimingLimit,limit = 5,db:Session= Depends(get_db)):
    now = datetime.utcnow()
    window_minutes= timedelta(minutes=1)
    

    query_api_keys = db.query(models.Timing).filter(
        models.Timing.api_keys == user.api_keys,
        models.Timing.created_at >= (now - window_minutes)
        ).count()
    # do the the counting but i do not know how and also 
    # i have to have an if-else statement to check the limit
    if query_api_keys > limit:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,detail=f"Too many requestions try after a minute")
    
    query_timing = models.Timing(api_keys = user.api_keys,created_at=now)
    db.add(query_timing)
    db.commit()
    db.refresh(query_timing)
    return {"message" : "API successful"}

