"""Add images to items

Revision ID: 4bc473d08efd
Revises: eaba23ec4033
Create Date: 2021-02-27 11:29:58.240750

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4bc473d08efd"
down_revision = "eaba23ec4033"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.add_column(sa.Column("image", sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.drop_column("image")

    # ### end Alembic commands ###
