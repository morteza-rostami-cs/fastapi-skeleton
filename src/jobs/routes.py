from arq import ArqRedis
from fastapi import FastAPI, APIRouter, Depends

from src.jobs.constants import WELCOME_EMAIL_JOB
from src.common.constants import API_PREFIX

# dependency
from src.jobs.dependency import get_arq_pool

def register_job_routes(
   app: FastAPI, 
   ):

   router = APIRouter()

   @router.post("/test-job")
   async def test_job(
      arq_pool: ArqRedis = Depends(get_arq_pool), # inject arq_pool
   ):

      # create and queue a job
      job = await arq_pool.enqueue_job(
         WELCOME_EMAIL_JOB, # handler function
         123, # user_id
      )

      return dict(
         message="job queued",
         job_id= job.job_id,
      )

   app.include_router(router, prefix=f"{API_PREFIX}/jobs")