from fastapi import FastAPI

# fastapi main app
app = FastAPI()

@app.get("/")
def home():
   return dict(message="hi, fastapi")