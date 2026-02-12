# app/services/analytics_service.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.sale_model import Sale

def sales_summary(db: Session):
    total_revenue = db.query(
        func.sum(Sale.quantity * Sale.unit_price)
    ).scalar() or 0

    avg_ticket = db.query(
        func.avg(Sale.quantity * Sale.unit_price)
    ).scalar() or 0

    by_category = db.query(
        Sale.category,
        func.sum(Sale.quantity)
    ).group_by(Sale.category).all()

    return {
        "total_revenue": float(total_revenue),
        "average_ticket": float(avg_ticket),
        "quantity_by_category": dict(by_category)
    }
