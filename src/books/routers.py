from fastapi import APIRouter, status
from fastapi.responses import Response
from src.books.dao import BookDAO
from src.books.schemas import BookPOST, BookGET
from src.books.utils import data_to_csv_file


router = APIRouter(prefix="/books", tags=["книги"])


@router.get("/", response_model=list[BookGET])
async def get_all_books() -> Response:
    books = await BookDAO.get_all()
    file = await data_to_csv_file(books)
    headers = {"Content-Disposition": "filename=file.csv"}
    return Response(file, headers=headers, media_type="file/csv")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookPOST):
    result = await BookDAO.create(**book.model_dump())
    return {"id": result}


@router.put("/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: BookPOST):
    result = await BookDAO.update(book_id, **book.model_dump())
    return {"id": result}


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    result = await BookDAO.delete(book_id)
    return {"id": result}
