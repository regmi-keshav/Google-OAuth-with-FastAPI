from sqlalchemy.orm import Session
from models.user import User


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user_data: dict):
    db_user = User(
        id=user_data['sub'],
        name=user_data.get('name'),
        email=user_data.get('email')
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: str, user_data: dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user_data.get('name', db_user.name)
        db_user.email = user_data.get('email', db_user.email)
        db.commit()
        db.refresh(db_user)
    return db_user
