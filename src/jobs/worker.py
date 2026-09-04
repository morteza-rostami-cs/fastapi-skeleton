
# import the jobs and configure worker

from arq import create_pool
from arq.connections import RedisSettings

from src.common.settings import settings
from src.jobs.constants import WELCOME_EMAIL_JOB # job name
from src.jobs.tasks import  (
   send_welcome_email,
   failing_job,
)

# on worker startup
async def startup(ctx):
   print("worker started")

# on worker shutdown
async def shutdown(ctx):
   print("worker shutdown")


class WorkerSettings:
   # register job handlers
   functions = [
      send_welcome_email,
      failing_job,
   ]


   # add redis
   redis_settings = RedisSettings.from_dsn(
      str(settings.redis_url), #redis url
   )

   max_tries = 3 # try 3 times on failure
   retry_jobs = True

   on_startup = startup
   on_shutdown = shutdown