import uvicorn
from fastapi import Depends, FastAPI, HTTPException

from Users import router as user_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
