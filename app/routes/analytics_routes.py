from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models.sale_model import Sale
from mongo.mongo_client import text_collection

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/sales-with-texts")
def sales_with_texts(db: Session = Depends(get_db)):
    sales = db.query(Sale).all()
    output = []

    for sale in sales:
        texts = list(text_collection.find(
            {"sale_id": sale.id},
            {"_id": 0}
        ))

        output.append({
            "sale": sale,
            "texts": texts
        })

    return output
