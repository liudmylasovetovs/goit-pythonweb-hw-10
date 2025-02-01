import uvicorn

from src.conf import messages
from fastapi import FastAPI

from src.api import utils, contacts, auth, users


app = FastAPI()

app.include_router(utils.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")


@app.get("/")
async def root():
    return {"message": messages.WELCOME_MESSAGE}

if __name__ == "__main__":
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=4)


