from fastapi import APIRouter, Depends, Header
from typing import Optional
from http import HTTPStatus
from app.dependencies import get_db
from . import crud, schemas
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(prefix="/comments", dependencies=[Depends(get_db)])


@router.get("", response_model=List[schemas.Comment])
def comments(db: Session = Depends(get_db), item: Optional[int] = None):
    return crud.get_comments_for_item_id(db, item)


@router.post("", response_model=schemas.Comment, status_code=HTTPStatus.CREATED)
def create_comment(
    comment: schemas.CommentCreate,
    db: Session = Depends(get_db),
    x_pomerium_jwt_assertion: Optional[str] = Header(None),
):
    return crud.create_comment(db, comment, x_pomerium_jwt_assertion)
