from sqlalchemy import ForeignKey,Integer,Column,String,TIMESTAMP,text
from sqlalchemy.orm import relationship
from .database import Base



class User(Base):
    __tablename__ = "users"


    id = Column(Integer,primary_key=True)
    api_keys = Column(String,index=True,nullable=False,unique=True)
    name = Column(String,index=True,nullable=False)
  


class Timing(Base):
    __tablename__ = "timing"

    id = Column(Integer,primary_key=True)
    api_key = Column(String,ForeignKey("users.api_keys",ondelete='CASCADE'),nullable=False)
    api = relationship("User")
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))    