from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas, database
from sqlalchemy.orm import Session
from .database import engine
from .ai_helper import generate_description

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Smart WareHouse API",
    description="Backend dla inteligentnego magazynu z AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "online", "message": "Smart WareHouse API jest gotowe do pracy!"}

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    """
    Dodaje nowy przedmiot do magazynu.
    """

    final_description = item.description
    if not final_description or final_description.strip() == "":
        print(f"--- Generuję opis AI dla: {item.name} ---")
        final_description = generate_description(item.name)

    db_item = models.Item(
        name=item.name,
        description=final_description,
        quantity=item.quantity,
        price=item.price
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

@app.get("/items/", response_model=list[schemas.ItemResponse])
def read_items(db: Session = Depends(database.get_db)):
    """
    Zwraca listę wszystkich przedmiotów w magazynie.
    """
    items = db.query(models.Item).all()
    return items

@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_items(item_id: int, db: Session = Depends(database.get_db)):

    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Nie znaleziono przedmiotu o tym ID")
    return db_item

@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item_update: schemas.ItemUpdate, db: Session = Depends(database.get_db)):
    db_item= db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Przedmiot nie istnieje")

    update_data = item_update.model_dump(exclude_unset=True)

    if "description" in update_data:
        desc = update_data["description"]
        if not desc or desc.strip() == "":
            name_to_use = update_data.get("name", db_item.name)
            print(f"--- Re-generuję opis AI dla: {name_to_use} ---")
            update_data["description"] = generate_description(name_to_use)

    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Nie można usunąć - przedmiot nie istnieje")

    db.delete(db_item)
    db.commit()
    return {"message": f"Przedmiot o ID {item_id} został pomyślnie usunięty"}