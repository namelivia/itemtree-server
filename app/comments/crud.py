from sqlalchemy.orm import Session
import logging
from . import models, schemas
from app.notifications.notifications import Notifications
from app.user_info.user_info import UserInfo

logger = logging.getLogger(__name__)


def get_comments_for_item_id(db: Session, item_id: int):
    return db.query(models.Comment).filter(models.Comment.item_id == item_id).all()


def create_comment(
    db: Session, comment: schemas.CommentCreate, x_pomerium_jwt_assertion
):
    db_comment = models.Comment(**comment.dict())
    user_info = UserInfo.get_current(x_pomerium_jwt_assertion)
    db_comment.user_id = user_info["sub"]
    db_comment.user_name = user_info["name"]
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    logger.info("New comment created")
    try:
        Notifications.send(f"A comment has been created")
    except Exception as err:
        logger.error(f"Notification could not be sent: {str(err)}")
    return db_comment
