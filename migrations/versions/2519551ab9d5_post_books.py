"""post books

Revision ID: 2519551ab9d5
Revises: 82a1eb2569a1
Create Date: 2024-03-23 22:46:39.506732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2519551ab9d5'
down_revision: Union[str, None] = '82a1eb2569a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('authors', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('authors', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=10, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###