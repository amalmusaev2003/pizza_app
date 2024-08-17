"""Add composition field to products table

Revision ID: a67bb57f43a4
Revises: 392b58a500ef
Create Date: 2024-08-17 04:48:56.377900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a67bb57f43a4'
down_revision: Union[str, None] = '392b58a500ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('composition', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'composition')
    # ### end Alembic commands ###
