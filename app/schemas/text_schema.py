from pydantic import BaseModel

class TextCreate(BaseModel):
    sale_id: int
    text: str
