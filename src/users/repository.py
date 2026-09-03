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