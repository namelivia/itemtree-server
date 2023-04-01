from fastapi import APIRouter, Path, HTTPException, Depends, Response, Header
from typing import Optional
from http import HTTPStatus
from app.dependencies import get_db
from . import crud, schemas
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(prefix="/items", dependencies=[Depends(get_db)])


@router.get("", response_model=List[schemas.Item])
def items(db: Session = Depends(get_db), parent: Optional[int] = None):
    return crud.get_items_for_parent_id(db, parent)


def _get_item(db: Session, item_id: int):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")
    return db_item


@router.get("/{item_id}", response_model=schemas.Item)
def get_item(
    item_id: int = Path(title="The ID of the item to get", ge=1),
    db: Session = Depends(get_db),
):
    return _get_item(db, item_id)


@router.post("", response_model=schemas.Item, status_code=HTTPStatus.CREATED)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    x_pomerium_jwt_assertion: Optional[str] = Header(None),
):
    return crud.create_item(db, item, x_pomerium_jwt_assertion)


@router.put("/{item_id}", response_model=schemas.Item, status_code=HTTPStatus.OK)
def update_item(
    new_item_data: schemas.ItemUpdate,
    db: Session = Depends(get_db),
    item_id: int = Path(title="The ID for the item to update", ge=1),
):
    return crud.update_item(db, item_id, new_item_data)


@router.delete("/{item_id}")
async def delete_item(
    item_id: int = Path(title="The ID of the item to remove", ge=1),
    db: Session = Depends(get_db),
):
    crud.delete_item(db, _get_item(db, item_id))
    return Response(status_code=HTTPStatus.NO_CONTENT)
