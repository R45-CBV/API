from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()
posts = []

@app.get("/")
async def root():
    return {"message": f"{posts}"}
    
@app.get("/{number}")
async def root(number:int):
    return {"message": f"{posts[number]}"}


@app.post("/createpost")
def create_post(turtle: dict = Body(...)):
    posts.append(turtle)
    return{f"post created, {turtle['title']}, {turtle['content']}"}
