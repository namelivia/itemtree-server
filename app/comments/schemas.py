from pydantic import BaseModel, Field


class CommentBase(BaseModel):
    content: str = Field(title="Content for the comment")
    item_id: int = Field(title="Item for attaching the comment to")


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    user_id: str = Field(title="User id for the comment")

    class Config:
        orm_mode = True
