from sqlmodel import Session, select

from src.database.connection import engine # database access
from src.users.model import User

class UserRepository:

   def get_all(self) -> list[User]:
      # db session
      with Session(engine) as session:
         # build a query to select all users
         query = select(User)

         # use session to execute query and return all users
         users = session.exec(query).all()

         return users


   def get_by_id(self, user_id: int) -> User | None:
      with Session(engine) as session:
         user = session.get(User, user_id)

         return user

   def create(self, user: User) -> User:
      with Session(engine) as session:
         session.add(user)
         session.commit() # save to db
         session.refresh(user)

         return user

   def update(self, user: User) -> User:
      with Session(engine) as session:
         session.add(user)
         session.commit()
         session.refresh(user)

         return user

   def delete(self, user: User) -> User:
      with Session(engine) as session:
         session.delete(user)
         session.commit()

         return user