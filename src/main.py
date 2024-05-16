from fastapi import FastAPI
import uvicorn

from src.books.routers import router as book_router


app = FastAPI()

app.include_router(book_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
