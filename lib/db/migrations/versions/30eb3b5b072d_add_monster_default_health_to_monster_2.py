"""Add monster_default_health to monster.2

Revision ID: 30eb3b5b072d
Revises: f05772e5999c
Create Date: 2023-08-10 20:30:51.167614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30eb3b5b072d'
down_revision: Union[str, None] = 'f05772e5999c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###