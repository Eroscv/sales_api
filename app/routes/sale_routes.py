from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from services.sale_service import *
from schemas.sale_schema import SaleCreate, SaleUpdate
from mongo.mongo_client import text_collection
router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/")
def create(data: SaleCreate, db: Session = Depends(get_db)):
    return create_sale(db, data)


@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return list_sales(db)


@router.get("/{sale_id}")
def get_one(sale_id: int, db: Session = Depends(get_db)):
    sale = get_sale(db, sale_id)
    if not sale:
        raise HTTPException(404, "Sale not found")
    return sale


@router.put("/{sale_id}")
def update(sale_id: int, data: SaleUpdate, db: Session = Depends(get_db)):
    sale = update_sale(db, sale_id, data)
    if not sale:
        raise HTTPException(404, "Sale not found")
    return sale


@router.delete("/{sale_id}")
def delete(sale_id: int, db: Session = Depends(get_db)):
    ok = delete_sale(db, sale_id)
    if not ok:
        raise HTTPException(404, "Sale not found")
    return {"status": "deleted"}


@router.get("/search-sales")
def search_sales(query: str, db: Session = Depends(get_db)):
    matched_texts = text_collection.find(
        {"text": {"$regex": query, "$options": "i"}}
    )

    results = []

    for t in matched_texts:
        sale = db.query(Sale).filter(Sale.id == t["sale_id"]).first()
        if sale:
            results.append({
                "sale": sale,
                "text": t["text"]
            })

    return results
