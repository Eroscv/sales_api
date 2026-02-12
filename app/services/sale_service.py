from sqlalchemy.orm import Session
from models.sale_model import Sale

def create_sale(db: Session, data):
    sale = Sale(**data.dict())
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale


def get_sale(db: Session, sale_id: int):
    return db.query(Sale).filter(Sale.id == sale_id).first()


def list_sales(db: Session, category=None, start_date=None, end_date=None):
    query = db.query(Sale)

    if category:
        query = query.filter(Sale.category == category)
    if start_date:
        query = query.filter(Sale.sale_date >= start_date)
    if end_date:
        query = query.filter(Sale.sale_date <= end_date)

    return query.all()


def update_sale(db: Session, sale_id: int, data):
    sale = get_sale(db, sale_id)
    if not sale:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(sale, key, value)

    db.commit()
    db.refresh(sale)
    return sale


def delete_sale(db: Session, sale_id: int):
    sale = get_sale(db, sale_id)
    if not sale:
        return None

    db.delete(sale)
    db.commit()
    return True
