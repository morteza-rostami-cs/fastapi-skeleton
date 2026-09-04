<!--

# Learning about background jobs:

- instead of blocking the http request
   register the job now
   worker process it in the background (separate process)

- flow:
   - http request
   - queue job in postgres and cache it in redis
   - responsenhn

   we have to different processes:
      - http api
      - worker process

   ~ so api, queues a job - inside a queue
   ~ worker process -- takes jobs from the queue -- and execute them

#=====

## job should only contain what worker needs to execute the job

{
   "task": "send_welcome_email",
   "user_id": 123
}

#=====
#=====
#=====
#=====
#=====
#=====
#=====

-->

```bash
# run worker process
python -m src.jobs.worker


```
