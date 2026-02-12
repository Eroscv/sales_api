from fastapi import APIRouter
from mongo.mongo_client import text_collection
from schemas.text_schema import TextCreate

router = APIRouter(prefix="/texts", tags=["Text Search"])

@router.post("/")
def create_text(payload: TextCreate):
    doc = {
        "sale_id": payload.sale_id,
        "text": payload.text
    }
    result = text_collection.insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc


@router.get("/search")
def search_text(query: str):
    return list(text_collection.find(
        {"text": {"$regex": query, "$options": "i"}},
        {"_id": 0}
    ))
