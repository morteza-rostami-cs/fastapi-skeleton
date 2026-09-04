
# keep the function who perform jobs here

import asyncio

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