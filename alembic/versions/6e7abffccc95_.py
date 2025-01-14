"""empty message

Revision ID: 6e7abffccc95
Revises: 0d5dbe9e2933
Create Date: 2024-05-15 21:58:25.601864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e7abffccc95'
down_revision: Union[str, None] = '0d5dbe9e2933'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'books', ['isbn'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='unique')
    # ### end Alembic commands ###
