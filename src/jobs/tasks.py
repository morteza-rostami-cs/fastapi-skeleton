
# keep the function who perform jobs here

import asyncio
from arq import Retry

# worker calls this function to -- execute the job
async def send_welcome_email(
   ctx: dict, # arq passes this context
   user_id: int
   ):
   print(f"task: sending email to: {user_id}")

   # access job info
   print(f"Job ID: {ctx['job_id']}")
   print(f"Job tries: {ctx['job_try']}")

   await asyncio.sleep(5)

   print(f"task: welcome email to: {user_id}")

# a job that fails
async def failing_job(ctx: dict):
   print("job: failing job")

   await asyncio.sleep(1)

   raise Retry() # retry the job if max_tries is set inside WorkerSettings