"""Add monster_default_health to monster.3

Revision ID: 5fc9c9d64e37
Revises: 30eb3b5b072d
Create Date: 2023-08-10 20:32:58.334255

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5fc9c9d64e37'
down_revision: Union[str, None] = '30eb3b5b072d'
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
