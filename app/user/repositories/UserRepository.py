from app.shared.base.BaseRepository import BaseRepository
from app.user.entities.UserEntity import UserFromQuery, UserEntity
from app.user.models.UserModel import User
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session, lazyload
from config.database_config import Engine

class UserRepository(BaseRepository): 

    def __init__(self, eng:Engine):
        self.eng = eng
        
    def create(self, user):
        with Session(self.eng) as db:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
    
    def get_all(self):
        with Session(self.eng) as db:
            user = db.query(User).all()
            return user
    
    def get_by_id(self, id: int):
        with Session(self.eng) as db:
            user = db.query(User).filter(User.id==id).first()
            return user
    
    def update(self, Entity):
        return super().update(Entity)
    
    def delete(self, user_param):
        with Session(self.eng) as db:
            user = db.query(User).filter((User.Email==user_param) | (User.UserName==user_param)).first()
            return db.delete(user)
            
    def get_by_email(self, user_param):
        with Session(self.eng) as db:
            user = db.query(User).filter((User.Email==user_param) | (User.UserName==user_param)).first()
            return user
        
    def get_by_username_or_email(self, user):
        with Session(self.eng) as db:
            user = db.query(User).filter((User.Email==user.Email) | (User.UserName==user.UserName)).first()
            return user

            
        
       
        
    