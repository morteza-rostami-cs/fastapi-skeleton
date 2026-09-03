from sqlmodel import Field, SQLModel
from datetime import datetime, timezone

class User(
   SQLModel, 
   table=True, # it's a table
   ):

   id: int | None = Field(
      default=None,
      primary_key=True,
      )

   username: str = Field(
      index=True, # indexed
      unique=True,
      nullable=False, # can't be null
   )

   email: str = Field(
      index=True,
      unique=True,
      nullable=False, # required
   )

   hashed_password: str = Field(
      nullable=False
   )

   created_at: datetime = Field(
      default_factory=lambda: datetime.now(timezone.utc),
      nullable=False,
   )

   updated_at: datetime = Field(
      default_factory=lambda: datetime.now(timezone.utc),
      nullable=False,
   )