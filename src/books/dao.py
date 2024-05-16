from src.dao import BaseDAO
from .models import Book


class BookDAO(BaseDAO):
    model = Book
