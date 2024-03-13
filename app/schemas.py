from pydantic import BaseModel


class TreeCountRequest(BaseModel):
    city: str
    country: str
    year: int