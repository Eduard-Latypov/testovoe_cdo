from pydantic import BaseModel, ConfigDict


class BookPOST(BaseModel):
    title: str
    author: str
    category: str
    isbn: int


class BookGET(BookPOST):
    id: int

    model_config = ConfigDict(from_attributes=True)
