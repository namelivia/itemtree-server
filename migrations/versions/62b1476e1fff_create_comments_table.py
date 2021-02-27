"""Create comments table

Revision ID: 62b1476e1fff
Revises: 4bc473d08efd
Create Date: 2021-02-27 11:54:28.996703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "62b1476e1fff"
down_revision = "4bc473d08efd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "comments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_comments_id"), ["id"], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_comments_id"))

    op.drop_table("comments")
    # ### end Alembic commands ###
