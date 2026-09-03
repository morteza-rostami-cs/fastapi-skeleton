from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn

# if validation fails -- fail fast
class Settings(BaseSettings):

   database_url: PostgresDsn # maps to: DATABASE_URL

   model_config = SettingsConfigDict(
      env_file=".env",
      env_file_encoding="utf-8",
   )


settings = Settings()