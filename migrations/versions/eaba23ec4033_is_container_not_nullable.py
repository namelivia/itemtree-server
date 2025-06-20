"""Is container not nullable

Revision ID: eaba23ec4033
Revises: e1c5d4e541fc
Create Date: 2021-02-27 10:04:35.108781

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "eaba23ec4033"
down_revision = "e1c5d4e541fc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.alter_column(
            "is_container", existing_type=sa.BOOLEAN(), nullable=False
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.alter_column("is_container", existing_type=sa.BOOLEAN(), nullable=True)

    # ### end Alembic commands ###
