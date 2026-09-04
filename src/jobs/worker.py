# import the job
from src.jobs.tasks import process_example_job

def main():
   print("worker: started")

   process_example_job()

   print("worker: shutdown")

# we run this module directly (as a process on our os)
if __name__ == "__main__":
   main()