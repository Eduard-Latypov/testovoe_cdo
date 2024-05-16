import io
import csv

from .schemas import BookGET
from .models import Book


async def data_to_csv_file(data: list[Book]):
    book_models = [BookGET.model_validate(book).dict() for book in data]
    fieldnames = list(BookGET.model_fields.keys())
    csv_file = io.StringIO(newline="")
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for book in book_models:
        writer.writerow(book)
    return csv_file.getvalue()
