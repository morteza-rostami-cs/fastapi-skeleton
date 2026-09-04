from fastapi import Request

# get the arq_pool inside routes -- after async stuff is done and app.state has it!
async def get_arq_pool(request: Request):
   return request.app.state.arq_pool