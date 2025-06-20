"""Add date to comments

Revision ID: 0fac21601078
Revises: a0d7ea709e10
Create Date: 2021-02-28 11:13:43.562158

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0fac21601078"
down_revision = "a0d7ea709e10"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "date",
                sa.DateTime(),
                server_default=sa.text("CURRENT_TIMESTAMP"),
                nullable=False,
            )
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.drop_column("date")

    # ### end Alembic commands ###
