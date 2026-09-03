from sqlmodel import create_engine
from src.common.settings import settings

# not a single db connection -- more like a connection manager
engine = create_engine(
   url=str(settings.database_url),
)