# TODO: Maybe the filename crud is not that good since this is not CRUD anymore
from sqlalchemy.orm import Session
from sqlalchemy import func
import logging
from . import models, schemas
from app.notifications.notifications import Notifications
from app.user_info.user_info import UserInfo

logger = logging.getLogger(__name__)


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


# TODO: skip and limit
# TODO: passing around the whole assertion is something I can avoid
def get_items(db: Session, x_pomerium_jwt_assertion, skip, limit):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate, x_pomerium_jwt_assertion):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    logger.info("New item created")
    try:
        Notifications.send(f"The item {db_item.name} has been created")
    except Exception as err:
        logger.error(f"Notification could not be sent: {str(err)}")
    return db_item


def update_item(db: Session, item_id: int, new_item_data: schemas.ItemUpdate):
    items = db.query(models.Item).filter(models.Item.id == item_id)
    items.update(new_item_data, synchronize_session=False)
    db.commit()
    item = items.first()
    logger.info("Item updated")
    try:
        Notifications.send(f"The item {item.name} has been updated")
    except Exception as err:
        logger.error(f"Notification could not be sent: {str(err)}")
    return item


def delete_item(db: Session, item: models.Item):
    db.delete(item)
    db.commit()
    logger.info("Item deleted")
