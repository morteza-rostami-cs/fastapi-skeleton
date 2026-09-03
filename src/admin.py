from fastapi import FastAPI
from sqladmin import Admin, ModelView

from src.database.connection import engine
from src.users.model import User


class UserAdmin(ModelView, model=User):
   name = "User"
   name_plural = "Users"

   column_list = [
      User.id,
      User.username,
      User.email,
      User.created_at,
      User.updated_at,
   ]

   column_searchable_list = [
      User.username,
      User.email,
   ]

   column_sortable_list = [
      User.id,
      User.username,
      User.email,
      User.created_at,
      User.updated_at,
   ]


def register_admin(app: FastAPI):
   admin = Admin(
      app,
      engine,
      title="Application Admin",
   )

   admin.add_view(UserAdmin)

   return admin